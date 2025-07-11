from dotenv import load_dotenv
import streamlit as st
import tempfile
import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

# Load environment variables
load_dotenv()

st.title("Upload File")
st.write("Upload a PDF, choose an embedding model, and index it to Qdrant.")

# Upload file
uploaded_file = st.file_uploader("Upload your pdf", type=["pdf", "txt"])

file_type = None 

if uploaded_file is not None:
    file_type = uploaded_file.type

st.info(f"File type is {file_type}")

suffix = ".pdf" if file_type == "application/pdf" else ".txt"

if uploaded_file and st.button("Start Processing"):
   with st.spinner("Processing PDF and indexing to Qdrant..."):
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_pdf_path = Path(tmp_file.name)

    loader = None
    if file_type == 'application/pdf':
        # Load the pdf file
        loader = PyPDFLoader(tmp_pdf_path)
    
    elif file_type == 'text/plain':
        # Load the text file
        loader = TextLoader(tmp_pdf_path)

    # Read PDF File
    docs = loader.load() 

    # Chunking
    text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1000,
    chunk_overlap=300,
    )

    # Split the document into chunks
    split_docs = text_splitter.split_documents(documents=docs)
    st.success(f"Split into {len(split_docs)} chunks.")

    # Vector Embedding Open AI
    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-large"
    )

    # Using [embedding_model] create embeddings of [split_docs] and store in DB
    vector_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    url="http://localhost:6333",
    collection_name="clg_notes",
    embedding=embedding_model
    )

    st.info("Indexed to Qdrant")

    os.remove(tmp_pdf_path)