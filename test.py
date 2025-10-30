from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List available models
models = genai.list_models()
for m in models:
    print(m.name)
