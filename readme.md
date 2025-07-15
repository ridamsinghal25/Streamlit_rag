# 📚 RAG PDF Assistant with Streamlit

An interactive **Retrieval-Augmented Generation (RAG)** application built with **Streamlit**. This app lets you upload PDF or text files, indexes their content into **Qdrant** using **LangChain**, and allows you to query them via **OpenAI GPT models**.

Perfect for quickly building a knowledge base from your documents and asking natural language questions to retrieve context-aware answers.

---

## ✨ Features

✅ Upload PDF or TXT files
✅ Automatic chunking and indexing with LangChain
✅ Store and retrieve vector embeddings using Qdrant
✅ Query your documents with GPT-4 (or GPT-3.5) using OpenAI API
✅ Simple and intuitive Streamlit interface
✅ Background job processing with Redis RQ (runs in devcontainer)

---

## 📦 Tech Stack

* [Streamlit](https://streamlit.io/) – Web UI
* [LangChain](https://www.langchain.com/) – Document loading, splitting, retrieval
* [Qdrant](https://qdrant.tech/) – Vector database for embeddings
* [OpenAI](https://platform.openai.com/docs) – GPT models for answering questions
* [Redis + RQ](https://python-rq.org/) – Background job queue (runs in Docker devcontainer)
* [dotenv](https://pypi.org/project/python-dotenv/) – Manage environment variables

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/rag-pdf-assistant.git
cd streamlit_rag_queue
```

---

### 2️⃣ Set Up Python Environment

We recommend using a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the root directory with your OpenAI API key:

```bash
OPENAI_API_KEY=your-openai-api-key
```

---

## 🐳 Running Qdrant & Redis RQ (Docker)

This app requires both **Qdrant** (vector database) and **Redis RQ** (job queue) to be running.

We recommend using the provided **Docker Devcontainer setup** for this.

---

### 🏗️ Option 1: Using Devcontainer (Recommended)

The included **devcontainer** is preconfigured with:

* ✅ Qdrant
* ✅ Redis + RQ Worker
* ✅ All dependencies

To launch:

1. Open the folder in **VS Code**.
2. Install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
3. Reopen in container.

This will start:

* Qdrant at `http://vector-db:6333`
* Redis at `valkey:6379` (used by RQ for background processing)

> ⚠️ **Note:** Redis RQ works only inside the devcontainer setup. If running locally, you need to install and start Redis separately.

---

### 🏃 Option 2: Run Qdrant directly with Docker

If you only want Qdrant (without Redis):

```bash
docker run -p 6333:6333 qdrant/qdrant
```

---

### 📦 Option 3: Use Docker Compose

We provide a `docker-compose.yml`:

```bash
docker compose up -d
```

This will:

* Start Qdrant
* Start Redis
* Spin up RQ worker

Stop services later with:

```bash
docker compose down
```

---

## 📝 How It Works

### 📤 Step 1: Upload and Index Documents

* Upload a PDF or TXT file via the Streamlit UI.
* The app uses **LangChain** to:

  * Load and split your document into chunks
  * Generate embeddings with OpenAI’s `text-embedding-3-large` model
  * Store them in Qdrant

---

### 🔎 Step 2: Ask Questions

* Enter any question about your document.
* The app:

  * Retrieves relevant chunks from Qdrant
  * Feeds them as context to GPT-4
  * Returns concise answers with references to page numbers and file locations

---

### ⚡ Background Processing with Redis RQ

* Queries are enqueued as jobs using **Redis RQ**.
* Workers pick up and process queries asynchronously.
* Works **only in Docker devcontainer**, where Redis and RQ are preconfigured.

---

## 🖥️ Running the App Locally

Make sure **Qdrant** is running at `http://localhost:6333`.
Start the Streamlit app:

```bash
streamlit run streamlit.py
```

The app will open in your browser at [http://localhost:8501](http://localhost:8501).

---

## 🔥 API Endpoints

| Endpoint           | Method | Description                     |
| ------------------ | ------ | ------------------------------- |
| `/`                | GET    | Health check                    |
| `/chat`            | POST   | Submit query (enqueued in RQ)   |
| `/result/{job_id}` | GET    | Fetch result for a given job ID |

---


## 📖 Notes

* **Redis RQ dependency:** Background jobs require Redis. This is preinstalled in the Docker devcontainer.
* If running locally without Docker, you must install Redis and start an RQ worker manually:

```bash
redis-server
rq worker
```

---

## 🛠️ Tech Versions

| Tool      | Version      |
| --------- | ------------ |
| Python    | 3.10+        |
| Qdrant    | Latest       |
| Redis     | 7.x (valkey) |
| Streamlit | >=1.22       |
| LangChain | >=0.1        |

---

