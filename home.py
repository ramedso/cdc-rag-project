import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def generate_response(input_text):
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    st.info(model.invoke(input_text).content)

st.title("⚖️ Código de Defesa do Consumidor")

with st.form("my_form"):
    text = st.text_area(
        "Qual a sua dúvida?",
    )
    submitted = st.form_submit_button("Enviar")
    if submitted:
        generate_response(text)