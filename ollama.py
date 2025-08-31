#LANGCHAIN_API_KEY=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
#OPENAI_API_KEY=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
#LANGCHAIN_Project="Tutorial"


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()



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

# Ollama2 LLM call
llm=ollama.Ollama(model="llama2")
output_parser=StrOutputParser()

# chain
chain=prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))