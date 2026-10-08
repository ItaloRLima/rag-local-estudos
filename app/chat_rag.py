import requests
import time

# URL da sua API local
URL = "http://localhost:8000/pergunta"

print("🤖 Chat do RAG Local Iniciado. (Digite 'sair' para encerrar)")

while True:
    # 1. Pega a pergunta do usuário no terminal
    pergunta_usuario = input("\nVocê: ")
    
    if pergunta_usuario.strip().lower() in ['sair', 'exit', 'quit']:
        print("Encerrando...")
        break

    # 2. Monta o corpo da requisição (Ajuste a chave "pergunta" conforme sua API exige)
    payload = {
        "question": pergunta_usuario
    }

    try:
        # 3. Faz o POST para a API
        start = time.time()
        response = requests.post(URL, json=payload)
        response.raise_for_status() # Dispara um erro se o status code não for 2xx
        
        # 4. Extrai a resposta (Ajuste a chave "resposta" conforme o retorno da sua API)
        dados = response.json()
        end = time.time()
        resposta_rag = dados.get("answer", "Chave 'resposta' não encontrada no JSON de retorno.")
        
        print(f"RAG: {resposta_rag.get('content')}\nTempo de resposta: {end - start:4f} segundos")
        
    except requests.exceptions.ConnectionError:
        print("\nErro: Não foi possível conectar. A API local (porta 8000) está rodando?")
    except requests.exceptions.RequestException as e:
        print(f"\nErro na requisição: {e}")