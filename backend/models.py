from pydantic import BaseModel

class UploadResponse(BaseModel):
    text: str
    char_count: int

class QuestionRequest(BaseModel):
    document_text: str
    question: str

class AnswerResponse(BaseModel):
    answer: str

class StreamRequest(BaseModel):
    document_text: str
    question: str

class SummaryRequest(BaseModel):
    document_text: str

class FlashcardsRequest(BaseModel):
    document_text: str

class Flashcard(BaseModel):
    question: str
    answer: str

class FlashcardsResponse(BaseModel):
    cards: list[Flashcard]