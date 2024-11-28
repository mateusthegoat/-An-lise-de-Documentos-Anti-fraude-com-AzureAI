import streamlit as st

def configure_interface():
    st.title("Upload de arquivo Dio - desafio -1 - python - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg","jpeg"])