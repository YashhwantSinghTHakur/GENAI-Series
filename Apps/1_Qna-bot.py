from dotenv import load_dotenv
load_dotenv()
import os

from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash",
    temperature=0)

st.title("👦 Buddy - AI QNA BOT")
st.markdown("my QnA Bot with langchain and Google Gemini !")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]

    content = message["content"]
    st.chat_message(role).markdown (content)


query = st.chat_input("Ask anything ?")
if query:
    st.session_state.messages.append({"role":"user" , "content":query})
    st.chat_message("User").markdown(query)
    res = llm.invoke(query)
    st.chat_message("AI").markdown(res.content[0]["text"])
    st.session_state.messages.append({"role": "AI" , "content": query})








