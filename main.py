import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from loan_total import loan_total_page
from state import lib_status_result
from test import prefer


def main():
    st.set_page_config(layout="wide")

    with st.sidebar:
        choose = option_menu("Menu",
            options= ["장서현황", "대출누적", "연령대별 대출누적", "인기대출도서"],
            icons = ["bi bi-list","bi bi-list","bi bi-list","bi bi-list"],
            default_index = 0
        )
    # st.title("서울도서관")

    if choose == "장서현황":
        lib_status_result()

    if choose == "대출누적":
        loan_total_page()

    if choose == "연령대별 대출누적":
        pass

    if choose == "인기대출도서":
        prefer()
        


if __name__ == "__main__":
    main()