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
creative_temperature = st.text_input("How creative do you want your responses? (Pick a value between 0 and 1)", "0.9")
predictable_temperature = st.text_input("How predictable do you want your responses? (Pick a value between 0 and 1)", "0.2")

# Convert the number of tokens input to an integer
number_of_tokens = int(number_of_tokens)
creative_temperature = float(creative_temperature)
predictable_temperature = float(predictive_temperature)

### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')

### Use the pipeline
creative_response = generator(prompt, max_length= number_of_tokens, temperature= creative_temperature)
predictable_response = generator(prompt, max_length= number_of_tokens, temperature= predictable_temperature)

### Display
st.write("Creative Response:")
st.write(creative_response[0]['generated_text'])

st.write("Predictable Response:")
st.write(predictable_response[0]['generated_text'])
