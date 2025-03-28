import streamlit as st
from app_customization import show_message
def login_screen():
    
    with st.form("login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log in")

    if submitted:
        if username == "ceo" and password == "1234":
            st.session_state["logged_in"] = True
            show_message(f"Welcome back boss! Press enter again.")
        else:
            show_message("Wrong username or password")
    return False

def logout():
    st.session_state["logged_in"] = False
    st.rerun()
