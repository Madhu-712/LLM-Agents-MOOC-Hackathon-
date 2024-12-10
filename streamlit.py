#Install Libraries: 
pip install streamlit langchain google-generativeai tavily-search python-dateutil regex

import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain.llms import GooglePalm  # For Gemini
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from tavily_search import TavilySearch
from dateutil.parser import parse
from dateutil import tz
import os
import re

# Replace with your Tavily API key (using Streamlit secrets is recommended)
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
or
from google.colab import userdata
#os.environ["TAVILY_API_KEY"] = userdata.get("TAVILY_API_KEY")
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
or
# Set up Google  (Gemini)
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]  # Or set as env variable

llm = GoogleGenerativeAI(model="gemini-1.5-flash", 
google_api_key=os.environ["GOOGLE_API_KEY"])


@st.cache_data
def fetch_flight_data(flight_id):
    try:
        tavily = TavilySearch(api_key=TAVILY_API_KEY)
        query = f"Flight status of {flight_id}"
        response = tavily.search(query)
        flight_data = response["results"][0].get("data", {})
        return flight_data
    except Exception as e:
        st.error(f"Error fetching flight data: {e}")
        return {}


def utc_to_local(utc_time_str, timezone_str):
    if utc_time_str:
        try:
            utc_time = parse(utc_time_str)
            local_zone = tz.gettz(timezone_str)
            local_time = utc_time.astimezone(local_zone)
            return local_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        except Exception as e:
            st.warning(f"Error converting time: {e}. Returning original UTC time.")
            return utc_time_str
    return "N/A"


@st.tool
def get_flight_status(flight_id: str):
    flight_data = fetch_flight_data(flight_id)
    if not flight_data:
        return "Flight information not found."

    dep_key = next((key for key in ["estimatedOut", "actualOut", "scheduledOut"] if key in flight_data and flight_data[key]), None)
    arr_key = next((key for key in ["estimatedIn", "actualIn", "scheduledIn"] if key in flight_data and flight_data[key]), None)

    origin_city = flight_data.get("origin", {}).get("city", "N/A")
    destination_city = flight_data.get("destination", {}).get("city", "N/A")
    origin_timezone = flight_data.get("origin", {}).get("timezone", "UTC")
    destination_timezone = flight_data.get("destination", {}).get("timezone", "UTC")

    flight_details = {
        "source": origin_city,
        "destination": destination_city,
        "depart_time": utc_to_local(flight_data.get(dep_key), origin_timezone) if dep_key else "N/A",
        "arrival_time": utc_to_local(flight_data.get(arr_key), destination_timezone) if arr_key else "N/A",
        "status": flight_data.get("status", "N/A"),
    }

    return f"""The current status of flight {flight_id} from {flight_details["source"]} to {flight_details["destination"]} is {flight_details["status"]} with the departure time as {flight_details["depart_time"]} and arrival time as {flight_details["arrival_time"]}"""



class TavilySearchResults:
    def __init__(self):
        self.tavily = TavilySearch(api_key=TAVILY_API_KEY)

    def run(self, query):
        try:
            response = self.tavily.search(query)
            return str(response) 
        except Exception as e:
            return f"Error searching Tavily: {e}"

    def name(self):
      return "Tavily Search"

    def description(self):
      return "A tool to search using Tavily API"


# --- LangChain Agent Setup ---
flight_status_tool = Tool(
    name="Flight info",
    func=get_flight_status,
    description="Useful to get flight status info like arrival, departure, source, destination."
)

search_tool = TavilySearchResults()
tools = [search_tool, flight_status_tool]

prompt = PromptTemplate(
    template="""Answer the following questions as best as you can. You have access to the following tools: {tool_names}

{input}
{agent_scratchpad}""",
    input_variables=["input", "tool_names", "agent_scratchpad"],
)


# --- Streamlit App ---
st.title("Flight Status Agent with LangChain and Gemini")

user_query = st.text_input("Enter your flight-related query:")

if user_query:
    tool_names = [tool.name for tool in tools]
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    agent_scratchpad = ""
    final_prompt = prompt.format(input=user_query, tool_names=tool_names, agent_scratchpad=agent_scratchpad)

    try:
        response = agent.run(final_prompt)
        st.write(response)
    except Exception as e:
        st.error(f"Error running agent: {e}")





#Run the Streamlit app: streamlit run streamlit.py

