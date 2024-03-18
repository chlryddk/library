import os
from dotenv import load_dotenv
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import streamlit as st

def ai():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(api_token=openai_api_key)

    df = pd.read_excel('서울도서관 도서분야별성별 대출 통계_2021.xlsx')
    new_columns = df.iloc[0].values
    df.columns = new_columns.astype(str)

    df.drop(index = 0, columns= df.columns[0], inplace=True)

    sums = []
    for i in range(7):
        row1 = df.iloc[i,1:]
        row2 = df.iloc[i+8, 1:]
        row_sum = row1 + row2
        sums.append(row_sum)

    result_df = pd.DataFrame(sums)

    result_df.insert(0,'연령대', df.iloc[:7,0].values)
    result_df.insert(0,'년도','2021')


    agent = SmartDataframe(result_df,config={"llm":llm})

    st.write(agent.chat('총류 연령대 순위를 알려줘'))
    # print(agent.chat("20대 연령대 안에서 높은 숫자의 이름대로 나열해줘"))
