"""Edit Items Section."""
import streamlit as st
from utils.st_utils import header_section, edit_project_budget, assign_task_assignee, change_task_status, set_salary


def edit_section(projects_from_query: list[str], tasks_from_query: list[str], assignees_from_query: list[str]) -> None:
    """Creates an interactive section in the Streamlit application for editing various project-related items.

    This function generates a section within a Streamlit app that allows users to update existing data in the system.
    The section is divided into multiple tabs, each focused on a specific type of update: editing project budgets,
    assigning task assignees, changing task statuses, and setting assignee salaries. Users can make selections
    from dropdown menus and input fields, and submit their changes to be saved to the database.

    Parameters:
    projects_from_query : list[str]
        A list of project names or identifiers obtained from a database query. This list is used to populate
        the dropdown menus where the user can select a project to edit its budget.

    tasks_from_query : list[str]
        A list of task names or identifiers obtained from a database query. This list is used to populate
        the dropdown menus where the user can select a task to assign an assignee or change its status.

    assignees_from_query : list[str]
        A list of assignee names or identifiers obtained from a database query. This list is used to populate
        the dropdown menus where the user can select an assignee to assign to a task or set their salary.

    Returns:
    None
        This function does not return any value. It directly modifies the Streamlit UI to allow users
        to edit project-related items and saves the changes to the database.
    """
    with (st.container()):
        st.write("---")
        left_column, right_column = st.columns([1, 3])
        with left_column:
            header_section(
                "Update Items",
                'Update existing data: assign manager, change project budget, assign task assignee, '
                'set salary, change task status and check the results in _Data Overview Page_.'
            )
        with right_column:
            tab1, tab2, tab3, tab4 = st.tabs(["edit budget", "assign assignee", "change status", "set salary"])
            with tab1:
                edit_project_budget(projects_from_query)
            with tab2:
                assign_task_assignee(tasks_from_query, assignees_from_query)
            with tab3:
                change_task_status(tasks_from_query)
            with tab4:
                set_salary(assignees_from_query)
