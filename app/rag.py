from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama

#Realiza a pergunta ao ollama
def ask_rag(question: str):
    embeddings = OllamaEmbeddings(
        model="bge-m3"
    )#Modelo que transforma dados em embeddings
    
    db = Chroma(
        persist_directory = "chroma",
        embedding_function = embeddings
    )
    #Realiza a busca por similaridade, o k determina o tanto de similaridades que eu quero
    docs = db.similarity_search(question, k=4)
    
    contexto = "\n\n".join([doc.page_content for doc in docs])
    
    #Define o prompt de contexto para a LLM
    prompt = f"""
        Use apenas o contexto abaixo para responder a pergunta.
        Se a resposta não estiver no contexto, diga que não encontrou a informação.
        
        Contexto:
        {contexto}
        
        Pergunta:
        {question}
    """
    
    llm = ChatOllama(model="llama3.1")
    
    return llm.invoke(prompt)
    