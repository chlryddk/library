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

    # for i in range(len(loan_total)):
    #     st.dataframe(loan_total[i])

    return loan_total

loan_total = get_total_data()

# 각 분야별 대출통계 데이터셋 시각화
def total_chart(loan_total):
    plt.rcParams['font.family'] = 'Malgun Gothic'

    def total_2021(df):
        #
        df = df.iloc[:,3:-2]
        last_row = df.iloc[-1]
        sorted_values = last_row.sort_values(ascending=False)
        sorted_rank = sorted_values.to_frame().transpose()
        st.dataframe(sorted_rank)
        
        # 파이차트
        labels = sorted_rank.columns.tolist()
        sizes = sorted_rank.values.flatten().tolist()
        data_series = pd.Series(sizes, index = labels)

        fig,ax = plt.subplots(figsize=(3,3))
        ax.pie(data_series, labels = data_series.index, autopct = '%1.1f%%')
        ax.set_title('2021년도 대출누적 분포')

        return fig
        
    def total_2022(df):
        #
        df = df.iloc[:,3:-2]
        last_row = df.iloc[-1]
        sorted_values = last_row.sort_values(ascending=False)
        sorted_rank = sorted_values.to_frame().transpose()
        st.dataframe(sorted_rank)
        
        # 파이차트
        labels = sorted_rank.columns.tolist()
        sizes = sorted_rank.values.flatten().tolist()
        data_series = pd.Series(sizes, index = labels)

        fig,ax = plt.subplots(figsize=(3,3))
        ax.pie(data_series, labels = data_series.index, autopct = '%1.1f%%')
        ax.set_title('2022년도 대출누적 분포')
        return fig
    
    # streamlit에 파이차트 생성
    chart_2021 = total_2021(loan_total[0])
    chart_2022 = total_2022(loan_total[1])

    col1, col2 = st.columns(2)
    with col1:
         st.pyplot(chart_2021)
    with col2:
         st.pyplot(chart_2022)


total_chart(loan_total)

# streamlit 페이지 구성
def main_page():
    pass