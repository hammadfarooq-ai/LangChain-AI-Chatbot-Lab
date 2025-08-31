# 🚀 LangChain RAG + Agents Chatbot Series

This repository contains a **series of projects** focused on building **advanced Q&A Chatbots** using **LangChain, RAG (Retrieval-Augmented Generation), and Agents**.  
It also demonstrates how to integrate both **OpenAI API** and **Ollama API** for flexibility between closed-source and open-source LLMs.

---

## 📂 Project Structure

```
LangChain-RAG-Agents-Chatbots-Series/
│
├── 01-Why-LangChain-And-Ecosystem/
├── 02-EndToEnd-QA-Chatbot-OpenAI-Ollama/
├── 03-Deployment-LangServe-FastAPI/
├── 04-Getting-Started-RAG-Pipeline/
├── 05-Advanced-RAG-QA-Chain-Retrievers/
├── 06-MultiSource-RAG-Chatbot-With-Agents/
└── README.md
```

---

## 📌 Projects Overview

### 1️⃣ Why LangChain and Understanding the Ecosystem
- What LangChain is and why it is powerful for LLM apps.
- Ecosystem overview: Chains, Retrievers, Tools, Agents, Memory.

---

### 2️⃣ End-to-End Q&A Chatbot (OpenAI + Ollama)
- Chatbot built using **LangChain**.
- Uses **OpenAI GPT models** (via API key) and **Ollama open-source models** (via local API).
- Switch between APIs for testing closed-source vs open-source LLMs.

---

### 3️⃣ Deployment as API (LangServe + FastAPI)
- Deploy LangChain apps with **LangServe**.
- Expose RAG + Agent-based chatbot through **FastAPI endpoints**.
- Ready for integration with web apps or external services.

---

### 4️⃣ Getting Started with RAG Pipeline
- Basic **Retrieval-Augmented Generation** with LangChain.
- Data ingestion → Vector database indexing → Retriever + LLM chain.
- Simple Q&A bot using context from documents.

---

### 5️⃣ Advanced RAG Q&A Chatbot (Chains + Retrievers)
- Enhanced retrievers for better context search.
- Custom **LangChain chains** to improve answers.
- Handles longer context, chunking, and embeddings.

---

### 6️⃣ Multi-Source RAG Chatbot with Agents
- Advanced **RAG with multiple data sources** (PDF, web, DB).
- **LangChain Agents** to decide dynamically:
  - Which retriever/tool to use.
  - When to call OpenAI or Ollama.
- Example: Bot can answer from PDF, fetch from a DB, or use LLM reasoning automatically.

---

## 🛠️ Tech Stack

- **LangChain** – Framework for LLM-powered apps
- **OpenAI API** – GPT models (requires `OPENAI_API_KEY`)
- **Ollama API** – Local open-source LLMs (requires `OLLAMA_API_KEY`)
- **LangServe** – For deployment
- **FastAPI** – API hosting
- **Vector Databases** – FAISS / Chroma for document retrieval

---

## 🔑 API Keys Setup

1. **OpenAI**
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```
2. **Ollama**
   ```bash
   export OLLAMA_API_KEY="your_ollama_api_key"
   ```
Make sure both are available in your environment before running.

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/LangChain-RAG-Agents-Chatbots-Series.git
   cd LangChain-RAG-Agents-Chatbots-Series
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run any project:
   ```bash
   cd 05-Advanced-RAG-QA-Chain-Retrievers
   python main.py
   ```

4. For API deployment:
   ```bash
   cd 03-Deployment-LangServe-FastAPI
   uvicorn main:app --reload
   ```

---

## 📚 Learning Goals

✅ Understand LangChain ecosystem  
✅ Use RAG pipelines with retrievers  
✅ Build Agent-powered chatbots  
✅ Integrate OpenAI + Ollama seamlessly  
✅ Deploy using LangServe + FastAPI  
✅ Work with multi-source data  

---

## 📧 Author

**Hammad Farooq**