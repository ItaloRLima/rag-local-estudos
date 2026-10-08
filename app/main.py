#Criar uma API para subir o teste
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.rag import ask_rag

app = FastAPI()

#Classe para validar a estrutura da pergunta
class Question(BaseModel):
    question: str


@app.post("/pergunta")
def ask_question(data: Question):
    # Validação de regra de negócio
    if len(data.question.strip()) < 5:
        raise HTTPException(
            status_code=400, # 400 significa "Bad Request" (Requisição mal formulada)
            detail="A pergunta é muito curta. Por favor, seja mais específico."
        )
    try:
        # Tenta executar o RAG normalmente
        answer = ask_rag(data.question)
        return {"answer": answer}
        
    except Exception as e:
        # Se der qualquer erro no código acima, ele cai aqui.
        # O HTTPException exige dois parâmetros principais:
        # 1. status_code: O código do erro HTTP (500 significa Erro Interno do Servidor)
        # 2. detail: A mensagem que explica o erro para quem chamou a API
        
        raise HTTPException(
            status_code=500, 
            detail=f"Falha ao processar a requisição no RAG. Erro original: {str(e)}"
        )

#Para subir a API utilizar o uvicorn app.main:app --reload