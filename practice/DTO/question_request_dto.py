from pydantic import BaseModel
from datetime import datetime

class QuestionRequestDto(BaseModel):
    subject: str
    content: str
    create_date: datetime = None
