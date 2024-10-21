import streamlit as st
import transformers
import os

st.title("🎈 New app for class!")
st.write(
    "We've started building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Use a pipeline as a high-level helper
from transformers import pipeline
prompt = st.text_input("What is your prompt today?", "Damascus is")
number_of_tokens = st.text_input("What is the number of tokens to be used?", "20")

# Convert the number of tokens input to an integer
number_of_tokens = int(number_of_tokens)

### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')

### Use the pipeline
response = generator(prompt, max_length= number_of_tokens)

### Display
st.write(response.choices[0].message.content)   #cannot "print" in a webapp; have to code to show on UI

