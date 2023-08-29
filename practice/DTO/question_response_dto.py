from pydantic import BaseModel
from datetime import datetime

class QuestionResponseDto(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime
