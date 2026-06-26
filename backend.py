from fastapi import FastAPI
import requests
from langchain_openrouter import ChatOpenRouter
from langchain_community.document_loaders import WebBaseLoader
from langchain_classic.chains.summarize import load_summarize_chain
from secret_key import openrouter_api_key1

app = FastAPI()

model = ChatOpenRouter(
    model="openrouter/free", 
    openrouter_api_key=openrouter_api_key1
)

@app.get("/")
def hello():
    return {"Message": "Hello! Welcome To The Web Summarizer backend infrastructure."}

@app.get("/summarize")
def summarize_page(url: str):
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        chain = load_summarize_chain(model, chain_type="stuff")
        response = chain.invoke({"input_documents": docs})
        return {"summary": response["output_text"]}
    except Exception as e:
        return {"summary": f"Failed to parse or summarize link: {str(e)}"}
