"""Delete Item Section."""
import streamlit as st
from utils.st_utils import header_section, delete_project, delete_manager, delete_task, delete_assignee


def delete_item_section(
        projects_from_query: list[str], managers_from_query: list[str], tasks_from_query: list[str],
        assignees_from_query: list[str]
) -> None:
    """Creates an interactive section in the Streamlit application for deleting various project-related items.

    This function generates a section within a Streamlit app that allows users to delete different types of items
    from the system, including projects, managers, tasks, and assignees. The section is divided into tabs, each
    focused on a specific type of item. Users can select an item from a dropdown menu and submit the form to delete
    the selected item from the database.

    Parameters:
    projects_from_query : list[str]
        A list of project names or identifiers obtained from a database query. This list is used to populate
        the dropdown menu where the user can select a project to delete.
    managers_from_query : list[str]
        A list of manager names or identifiers obtained from a database query. This list is used to populate
        the dropdown menu where the user can select a manager to delete.
    tasks_from_query : list[str]
        A list of task names or identifiers obtained from a database query. This list is used to populate
        the dropdown menu where the user can select a task to delete.
    assignees_from_query : list[str]
        A list of assignee names or identifiers obtained from a database query. This list is used to populate
        the dropdown menu where the user can select an assignee to delete.

    Returns:
    None
        This function does not return any value. It directly modifies the Streamlit UI and interacts with the
        database to delete the selected items upon form submission.
    """
    with (st.container()):
        st.write("---")
        left_column, right_column = st.columns([1, 3])
        with left_column:
            header_section("Delete selected Item", 'Get Ride of the unnecessary items.')
        with right_column:
            st.divider()
            tab1, tab2, tab3, tab4 = st.tabs(["delete project", "delete manager", "delete task", "delete assignee"])
            with tab1:
                delete_project(projects_from_query)
            with tab2:
                delete_manager(managers_from_query)
            with tab3:
                delete_task(tasks_from_query)
            with tab4:
                delete_assignee(assignees_from_query)
