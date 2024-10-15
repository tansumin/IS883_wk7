import streamlit as st
from openai import OpenAI
import os

st.title("🎈 New app for class!")
st.write(
    "We've started building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
-----

prompt = st.text_input("What is your prompt today?", "Damascus is")


### Load your API Key
my_secret_key = st.secrets['MyOpenAIKey']
os.environ["OPENAI_API_KEY"] = my_secret_key


### Request the answer to the question "Damascus is a"
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": "Barcelona is a"}
  ],
  n=10,
  max_tokens=20
)


### Display
for i in range(10):
  st.write(response.choices[i].message.content)   #cannot "print" in a webapp; have to code to show on UI

