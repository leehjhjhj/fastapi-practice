from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import controller.question_controller as question_controller
from database import Base, engine

app = FastAPI()

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_controller.router)