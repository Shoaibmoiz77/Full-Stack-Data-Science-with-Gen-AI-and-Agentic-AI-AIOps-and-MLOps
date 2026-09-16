# this code integrates ollama with streamlit interface:
import streamlit as st 
from ollama import Client 

# ✅ Create client instance (VERY IMPORTANT)
client = Client(host="http://localhost:11434") 

st.set_page_config(
    page_title="Custom LLM model by Prakash Senapati - Ollama",
    layout="centered"
)

st.title("Mr. Shoaib Moiz - Ollama App")

prompt = st.text_area("Enter your prompt:", height=200)

if st.button("Generate Response"):
    if prompt.strip() == "deepseek-r1:1.5b":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat(
                model="deepseek-r1:1.5b",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.success("Response Generated!")
            st.write(response["message"]["content"])