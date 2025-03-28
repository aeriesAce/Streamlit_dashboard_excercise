import streamlit as st
from read_data import read_file
from app_customization import set_bg_from_pic, set_log_in_screen, page_style, set_sidebar
from sidebar_choices import sidebar_choice
from kpis import show_basic_statistics
from login_ import login_screen, logout

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    page_style()
    st.title("Welcome")
    set_log_in_screen('./Media/forest.png')
    login_screen()
    st.stop()
else:
    df = read_file()
    page_style()
    st.markdown("# Excecutive dashboard")
    st.markdown("## For the cool kids")
    set_bg_from_pic('./Media/pic.png.webp')
    show_basic_statistics(df)
    choice, columns_ = set_sidebar(df)
    sidebar_choice(df, choice, columns_)
    st.sidebar.button("Log out", on_click=logout, key="logout_button") 