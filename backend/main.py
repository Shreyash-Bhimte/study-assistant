from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException
from file_parser import extract_text_from_pdf, extract_text_from_txt
from models import UploadResponse
from gemini_client import ask_gemini
from models import UploadResponse, QuestionRequest, AnswerResponse

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

MAX_CHARS = 50_000

@app.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ("application/pdf", "text/plain"):
        raise HTTPException(status_code=400, detail="Only PDF or .txt files are supported.")
    
    file_bytes = await file.read()

    if file.content_type == "application/pdf":
        text = extract_text_from_pdf(file_bytes)
    else:
        text = extract_text_from_txt(file_bytes)

    if not text.strip():
        raise HTTPException(status_code=422, detail="No text could be extracted from this file.")

    text = text[:MAX_CHARS]
    return UploadResponse(text=text, char_count=len(text))

@app.post("/ask", response_model=AnswerResponse)
def ask_question(body: QuestionRequest):
    system_prompt = f"""You are a study assistant. Answer the user's question using ONLY the content provided below.
If the answer is not in the content, say "I couldn't find that in the document."

CONTENT:
{body.document_text}"""

    answer = ask_gemini(system_prompt, body.question)
    return AnswerResponse(answer=answer)