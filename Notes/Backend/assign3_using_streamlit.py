import requests
import streamlit as st
 
st.title("***RHYMING WORD GENERATOR***")
choice= st.text_input('Enter a word:')

# choice = input('Enter a word:')
endpoint = f"https://api.datamuse.com/words?sp={choice}"
 
response = requests.get(endpoint)
 
data = response.json()
is_clicked= st.button("Generate", type = "primary")

if is_clicked:
    if response.status_code == 200:
        for item in data:
            st.write(item.get('word'))



