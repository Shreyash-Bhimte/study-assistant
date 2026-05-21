from pydantic import BaseModel

class UploadResponse(BaseModel):
    text: str
    char_count: int

class QuestionRequest(BaseModel):
    document_text: str
    question: str

class AnswerResponse(BaseModel):
    answer: str