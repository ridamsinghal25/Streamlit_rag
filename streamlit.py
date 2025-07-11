import streamlit as st

pages = {
    "Upload and chat": [
        st.Page("upload.py", title="Upload File"),
        st.Page("chat.py", title="Chat with File"),
    ]
}

pg = st.navigation(pages)
pg.run()