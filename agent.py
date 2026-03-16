import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load config dari .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Setup model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def tanya_agent(pertanyaan):
    try:
        response = model.generate_content(pertanyaan)
        print(f"Agent: {response.text}")
    except Exception as e:
        print(f"Waduh Error: {e}")

if __name__ == "__main__":
    print("--- AI Agent Lab Testing ---")
    tanya_agent("Halo bre! Coba jelasin singkat apa itu airdrop crypto ke orang awam.")
