import streamlit as st
import pandas as pd
from pyecharts.charts import Bar,Pie
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts

def get_new_df():
    df = pd.read_excel('서울도서관 분야별 장서현황_2022.12.31.기준.xlsx')
    # 데이터 추출
    df = df.iloc[:,2:-2]
    new_df = pd.concat([df.iloc[0], df.iloc[2]], axis=1).T
    new_columns = new_df.iloc[0].astype(str).str.replace('\n','').tolist()
    new_df.columns = new_columns
    new_df.drop(0)
    new_df = new_df.reset_index(drop=True)

    return new_df, new_columns

def lib_status(new_df, new_columns):

    ## 막대그래프로 그리기
    # 리스트로 변경
    x = new_columns
    y = new_df.iloc[1].tolist()

    bar_chart = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("분류",y, label_opts=False)
        .set_global_opts(title_opts=opts.TitleOpts(title = "서울도서관 분야별 장서보유 현황",
                                                    subtitle= "마우스를 막대 위에 올리면 정확한 수치 확인이 가능합니다"))       
    )


    ## 파이차트로 그리기
    # 파이 그래프에 사용될 데이터셋
    z = [list(i) for i in zip(x,y)]

    pie_chart = (
        Pie()
        .add("",z, radius=["30%","80%"]) # radius : 내부 및 외부 링 크기
        .set_global_opts(title_opts=opts.TitleOpts(title="파이그래프",subtitle="마우스를 원 위에 올리면 정확한 수치 확인이 가능합니다"),
                         legend_opts=opts.LegendOpts(orient="vertical", pos_top="20%", pos_left="5%")) # 범례 조정
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b} : ({d}%)"))
    )


    st_pyecharts(bar_chart)
    st_pyecharts(pie_chart)

def lib_status_result():
    data, columns_name = get_new_df()
    lib_status(data, columns_name)

if __name__ == "__main__":
    lib_status_result()