import streamlit as st


from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI()

# Streamlit UI
st.title("📚 PDF Query Assistant")
st.write("Ask a question and get answers from your PDF knowledge base.")

# Vector Embedding
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# Vector DB
vector_db = QdrantVectorStore.from_existing_collection(
    url = "http://localhost:6333",
    collection_name="clg_notes",
    embedding=embedding_model
)

# User input
query = st.text_input("Enter your question:", "")

if query:
    with st.spinner("Searching and generating response..."):

        # Vector similarity search in DB
        search_results = vector_db.similarity_search(
            query=query,
        )

        if not search_results:
            st.warning("No relevant context found in the PDF.")

        else :
            context = "\n\n\n".join([
                f"Page Content: {result.page_content}\n"
                f"Page Number: {result.metadata.get('page_label', 'N/A')}\n"
                f"File Location: {result.metadata.get('source', 'N/A')}"
                for result in search_results
            ])


            SYSTEM_PROMPT = f"""
                You are a helpfull AI Assistant who asnweres user query based on the available context
                retrieved from a PDF file along with page_contents and page number.

                You should only ans the user based on the following context and navigate the user
                to open the right page number to know more.

                Context:
                {context}
            """


            chat_completion = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": query},
                ]
            )

            # Display results
            st.subheader("🤖 Answer:")
            st.write(chat_completion.choices[0].message.content)