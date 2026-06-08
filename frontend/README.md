# StudyAI — AI-Powered Study Assistant

A full-stack AI application that lets you upload a document and interact with it through streaming chat, summarisation, and flashcard generation.

**Live:** https://study-assistant-frontend-rho.vercel.app

---

## Features

- Upload PDF or plain text files as study material
- Ask questions about the document — AI answers only from the uploaded content
- Summarise the document into 6 structured bullet points
- Generate 5 flashcards with a CSS flip animation
- Streaming responses — AI output renders word by word
- Token and character count of uploaded content
- Session clear — wipes document and chat history
- Loading states and auto-dismissing error handling

---

## Architecture
```
Browser (React + Vite)  ←→  FastAPI (Python)  ←→  Gemini API
Vercel                    Render               Google
```
The browser never calls Gemini directly. Every request goes through the FastAPI backend, which holds the API key, builds the prompt, and streams the response back to the frontend.

---

## Tech Stack

**Frontend**
- React 18 + Vite
- CSS Modules
- `useReducer` for session state
- `useRef` for auto-scroll
- `ReadableStream` for streaming

**Backend**
- Python 3.12 + FastAPI
- PyMuPDF (`fitz`) for PDF parsing
- `requests` for raw Gemini API calls
- `StreamingResponse` for SSE streaming
- `python-dotenv` for environment variables
- Pydantic for request/response validation

**AI**
- Google Gemini 2.5 Flash
- Raw HTTP calls — no SDK or framework
- Structured prompt engineering for flashcard JSON output
- Streaming via `streamGenerateContent` with `alt=sse`

**Deployment**
- Frontend → Vercel
- Backend → Render

---

## Project Structure
```
study-assistant/
├── backend/
│   ├── main.py            # FastAPI app, all routes
│   ├── gemini_client.py   # Gemini API functions
│   ├── file_parser.py     # PDF and text extraction
│   ├── models.py          # Pydantic schemas
│   └── requirements.txt
└── frontend/
└── src/
├── components/
│   ├── FileUpload.jsx
│   ├── ChatWindow.jsx
│   ├── MessageBubble.jsx
│   ├── FlashCards.jsx
│   └── Toolbar.jsx
├── hooks/
│   └── useStudySession.js
├── lib/
│   └── api.js
└── App.jsx
```
---

## Local Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- Gemini API key — free at [aistudio.google.com](https://aistudio.google.com)

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
```

Create `backend/.env`:
GEMINI_API_KEY=your_key_here

Start the server:
```bash
uvicorn main:app --reload
```

Backend runs at `http://localhost:8000`
API docs at `http://localhost:8000/docs`

### Frontend

```bash
cd frontend
npm install
```

Create `frontend/.env.local`:
VITE_API_URL=http://localhost:8000

Start the dev server:
```bash
npm run dev
```

Frontend runs at `http://localhost:5173`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/upload` | Upload PDF or .txt, returns extracted text |
| POST | `/ask-stream` | Streaming chat response |
| POST | `/summarise` | Streaming bullet point summary |
| POST | `/flashcards` | Generate 5 Q&A flashcards as JSON |

---

## Deployment

**Backend (Render)**
- New Web Service → connect GitHub repo
- Root directory: `backend`
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Environment variable: `GEMINI_API_KEY`

**Frontend (Vercel)**
- New Project → connect GitHub repo
- Root directory: `frontend`
- Environment variable: `VITE_API_URL` → your Render URL

---

## Key Implementation Notes

- **No LangChain** — raw Gemini API calls only, every part of the pipeline is explicit
- **No database** — conversation history held in React state, stateless backend
- **In-memory PDF parsing** — PyMuPDF reads bytes directly, no disk I/O
- **Structured output** — flashcard prompt constrains Gemini to return raw JSON; defensive parsing strips markdown fences before `json.loads()`
- **Streaming** — backend uses `streamGenerateContent` with SSE, frontend reads `ReadableStream` chunk by chunk

---

## Author

Shreyash Bhimte — [github.com/Shreyash-Bhimte](https://github.com/Shreyash-Bhimte) · [LinkedIn](https://www.linkedin.com/in/shreyash-bhimte)
