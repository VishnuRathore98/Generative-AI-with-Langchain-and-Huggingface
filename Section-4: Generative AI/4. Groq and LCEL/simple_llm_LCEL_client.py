import requests
import streamlit as st
import json


def get_groq_response(input_text):
    dict_body = {
        "input": {
            "language": "French",
            "text": input_text
        },
        "config": {},
        "kwargs": {}

    }
    json_body = json.dumps(dict_body)
    response = requests.post("http://127.0.0.1:8000/chain/invoke", json_body)

    print(response.json())

    return response.json()


# Streamlit app
st.title("LLM Application Using LCEL")
input_text = st.text_input("Enter the text you want to convert to french")

if input_text:
    output = get_groq_response(input_text)

    st.write(output['output'])
