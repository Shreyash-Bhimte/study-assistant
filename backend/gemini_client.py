import os
import requests
import json

GEMINI_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"
GEMINI_STREAM_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:streamGenerateContent"

def ask_gemini(system_prompt: str, user_message: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": f"{system_prompt}\n\n{user_message}"}]}
        ]
    }
    response = requests.post(f"{GEMINI_URL}?key={api_key}", json=payload)
    if response.status_code != 200:
        raise Exception(f"Gemini API error: {response.text}")
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

def stream_gemini(system_prompt: str, user_message: str):
    api_key = os.getenv("GEMINI_API_KEY")
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": f"{system_prompt}\n\n{user_message}"}]}
        ]
    }
    with requests.post(
        f"{GEMINI_STREAM_URL}?key={api_key}&alt=sse",
        json=payload,
        stream=True
    ) as response:
        if response.status_code != 200:
            raise Exception(f"Gemini stream error: {response.text}")
        for line in response.iter_lines():
            if line:
                decoded = line.decode("utf-8")
                if decoded.startswith("data: "):
                    data = decoded[6:]
                    if data == "[DONE]":
                        return
                    try:
                        chunk = json.loads(data)
                        text = chunk["candidates"][0]["content"]["parts"][0]["text"]
                        yield text
                    except (KeyError, json.JSONDecodeError):
                        continue

def stream_summary(document_text: str):
    system_prompt = """You are a study assistant. Summarise the provided document as exactly 6 bullet points.
Each bullet point must start with • and be one clear sentence.
Return only the bullet points — no intro, no headers, no extra text."""

    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": f"{system_prompt}\n\nDOCUMENT:\n{document_text}"}]}
        ]
    }

    api_key = os.getenv("GEMINI_API_KEY")
    with requests.post(
        f"{GEMINI_STREAM_URL}?key={api_key}&alt=sse",
        json=payload,
        stream=True
    ) as response:
        if response.status_code != 200:
            raise Exception(f"Gemini stream error: {response.text}")
        for line in response.iter_lines():
            if line:
                decoded = line.decode("utf-8")
                if decoded.startswith("data: "):
                    data = decoded[6:]
                    if data == "[DONE]":
                        return
                    try:
                        chunk = json.loads(data)
                        text = chunk["candidates"][0]["content"]["parts"][0]["text"]
                        yield text
                    except (KeyError, json.JSONDecodeError):
                        continue


def generate_flashcards(document_text: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    prompt = """You are a study assistant. Generate exactly 5 flashcards from the provided document.
Return ONLY a JSON array with exactly 5 objects. Each object must have exactly two keys: "question" and "answer".
No markdown, no code fences, no explanation — only the raw JSON array.

Example format:
[{"question": "What is X?", "answer": "X is ..."}]

DOCUMENT:
""" + document_textimport os
import requests
import json

GEMINI_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"
GEMINI_STREAM_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:streamGenerateContent"

def ask_gemini(system_prompt: str, user_message: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": f"{system_prompt}\n\n{user_message}"}]}
        ]
    }
    response = requests.post(f"{GEMINI_URL}?key={api_key}", json=payload)
    if response.status_code != 200:
        raise Exception(f"Gemini API error: {response.text}")
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

def stream_gemini(system_prompt: str, user_message: str):
    api_key = os.getenv("GEMINI_API_KEY")
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": f"{system_prompt}\n\n{user_message}"}]}
        ]
    }
    with requests.post(
        f"{GEMINI_STREAM_URL}?key={api_key}&alt=sse",
        json=payload,
        stream=True
    ) as response:
        if response.status_code != 200:
            raise Exception(f"Gemini stream error: {response.text}")
        for line in response.iter_lines():
            if line:
                decoded = line.decode("utf-8")
                if decoded.startswith("data: "):
                    data = decoded[6:]
                    if data == "[DONE]":
                        return
                    try:
                        chunk = json.loads(data)
                        text = chunk["candidates"][0]["content"]["parts"][0]["text"]
                        yield text
                    except (KeyError, json.JSONDecodeError):
                        continue

def stream_summary(document_text: str):
    system_prompt = """You are a study assistant. Summarise the provided document as exactly 6 bullet points.
Each bullet point must start with • and be one clear sentence.
Return only the bullet points — no intro, no headers, no extra text."""

    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": f"{system_prompt}\n\nDOCUMENT:\n{document_text}"}]}
        ]
    }
    api_key = os.getenv("GEMINI_API_KEY")
    with requests.post(
        f"{GEMINI_STREAM_URL}?key={api_key}&alt=sse",
        json=payload,
        stream=True
    ) as response:
        if response.status_code != 200:
            raise Exception(f"Gemini stream error: {response.text}")
        for line in response.iter_lines():
            if line:
                decoded = line.decode("utf-8")
                if decoded.startswith("data: "):
                    data = decoded[6:]
                    if data == "[DONE]":
                        return
                    try:
                        chunk = json.loads(data)
                        text = chunk["candidates"][0]["content"]["parts"][0]["text"]
                        yield text
                    except (KeyError, json.JSONDecodeError):
                        continue

def generate_flashcards(document_text: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    prompt = """You are a study assistant. Generate exactly 5 flashcards from the provided document.
Return ONLY a JSON array with exactly 5 objects. Each object must have exactly two keys: "question" and "answer".
No markdown, no code fences, no explanation — only the raw JSON array.

Example format:
[{"question": "What is X?", "answer": "X is ..."}]

DOCUMENT:
""" + document_text

    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}]
    }
    response = requests.post(f"{GEMINI_URL}?key={api_key}", json=payload)
    if response.status_code != 200:
        raise Exception(f"Gemini API error: {response.text}")
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}]
    }

    response = requests.post(f"{GEMINI_URL}?key={api_key}", json=payload)
    if response.status_code != 200:
        raise Exception(f"Gemini API error: {response.text}")
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]