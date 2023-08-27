from sqlalchemy import Column, Integer, BigInteger, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers") # 객체 참조용. backref를 통해서 역참조도 가능하다.