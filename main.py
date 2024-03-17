import streamlit as st
from streamlit_option_menu import option_menu
from loan_total import loan_total_page
from state import lib_status_result
from test import prefer


st.set_page_config(layout="wide")

# 옵션에 따라 실행할 함수들을 매핑한 딕셔너리 생성
option_functions = {
    "MAIN" : lib_status_result,
    "장서현황": lib_status_result,
    "대출통계": prefer,
    "연령대별 대출통계": prefer,
    "아직못정함" : lib_status_result
}


# 옵션 메뉴 생성
with st.sidebar:
    selected_option = option_menu("MENU", ["MAIN","장서현황", "대출통계", "연령대별 대출통계", '아직못정함'], 
                                icons=['house', 'cloud-upload', "list-task", 'gear'],
                                default_index=0
                                #  with st.sidebar 지우고 orientation="horizontal" 이거하면 
    )


# 선택된 옵션에 맞는 함수 실행
if selected_option in option_functions:
    option_functions[selected_option]()


