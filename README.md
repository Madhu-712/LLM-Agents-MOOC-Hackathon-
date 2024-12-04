# Flight Tracker powered by GEMINI LLM and Tavily API.

![Flight Tracker Banner](https://images.app.goo.gl/8zDroDCdbjAYZJfW6)

## Overview  
This repository contains a flight-tracking application that provides  flight information such as source, destination, departure, and arrival times. The app leverages the **Tavily API** for flight data and an **LLM (Large Language Model)** to offer intuitive natural language queries and enhanced user interactions.

---

## Features  
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

### Steps  
1. Clone the repository:  
   ```bash  
   git clone
   https://github.com/Madhu-712/LLM-Agents-MOOC-.git
   Hackathon-/edit/main/README.md
     
   cd LLM-Agents-MOOC

2.#Install dependencies 
pip install -r requirements.txt  

3.Set up your environment variables for the API keys (see below).

API Key Setup
Sign up on the Tavily API and retrieve your API key.

Create a .env file in the project root and add:

env
Copy code
TAVILY_API_KEY=your_api_key  
GEMINI_API_KEY=your_llm_api_key  
Ensure your keys are valid by running the API test:

bash
Copy code
python test_api.py  
Usage
Start the Application
Run the main script to start the app:

bash
Copy code
python app.py  
Example Queries
Track a flight by number:
"Where is flight AA123 currently?"
Check flight schedules:
"What flights are departing from JFK in the next hour?"

Environment Variables
TAVILY_API_KEY: Tavily API key for accessing flight data.
GOGGLE_API_KEY: LLM API key for natural language processing.
Settings
Modify config.py to customize default parameters like API timeouts or logging levels.

Contributing
We welcome contributions! Here's how you can help:

Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature-name  
Commit your changes and push:
bash
Copy code
git push origin feature-name  
Open a pull request.
License
This project is licensed under the MIT License.













 





