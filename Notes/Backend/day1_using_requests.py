import requests
# import streamlit as st
 
print("***RHYMING WORD GENERATOR***")
choice = input('Enter a word:')
endpoint = f"https://api.datamuse.com/words?sp={choice}"
 
response = requests.get(endpoint)
 
data = response.json()
 
if response.status_code == 200:
    for item in data:
        print(item.get('word'))


# OUTPUT:

# ***RHYMING WORD GENERATOR***
# Enter a word:monkey
# monkey
# money
# donkey
# honkey
# mankey
# conkey
# monkery
# monkly
# monkee
# monsey
# monke