# 📚 RAG PDF Assistant with Streamlit

An interactive **Retrieval-Augmented Generation (RAG)** application built with **Streamlit**. It lets you upload PDF or text files, indexes their content into **Qdrant** using **LangChain**, and then allows you to query them using **OpenAI GPT models**.

This app is perfect for quickly building a knowledge base from your documents and asking natural language questions to retrieve answers with context.

---

## ✨ Features

✅ Upload PDF or TXT files  
✅ Automatic chunking and indexing with LangChain  
✅ Store and retrieve vector embeddings using Qdrant  
✅ Query your documents with GPT-4 (or GPT-3.5) using OpenAI API  
✅ Simple and intuitive Streamlit interface

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/) – For building the web UI
- [LangChain](https://www.langchain.com/) – Document loading, splitting, and retrieval
- [Qdrant](https://qdrant.tech/) – Vector database for storing embeddings
- [OpenAI](https://platform.openai.com/docs) – GPT models for answering questions
- [dotenv](https://pypi.org/project/python-dotenv/) – Manage environment variables

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/rag-pdf-assistant.git

cd streamlit_rag
```

### 2️⃣ Set Up Python Environment

We recommend using a virtual environment:

```bash
virtualenv .venv

source venv/bin/activate # On Windows use venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a .env file in the root directory with your OpenAI API key:

```bash
OPENAI_API_KEY=your-openai-api-key
```

---

## 🐳 Running Qdrant with Docker

This app requires **Qdrant** as the vector database. You can run it in two ways:

---

### Option 1: Run Qdrant directly with Docker (if installed locally)

```bash
docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
```

### Option 2: Use Docker Compose (Recommended)

We provide a docker-compose.yml file. To pull the Qdrant image and run it:

```bash
docker compose up -d
```

This will:

- ✅ Download the Qdrant image
- ✅ Start it as a background service

To stop it later:

```bash
docker compose down
```

---

## 📝 How It Works

### 📤 Step 1: Upload and Index

- Upload a PDF or TXT file.
- The app uses **LangChain** to:
  - Load your document
  - Split it into chunks
  - Generate vector embeddings with OpenAI’s `text-embedding-3-large` model
  - Store them in **Qdrant** (running locally or remotely)

### 🔎 Step 2: Query Your Knowledge Base

- Ask any question about the uploaded document.
- The app:
  - Searches for relevant chunks in Qdrant
  - Provides context to GPT-4
  - Returns a concise answer with references to page numbers.

---

## 🖥️ Running the App

Make sure **Qdrant** is running locally at `http://localhost:6333` (or change the URL in the code if using a remote instance). You can start Qdrant using Docker:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

Then, run the Streamlit app:

```bash
streamlit run streamlit.py
```

The app will open in your browser at http://localhost:8501.
