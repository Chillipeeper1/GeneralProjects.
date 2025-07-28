import streamlit as st 
import pandas as pd
import requests

st.title('Sentiment Analysis API')
st.write("This is our first attempt at using Streamlit to create a web interface for our Translator API.")


API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-es"
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

data = st.text_input("Enter text to get a translation:")
data = {
    "inputs": data
}
if st.button('Translate'):
    st.write("Translating... Please wait.")
    # Make the API request

response = requests.post(API_URL, headers=headers, json=data)

st.write(f"Response from the API:{response.json()}") 




