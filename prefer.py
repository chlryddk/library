import pandas as pd
from pyecharts.charts import Bar
import streamlit as st
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts

def prefer():
    st.set_page_config(layout="wide")
    prefer_loan = pd.read_csv('서울도서관 인기대출 도서목록 100선 정보.csv',encoding='cp949')
    select_list = ["가장 인기 있는 도서 top10","장르별 대출 횟수 비교", "저자별 대출 횟수 비교"]

    st.title("하기싫다..")

    choose_select = st.selectbox("궁금한 점 선택", select_list, index=None)
    # 인기대출도서 top10 추출
    if choose_select == select_list[0]:
        st.dataframe(prefer_loan.iloc[:10])

    # 장르별 대출 횟수 비교
    elif choose_select == select_list[1]:
        prefer_loan['분류기호'].value_counts()
        category_mapping = {
            0:'총류',
            1:'철학',
            2:'종교',
            3:'사회과학',
            4:'자연과학',
            5:'기술과학',
            6:'예술',
            7:'언어',
            8:'문학',
            9:'역사'
        }
        prefer_loan['분류기호'] = prefer_loan['분류기호'].map(category_mapping)
        category_value = prefer_loan['분류기호'].value_counts().sort_index(ascending=False)
        
        # 그래프 그리기
        x = category_value.index.tolist()
        y = category_value.values.tolist()

        category_chart = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("장르별",y)
            .set_global_opts(title_opts = opts.TitleOpts(title = "장르별 대출횟수"))
        )

        st_pyecharts(category_chart)

    else:
        author = prefer_loan['저자'].value_counts().iloc[:10]
        st.dataframe(author)
        

if __name__ == "__main__":
    prefer()


