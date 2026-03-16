import os
from openai import OpenAI

print("AI Agent starting...")

api_key = os.getenv("AI_API_KEY")

if not api_key:
    print("API key not found")
else:
    client = OpenAI(api_key=api_key)

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            print("Agent stopped")
            break

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user
        )

        print("Agent:", response.output_text)
