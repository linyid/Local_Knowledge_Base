# Local Knowledge Base
This project is a local knowledge base that uses LLM to process the documents, and a chatbot to answer user questions.

## 🧭 Phase 1: Core Setup

### 1. Create Project Folder Structure

Create the following folders and files:

Local_Knowledge_Base/
├── config.json              # Stores list of folders to scan
├── ingest.py                # Crawls directories, extracts text
├── embed.py                 # Embeds text, stores vectors
├── retrieve.py              # Semantic retrieval logic
├── chat.py                  # RAG-style Q&A
├── main.py                  # Orchestration
├── requirements.txt
└── utils.py                 # Shared tools (e.g. file type filtering)


## 🛠️ Phase 2: Develop Core Modules

### 2. Create config.json

### 3. Build ingest.py
Reads include_dirs from config.json

Recursively scans valid files

Extracts and returns raw text with metadata


### 4. Build embed.py

Takes text chunks

Embeds them using a model like all-MiniLM (or any SentenceTransformer)

Saves into FAISS or ChromaDB

### 5. Build retrieve.py
Given a question, converts it into an embedding

Retrieves similar chunks from the vector store

### 6. Build chat.py
Uses RAG-style prompt construction

Sends prompt + retrieved docs to a local LLM (via Ollama) or OpenAI API

Returns the response

## 🧪 Phase 3: Testing & Interaction

### 7. Run main.py
Loads documents from C:\\Etienne\\documents

Indexes them

Lets you query and chat

## 📈 Phase 4: Scaling Later
When ready to scale, can:

Add more directories to config.json

Add support for more file types (PPTX, HTML, images with OCR, etc.)

Add file change detection (e.g., watchdog)

Build a local web UI (Streamlit, Gradio)

