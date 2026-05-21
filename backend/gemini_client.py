import os
import requests

GEMINI_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

def ask_gemini(system_prompt: str, user_message: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": f"{system_prompt}\n\n{user_message}"}]
            }
        ]
    }

    response = requests.post(
        f"{GEMINI_URL}?key={api_key}",
        json=payload
    )

    if response.status_code != 200:
        raise Exception(f"Gemini API error: {response.text}")

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]