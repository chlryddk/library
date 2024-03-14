import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

loan_file_paths = ['서울도서관 도서분야별성별 대출 통계_2021.xlsx','서울도서관 도서분야별성별 대출 통계_2022.xlsx']

loan_total = []

@st.cache_data
def get_total_data():
    for file_path in loan_file_paths:
        df = pd.read_excel(file_path,header=1)

        loan_total.append(df) 

    for i in range(len(loan_total)):
        st.dataframe(loan_total[i])

    return loan_total

loan_total = get_total_data()

# 각 분야별 대출통계 데이터셋 시각화(파이차트)
def plot_pie_chart(data):
    for df in data:
        st.subheader(df.columns[0])
        fig, ax = plt.subplot()
        ax.pie(df.iloc[:,2:], label=df.columns[2:], autopct='%1.1f%%',startangle=90)
        ax.axis('equal1')
        #st.pyplot(fig)
        plt.show()

plot_pie_chart(loan_total)


def main_page():
    pass