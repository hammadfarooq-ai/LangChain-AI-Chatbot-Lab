import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_response(input_text):
    response=requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {'topic': input_text}}
    )
    return response.json()['output']['content']


def get_ollama_response(input_text):
    response=requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input": {'topic': input_text}}
    )
    return response.json()['output']




## streamlit framework

st.title("Chatbot with LangChain and OpenAI")
input_text=st.text_input("Search the topic you want to ask about:")
input_text1=st.text_input("Search the topic you want to ask about:")

if input_text:
    st.write(get_openai_response(input_text))
    
    
if input_text1:
    st.write(get_ollama_response(input_text1))