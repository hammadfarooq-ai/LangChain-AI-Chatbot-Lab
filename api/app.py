from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import unicorn
import os
from langchain_community.llms import ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A Simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model=ChatOpenAI()

## ollama llm model
llm=ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
prompt2=ChatPromptTemplate.from_template("Write me a poem about {topic} for 5 years children.")

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)


add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)


if __name__=="__main__":
    unicorn.run(app, host="localhost", port=8000)