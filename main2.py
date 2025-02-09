import streamlit as st
from mira_sdk import MiraClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MIRA_API_KEY")
client = MiraClient(config={"API_KEY": api_key})

st.title("Personal Finance Assistant")

user_query = st.text_input("Ask about personal finance:", "")

if st.button("Submit"):
    if user_query:
        input_data = {"user_query": user_query}
        response = client.flow.execute("akshit/FinanceAdvisor", input_data)
        st.write("Advisor:", response.get("result", "No response from Mira AI"))
    else:
        st.warning("Please enter a query.")
