from pydantic import BaseModel

class UploadResponse(BaseModel):
    text: str
    char_count: int