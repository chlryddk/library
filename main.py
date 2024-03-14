import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

loan_file_paths = ['서울도서관 도서분야별성별 대출 통계_2021.xlsx','서울도서관 도서분야별성별 대출 통계_2022.xlsx']

loan_total = []

@st.cache_data
# 공공데이터 데이터프레임으로 변환
def get_total_data():
    for file_path in loan_file_paths:
        df = pd.read_excel(file_path,header=1)

        loan_total.append(df) 

    for i in range(len(loan_total)):
        st.dataframe(loan_total[i])

    return loan_total

loan_total = get_total_data()

# 각 분야별 대출통계 데이터셋 시각화(파이차트)
def total_chart(loan_total):
    def total_2021(df):
        # 분야 별 책 합계 중 상위 5개 추출
        df = df.iloc[:,3:-1]
        last_row = df.iloc[-1]
        sorted_values = last_row.sort_values(ascending=False)
        top_5_largest_value = sorted_values[:5]
        # sorted_values = last_row.drop(last_row.columns[0,1,2],axis=1)
        st.dataframe(top_5_largest_value)
        # sorted_values = last_row.sort_values(ascending=False)
        # top_5_largest_values = sorted_values[:5]
        # st.dataframe(top_5_largest_values)
        
        return top_5_largest_value

        

    def total_2022(df):
        pass



    total_2021(loan_total[0])
    total_2022(loan_total[1])

total_chart(loan_total)


def main_page():
    pass