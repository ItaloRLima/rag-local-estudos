#Criar uma API para subir o teste
from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import ask_rag

app = FastAPI()

#Classe para validar a estrutura da pergunta
class Question(BaseModel):
    question: str


@app.post("/pergunta")
def ask_question(data: Question):
    answer = ask_rag(data.question)
    return{"answer": answer}

#Para subir a API utilizar o uvicorn app.main:app --reload