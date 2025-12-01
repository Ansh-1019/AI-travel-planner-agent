import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")  # or whatever your course says

response = model.generate_content("Say hello in one short sentence.")
print(response.text)
