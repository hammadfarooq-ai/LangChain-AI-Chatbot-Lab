from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## environment variables call


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

## LangChain tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V1"] ="true"

## creating chatbot

prompt=ChatPromptTemplate.from_template(
    [
        ("system",),
        ("user", "Question: {question}")
    ]
)

# streamlit framework

st.title("Chatbot with LangChain and OpenAI")
input_text=st.text_input("Search the topic you want to ask about:")

# open AI LLM call
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()

# chain
chain=prompt | llm | output_parser

if input_text:

    st.write(chain.invoke({"question":input_text}))
