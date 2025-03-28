def sidebar_choice(df, choice, columns_):
    import streamlit as st
    from kpis import show_employee_details
    from charts import (
        employees_across_departments,
        salary_distribution,
        salaries_by_department,
        age_distribution,
        ages_by_department
    )
    if choice == "Employees":
        st.markdown("## Employee information")
        show_employee_details(df, columns_),

    elif choice == "Employees per department":
        st.markdown("## Total number of employees per department")
        employees_across_departments(df)

    elif choice == "Salary distribution":
        st.markdown("## Salary distribution")
        salary_distribution(df)

    elif choice == "Salary per department":
        st.markdown("## Salary per department")
        salaries_by_department(df)

    elif choice == "Age distribution":
        st.markdown("## Age distribution")
        age_distribution(df)

    elif choice == "Age per department":
        st.markdown("## Age per department")
        ages_by_department(df)