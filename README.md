# Demo RAG Local (Retrieval-Augmented Generation)

Este repositório contém uma aplicação educacional de RAG (Retrieval-Augmented Generation) rodando 100% localmente. O objetivo é demonstrar o fluxo completo de uma arquitetura de RAG, desde a ingestão de documentos até a geração de respostas usando LLMs de código aberto, sem depender de APIs pagas (como OpenAI).

Este projeto foi inspirado e desenvolvido com base nos ensinamentos e na estrutura do repositório original [giuliana-bezerra/demo-rag-local](https://github.com/giuliana-bezerra/demo-rag-local). Foi construído utilizando LangChain, ChromaDB, FastAPI e Ollama.

## Para que serve este projeto?

Este projeto serve como uma base de estudos para entender como um sistema de inteligência artificial pode responder a perguntas baseadas em documentos corporativos ou pessoais. Ele executa as seguintes tarefas:

1. Lê documentos (PDF, TXT, MD) de uma pasta local.
2. Quebra o texto em pedaços menores (chunks).
3. Converte os textos em vetores (embeddings) e salva em um banco de dados vetorial.
4. Expõe uma API web para receber perguntas.
5. Busca os contextos mais relevantes e usa um LLM local para formular a resposta final.

## Pré-requisitos e Instalação

### 1. Instalar o Ollama (Modelos Locais)

Como o processamento é 100% local, você precisa ter o [Ollama](https://ollama.com/download) instalado rodando em sua máquina.
Após a instalação, abra seu terminal e baixe os modelos que serão utilizados:

```sh
# Modelo para transformar texto em vetores (Embeddings)
ollama pull nomic-embed-text

# Modelo de Linguagem para gerar as respostas (LLM)
ollama pull mistral 
# (Nota: Pode ser substituído por llama3.1, qwen2.5, bge-m3, etc)
```

### 2. Configurar o Ambiente Python

Recomenda-se o uso do Python 3.10 ou superior. Clone este repositório e crie um ambiente virtual:

```sh
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate
```

### 3. Instalar Dependências

Com o ambiente ativado, instale as bibliotecas necessárias:

```sh
pip install -r "requirements.txt"
```


## Como Executar (Ordem de Execução)

Siga exatamente a ordem abaixo para que a aplicação funcione corretamente.

### Passo 1: Alimentar a base de dados

Coloque seus arquivos de texto (.txt, .md) ou .pdf dentro da pasta `data/docs/`.

### Passo 2: Rodar a Ingestão

No terminal, execute o script responsável por ler os arquivos, gerar os vetores e salvar no banco de dados Chroma:

```sh
python app/ingest.py
```

*Aguarde a mensagem indicando a conclusão e a quantidade de chunks gerados.*

### Passo 3: Iniciar a API

Com o banco populado, suba o servidor da API usando o Uvicorn:

```sh
uvicorn app.main:app --reload
```

*A API estará rodando em http://localhost:8000.*

### Passo 4: Interagir com o RAG

Abra outro terminal (mantenha a API rodando no primeiro) e execute o script de chat para fazer perguntas aos seus documentos:

```sh
python app/chat_rag.py
```

Agora basta digitar suas perguntas no console!

## Limitações Atuais (Oportunidades de Melhoria)

Por ser um projeto de introdução e estudos, ele possui algumas limitações arquiteturais que podem servir como próximos passos para aprendizado:

* Sem Memória de Conversação: O modelo não lembra de perguntas anteriores (Single-Turn). Cada pergunta é tratada de forma isolada.
* Busca Simples: Utiliza apenas busca semântica básica. Não implementa técnicas avançadas como Re-ranking ou MMR (Maximal Marginal Relevance).
* Chunking Básico: O corte dos textos é feito apenas por quantidade de caracteres (800), o que pode cortar ideias no meio.
* Ingestão Completa: Rodar o script de ingestão adiciona todos os arquivos novamente ao banco de dados (não suporta ingestão incremental baseada em arquivos novos/modificados).
* Desempenho de Inicialização: A cada requisição, os modelos e o banco são reinstanciados na função do LangChain, o que adiciona alguns segundos de latência.
