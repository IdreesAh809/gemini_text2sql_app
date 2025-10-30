from dotenv import load_dotenv
load_dotenv()  # Load environment variables from a .env file

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide the SQL query as a response
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")
        response = model.generate_content([prompt, question])
        return response.text.strip()
    except Exception as e:
        st.error(f"Gemini Error: {e}")
        return ""

# Function to retrieve data from SQL database
def read_sql_query(query):
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data

# Define prompt
prompt = """
You are an expert in converting English text into accurate SQL queries.
The database contains one table named STUDENT with columns: NAME, CLASS, SECTION, and MARKS.

Examples:
1️ Question: "How many student records are present?"
   → SQL: SELECT COUNT(*) FROM STUDENT;

2 Question: "Show all students who scored more than 80 marks."
   → SQL: SELECT * FROM STUDENT WHERE MARKS > 80;

Important:
- Only return the SQL query (no explanations, no quotes, no ```).
- Do not include any text like 'SQL Query:' or 'Answer:'.
"""

# Streamlit App
st.title("SQL Retrieval Bot using Google Gemini")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input:", key="input")
submit = st.button("Ask the Question")

if submit and question:
    sql_query = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(sql_query, language="sql")

    try:
        data = read_sql_query(sql_query)
        st.subheader("Query Result:")
        st.write(data)
    except Exception as e:
        st.error(f"Error executing SQL query: {e}")
