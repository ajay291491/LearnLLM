import streamlit as st

st.header("LLMLearning Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("upload a PDF file and start asking questions", type="pdf")


