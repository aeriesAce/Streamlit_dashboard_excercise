import streamlit as st

# calculate total employee count, average age and average salary
def basic_statistics(df):
    total_employee_count = len(df)
    average_age = round(df["Age"].mean(), 1)
    average_salary = round(df["Salary_SEK"].mean(), 1)

    return total_employee_count, average_age, average_salary

# show basic stats
def show_basic_statistics(df):
        labels = ("Employees:", "Average age:", "Average salary:")
        kpis = basic_statistics(df)
        cols = st.columns(3)

        for col, label, kpi in zip(cols, labels, kpis):
            with col:
                 st.markdown(
                f"""
                <div style='background-color: #07f5c5; padding: 3px; border-radius: 20px;'>
                    <h3 style='text-align:center; color:#291818; padding: 1px; margin-bottom: 0px;'>{label}</h3>
                    <h2 style='text-align:center; color:#291818; padding: 1px; margin-top: 2px'>{kpi}</h2>
                </div>
                """, unsafe_allow_html=True
            )

# employee details
def show_employee_details(df, columns_):
    if not columns_:
        st.info("Nothing to show")
        return 
    st.dataframe(df[columns_])