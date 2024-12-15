# Flight Tracker Langchain ReAct Agent , (Powered by GEMINI Llm and Tavily and other real time API's.)

![Flight Tracker Banner](https://images.app.goo.gl/8zDroDCdbjAYZJfW6)

## Overview  
This repository contains a flight-tracking application that provides  flight information such as source, destination, departure, and arrival time.

It's ReAct Agent (Reason +Action) which executes in a loop by iteratively gathering information from external tools before providing an answer.

1.Thought (Thinks)

2.Action (Uses Tools)

3.Observation (Makes Decision)

It's built using Langchain framework.

The app leverages the **Tavily API** for flight data and an **LLM (Large Language Model)** to offer intuitive natural language queries and enhanced user interactions.

I have also added  Real time API's integration to fetch dynamic information about flights .
Integrate with Real time API 
aviationstack.com
Url of the API:https://api.aviationstack.com/v1/flights

Integrate with Real time Weather API'S  weather.com
link:http://api.weatherapi.com/v1/

-## Features  
- **Flight Status**: Track flights source and destination  information  
- **Natural Language Queries**: Ask questions like, *"What's the status of flight ABC123?"*  
- **Comprehensive Flight Details**: Source, destination, airline, delays, and more.  

- **Scalable Backend**: Modular architecture ready for enhancements.  

---

## Table of Contents  
1. [Installation](#installation)  
2. [API Key Setup](#api-key-setup)  
3. [Usage](#usage)  
4. [Project Structure](#project-structure)  
5. [Configuration](#configuration)  
6. [Contributing](#contributing)  
7. [License](#license)  

---

## Installation  

### Prerequisites  
- Python 3.8 or later  
- pipenv or pip  
- Tavily API account for access credentials
- Aviationstack API account for getting real time flight data information  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone
   https://github.com/Madhu-712/LLM-Agents-MOOC-.git
   Hackathon-/edit/main/README.md
     
   cd LLM-Agents-MOOC


 2.  Install dependencies:

pip install -r requirements.txt  


3.Set up your environment variables for the API keys (see below).

API Key Setup
Sign up on the Tavily API and retrieve your API key.

Create a .env file in the project root and add:

env
Environment Variables

TAVILY_API_KEY: Tavily API key for accessing flight data.
GOGGLE_API_KEY: LLM API key for natural language processing.
ACCESS_KEY:your_api_key(aviationstack API key) 
WEATHER_API_KEY="your_api_key (weatherapi)"

4.Ensure your keys are valid by running the API test:

bash
python test_api.py  


Usage
5.Start the Application
Run the main script to start the app:

bash
python app.py  


Example Queries
Track a flight by number:
"Where is flight AA123 currently?"
Check flight schedules:
"What flights are departing from JFK in the next hour?"

6.Settings
Modify config.py to customize default parameters like API timeouts or logging levels.

7.Contributing
We welcome contributions! Here's how you can help:

Fork the repository.
Create a feature branch:
bash
git checkout -b feature-name  

Commit your changes and push:
bash

git push origin feature-name  

Open a pull request.

License
This project is licensed under the MIT License.

Other References:
1.https://medium.com/@madhu.712/uc-berkeley-mooc-hackathon-2024-building-a-flight-agent-with-gemini-powered-by-tavily-api-e2c8168d298d

2.https://devpost.com/submit-to/22283-llm-agents-mooc-hackathon/manage/submissions/590914-gemini-flight-status-agents/project_details/edit

3.Other Real time flight API's
-https://rapidapi.com/aedbx-aedbx/api/aerodatabox

-https://aviation-edge.com/?gad_source=1&gclid=CjwKCAiAjeW6BhBAEiwAdKltMqLEJA8rI0n5KWNJuHdyYe79eylRZI30rJRKIyYjgN_Vg4HRh28_RBoCIEwQAvD_BwE

4.Specific api's from a flight carrier 
https://api.emirates.com/v2/flights











 





