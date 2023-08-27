from fastapi import APIRouter, Depends

from database import get_db
from domain.question import Question
from sqlalchemy.orm import Session
from DTO.question_request_dto import QuestionRequestDto
from DTO.question_response_dto import QuestionResponseDto

from database import Base, engine

router = APIRouter(
    prefix="/api/question",
)

@router.get("/", status_code=200)
def test():
    return {"detail": "success"}

@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list

@router.post("/create", response_model=QuestionResponseDto)
def create_question(question: QuestionRequestDto, db: Session = Depends(get_db)):
    new_question = Question(**question.dict())
    db.add(new_question)
    db.flush()
    db.commit()

