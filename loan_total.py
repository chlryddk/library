import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


@st.cache_data
# 공공데이터 데이터프레임으로 변환
def get_total_data():
    loan_file_paths = ['서울도서관 도서분야별성별 대출 통계_2021.xlsx','서울도서관 도서분야별성별 대출 통계_2022.xlsx']
    loan_total = []

    for file_path in loan_file_paths:
        df = pd.read_excel(file_path,header=1)
        loan_total.append(df) 

    return loan_total


# 각 분야별 대출통계 데이터셋 시각화
def total_chart(loan_total):
    plt.rcParams['font.family'] = 'Malgun Gothic'

    def total_2021(df):
        # 데이터 추출
        df = df.iloc[:,3:-2]
        last_row = df.iloc[-1]
        sorted_values = last_row.sort_values(ascending=False)
        sorted_rank_2021 = sorted_values.to_frame().transpose()
        dataframe_2021 = sorted_rank_2021
        
        # 파이차트
        labels = sorted_rank_2021.columns.tolist()
        sizes = sorted_rank_2021.values.flatten().tolist()
        data_series = pd.Series(sizes, index = labels)

        fig,ax = plt.subplots(figsize=(3,3))
        # ax.pie(sizes, labels = labels, autopct = '%1.1f%%')
        ax.pie(data_series, labels = data_series.index, autopct = '%1.1f%%')
        chart_2021 = fig

        return dataframe_2021, chart_2021
    
        
    def total_2022(df):
        # 데이터 추출
        df = df.iloc[:,3:-2]
        last_row = df.iloc[-1]
        sorted_values = last_row.sort_values(ascending=False)
        sorted_rank_2022 = sorted_values.to_frame().transpose()
        dataframe_2021 = sorted_rank_2022
        
        # 파이차트
        labels = sorted_rank_2022.columns.tolist()
        sizes = sorted_rank_2022.values.flatten().tolist()
        data_series = pd.Series(sizes, index = labels)

        fig,ax = plt.subplots(figsize=(3,3))
        ax.pie(data_series, labels = data_series.index, autopct = '%1.1f%%')
        chart_2022 = fig

        return dataframe_2021, chart_2022
    

    data_2021, chart_2021 = total_2021(loan_total[0])
    data_2022, chart_2022 = total_2022(loan_total[1])


    # 차트와 데이터 선택해서 볼 수 있음
    tab1, tab2, tab3, tab4= st.tabs(["2021년 chart", "2021년 data","2022년 chart", "2022년 data"])
    with tab1:
        st.subheader("2021년 대출누적 분포도")
        st.pyplot(chart_2021)

    with tab2:
        st.subheader("2021년 대출분포 표")
        st.dataframe(data_2021)

    with tab3:
        st.subheader("2022년 대출누적 분포도")
        st.pyplot(chart_2022)
    
    with tab4:
        st.subheader("2022년 대출분포 표")
        st.dataframe(data_2022)


def loan_total_page():
    loan_total = get_total_data()
    total_chart(loan_total)

    
if __name__ == "__main__":
    loan_total_page()