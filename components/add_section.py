"""This File Serves New Item Section for Add Item Page."""
import streamlit as st
from utils.st_utils import header_section, add_new_project, add_new_task, add_new_assignee


def add_section(projects_from_query: list[str], assignees_from_query: list[str]) -> None:
    """Creates an interactive section in the Streamlit application for adding new items to the system.

    This function generates a UI section in a Streamlit app that allows users to add new projects,
    tasks, and assignees. The section is organized into tabs, each providing a form for inserting
    different types of items into the system. Users can add a new project, add a new task and assign it
    to a project and an assignee, add a new assignee to the system.

    Parameters:
    projects_from_query : list[str]
        A list of project names or objects obtained from a database query. This list is used to
        populate the dropdown menu in the "add task" tab where the user can select a project
        to which the new task will be assigned.
    assignees_from_query : list[str]
        A list of assignee names or objects obtained from a database query. This list is used to
        populate the dropdown menu in the "add task" tab where the user can select an assignee
        to assign to the new task.

    Returns: None: This function does not return any value. It directly modifies the Streamlit UI to provide
        interactive controls for adding new items to the system.
    """
    with st.container():
        st.write("---")
        left_column, right_column = st.columns([2, 1])
        with right_column:
            header_section(
                "Insert New Item",
                'Insert any new item - project, manager, task, assignee - to the system and provide \
                    the item details accordingly.'
            )
        with left_column:
            tab1, tab2, tab3 = st.tabs(["add project", "add task", "add assignee"])
            with tab1:
                add_new_project()
            with tab2:
                add_new_task(assignees_from_query, projects_from_query)
            with tab3:
                add_new_assignee()
