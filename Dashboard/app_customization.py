import streamlit as st
import base64

def set_bg_from_pic(img):
    with open(img, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def set_log_in_screen(img):
    with open(img, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            backgrund-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

def page_style():
    st.markdown("""
        <style>
        h1 {
            color: #520500 !important;
        }
                
        h2 {
            color: #000000 !important;
        }
                
        h3 {
            color: #000000 !important;
        }

        .stMarkdown p{
            color: #000000;
        }
        </style>
        """, unsafe_allow_html=True)

def set_sidebar(df):
    sidebar_choices = st.sidebar.radio(
        "Choices",
        [
            "Employees",
            "Employees per department",
            "Salary distribution",
            "Salary per department",
            "Age distribution",
            "Age per department"
        ]
    )

    employee_columns = []
    if sidebar_choices == "Employees":
        columns_ = df.columns.tolist()
        with st.sidebar.expander("Filter information"):
            employee_columns = st.sidebar.multiselect(
                "Filter",
                options= columns_,
                default=columns_
            )

    return sidebar_choices, employee_columns

def show_message(message):
    st.markdown(f"""
        <div style='
            background-color: #d1e7dd;
            color: #0f5132;
            padding: 1rem;
            border-radius: 8px;
            font-weight: bold;
            border-left: 5px solid #072919;
            margin-top: 1rem;
        '>
            {message}
        </div>
     """, unsafe_allow_html=True)