import os
from dotenv import load_dotenv
import pandas as pd
from pandasai import PandasAI
# from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import streamlit as st

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(api_token=openai_api_key)
pandas_ai = PandasAI(llm)

st.title("Pandas AI")

uploaded_file = st.file_uploader("upload your CSV file", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    prompt = st.text_area("Enter your prompt: ")

    if st.button("generate"):
        if prompt:
            st.write("pandasai is generate an answer, please wait")
            st.write(pandas_ai.run(df, prompt=prompt))
        else:
            st.warning("please enter a prompt")