# SQL Retrieval Bot using Google Gemini

This project is a simple Streamlit application that converts natural language questions into SQL queries using Google Gemini and retrieves data from a SQLite database.

## Features
- Converts English text into SQL queries
- Executes the generated SQL on students.db
- Displays the query results in Streamlit

## Setup Instructions
1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate

## Install required packages
```
pip install -r requirements.txt
```
## Create a .env file in the root directory and add:
```
GOOGLE_API_KEY=your_api_key_here
```
## Run the Streamlit app:
``` 
streamlit run app.py
