from langchain.chains import create_retrieval_chain
import re
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
# Load Data--> Docs-->Divide our Docuemnts into chunks dcouments-->text-->vectors-->Vector Embeddings--->Vector Store DB
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document

st.set_page_config(page_title="WebChat: Chat with webpage", page_icon="🦜")

webpage = st.sidebar.text_input(
    "Website url:", placeholder="eg. https://example.com")

if not webpage:
    st.info("Please enter webpage url")
else:
    loader = WebBaseLoader(webpage)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(docs)

    embeddings = (
        OllamaEmbeddings(model="mxbai-embed-large")  # by default it ues llama2
    )

    vectorstoredb = FAISS.from_documents(documents, embeddings)

    # Prompt Template
    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful agent who answers the questions asked by the user based on the provided context:
        <context>{context}</context>
        """
    )

    llm = Ollama(model="deepseek-r1:1.5b")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    # streamlit framework
    st.title("Deepseek-r1:1.5b Website Query Model")
    input_text = st.text_input(
        "What questions do you have, about the website?")

    retriever = vectorstoredb.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, chain)

    if input_text:
        response = retrieval_chain.invoke({"input": input_text})
        answer = response['answer']
        model_answer = re.sub(r"<think>.*?</think>\n*", "",
                              answer, flags=re.DOTALL).strip()
        st.write(model_answer)
