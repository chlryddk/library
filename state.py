import streamlit as st
import pandas as pd
from pyecharts.charts import Bar
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
    # 막대그래프로 그리기
    x = new_columns
    y = new_df.iloc[1].tolist()

    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("갯수(권)",y)
        .set_global_opts(title_opts=opts.TitleOpts(title = "서울도서관 분야별 장서보유 현황",
                                                    subtitle= "마우스를 막대 위에 올려 정확한 수치를 확인해보세요!"))       
    )

    st_pyecharts(bar)

def lib_status_result():
    data, columns_name = get_new_df()
    lib_status(data, columns_name)

if __name__ == "__main__":
    lib_status_result()