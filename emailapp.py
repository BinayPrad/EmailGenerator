import streamlit as st
import openai
question=st.text_area("Input the Email context Here")
button=st.button("Generate")
def response1(ques):
    openai.api_type = "azure"
openai.api_base = "https://hack2023d1.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = st.secrets("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="hack2023d1gpt35",
  prompt="Write a product launch email for new AI-powered headphones that are priced at $79.99 and available at Best Buy, Target and Amazon.com. The target audience is tech-savvy music lovers and the tone is friendly and exciting.\n\n1. What should be the subject line of the email?  \n2. What should be the body of the email?",
  temperature=1,
  max_tokens=350,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

if question and button:
        answer=response1(question)
        st.code(answer)
