from fastapi import APIRouter, Depends, HTTPException

from database import get_db
from domain.question import Question
from sqlalchemy.orm import Session
from DTO.question_request_dto import QuestionRequestDto
from DTO.question_response_dto import QuestionResponseDto
from database import Base, engine

router = APIRouter(
    prefix="/question",
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
    try:
        db.commit()
        return new_question
    except Exception as e:
       raise HTTPException(status_code=400, detail=f"잘못된 접근입니다: {e}")