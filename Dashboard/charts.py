import duckdb
import streamlit as st
import plotly_express as px

# bar chart for employees across departments
def employees_across_departments(df):
    df = duckdb.query("""
                    SELECT Department, COUNT(*) AS Employees
                    FROM df
                    WHERE Department IS NOT NULL
                    GROUP BY Department
                    ORDER BY Employees
    """).df()

    fig = px.bar(  
        df,
        x="Department",
        y="Employees",
        orientation='v',
        labels={"Employees": "Number of Employees", "Department": "Department"},
        color="Department"
    )

    st.plotly_chart(fig, use_container_width=True)

# a histogram for salary distrubution
def salary_distribution(df):
        df = df[df["Salary_SEK"].notnull()]
        fig = px.histogram(
            df,
            x="Salary_SEK",
            nbins=30,
            labels={"Salary_SEK": "Salary (SEK)"},
            color_discrete_sequence=['#21c4a1']
        )
        fig.update_layout(
        yaxis_title="Employees")

        st.plotly_chart(fig, use_container_width=True)

# a box plot for salaries by department
def salaries_by_department(df):
        df = duckdb.query("""
                SELECT Department, Salary_SEK
                FROM df
                WHERE Department IS NOT NULL AND Salary_SEK IS NOT NULL
        """).df()
        fig = px.box(
        df,
        x="Department",
        y="Salary_SEK",
        points="all",
        labels={
            "Department": "Department",
            "Salary_SEK": "Salary (SEK)"
        },
        color="Department",
    )
 
        st.plotly_chart(fig, use_container_width=True)

# a histogram for age distribution
def age_distribution(df):
        df = df[df["Age"].notnull()]
        fig = px.histogram(
        df,
        x="Age",
        nbins=30,
        labels={"Age": "Age"},
        color_discrete_sequence=['#21c4a1']
        )
        fig.update_layout(
        yaxis_title="Employees")

        st.plotly_chart(fig, use_container_width=True)

# a box plot for ages by department
def ages_by_department(df):
            df = duckdb.query("""
                SELECT Department, Age
                FROM df
                WHERE Department IS NOT NULL AND Age IS NOT NULL
            """).df()
            fig = px.box(
                df,
                x="Department",
                y="Age",
                points="all",
                labels={
                    "Department": "Department",
                    "Age": "Age"
                },
                color="Department",
        )
            st.plotly_chart(fig, use_container_width=True)