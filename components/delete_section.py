import streamlit as st

from src.base import db_engine
from src.models import Assignee, Project, Task, Manager
from src.utilities import make_a_list, find_project_id, make_persons_list, find_person_id


def delete_item_section(session, projects_from_query, managers_from_query, tasks_from_query,
                        assignees_from_query) -> None:
    """
    Displays a Streamlit container with columns and tabs for deleting items.

    This code block creates a container in a Streamlit application that allows users to delete selected items
    such as tasks, assignees, or projects. It divides the UI into two columns, with the left column displaying
    a header and description, and the right column displaying data retrieved from a database and organized
    into tabs for deletion operations.

    Layout:
    - Left Column:
      - Displays a header titled "Delete selected Item".
      - Provides a brief description of the operation: "Get Rid of the unnecessary items."
    - Right Column:
      - Queries the database to retrieve lists of assignees, projects, and tasks.
      - Displays a divider for visual separation.
      - Organizes the deletion options into three tabs: "delete task", "delete assignee", and "delete project".

    Components:
    - `st.container()`: Creates a container for grouping the UI elements together.
    - `st.write("---")`: Inserts a horizontal rule (divider) to separate sections visually.
    - `st.columns([1, 3])`: Creates two columns with a 1:3 width ratio. The left column is narrower,
      and the right column is wider.
    - Left Column:
      - `st.header("Delete selected Item")`: Adds a header to the left column.
      - `st.write('Get Rid of the unnecessary items.')`: Adds a description below the header.
    - Right Column:
      - Queries the `Assignee`, `Project`, and `Task` tables using SQLAlchemy to fetch the necessary data.
      - `st.divider()`: Adds another visual divider before the tabs.
      - `st.tabs(...)`: Creates three tabs for different deletion operations.

    Parameters:
    - `assignees_from_query`: The list of assignees retrieved from the database, containing their ID, first name,
      and last name.
    - `projects_from_query`: The list of projects retrieved from the database, containing their ID, name, aim,
      and budget.
    - `tasks_from_query`: The list of tasks retrieved from the database, containing their ID and task name.

    Tabs:
    - "delete task": Tab for deleting tasks from the database.
    - "delete assignee": Tab for deleting assignees from the database.
    - "delete project": Tab for deleting projects from the database.

    This structure allows for a user-friendly interface where different entities can be deleted in a structured
    and organized manner using Streamlit.
    """
    with (st.container()):
        st.write("---")
        left_column, right_column = st.columns([1, 3])
        with left_column:
            st.header("Delete selected Item")
            st.write('Get Ride of the unnecessary items.')
        with right_column:
            st.divider()
            tab1, tab2, tab3, tab4 = st.tabs(["delete project", "delete manager", "delete task", "delete assignee"])
            with tab1:
                with st.form('delete_project', clear_on_submit=True):
                    st.write("Delete Project:")
                    selected_project = st.selectbox('Select a Project to delete',
                                                    make_a_list(projects_from_query))
                    selected_project_id = find_project_id(projects_from_query, selected_project)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        project_to_delete = session.query(Project).filter(Project.id == selected_project_id).first()
                        if project_to_delete:
                            try:
                                # Delete the project from the session and commit the transaction
                                session.delete(project_to_delete)
                                session.commit()
                                st.write(f"The project _'{selected_project}'_ was successfully deleted.")
                            except Exception as e:
                                session.rollback()
                                st.write(f"An error occurred: {e}")
                            finally:
                                db_engine.close_session()
                        else:
                            st.write(f"The project _'{selected_project}'_ could not be found.")
                    else:
                        st.write('To succeed please select input and smash a Submit button.')
            with tab2:
                with st.form('delete_manager', clear_on_submit=True):
                    st.write("Delete manager:")
                    selected_manager = st.selectbox('Select a Manager to delete',
                                                    make_persons_list(managers_from_query))
                    selected_manager_id = find_person_id(managers_from_query, selected_manager)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        manager_to_delete = session.query(Manager).filter(Manager.id == selected_manager_id).first()
                        if manager_to_delete:
                            try:
                                session.delete(manager_to_delete)
                                session.commit()
                                st.write(f"The manager _'{selected_manager}'_ was successfully deleted.")
                            except Exception as e:
                                session.rollback()
                                st.write(f"An error occurred: {e}")
                            finally:
                                db_engine.close_session()
                        else:
                            st.write(f"The manager _'{selected_manager}'_ could not be found.")
                    else:
                        st.write('To succeed please select input and smash a Submit button.')
            with tab3:
                with st.form('delete_task', clear_on_submit=True):
                    st.write("Delete task:")
                    selected_task = st.selectbox('Select a Task to delete', make_a_list(tasks_from_query))
                    selected_task_id = find_project_id(tasks_from_query, selected_task)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        task_to_delete = session.query(Task).filter(Task.id == selected_task_id).first()
                        if task_to_delete:
                            try:
                                session.delete(task_to_delete)
                                session.commit()
                                st.write(f"The task _'{selected_task}'_ was successfully deleted.")
                            except Exception as e:
                                session.rollback()
                                st.write(f"An error occurred: {e}")
                            finally:
                                db_engine.close_session()
                        else:
                            st.write(f"The manager _'{selected_manager}'_ could not be found.")
                    else:
                        st.write('To succeed please select input and smash a Submit button.')
            with tab4:
                with st.form('delete_assignee', clear_on_submit=True):
                    st.write("Delete assignee:")
                    selected_assignee = st.selectbox('Select a Assignee to delete',
                                                     make_persons_list(assignees_from_query))
                    selected_assignee_id = find_person_id(assignees_from_query, selected_assignee)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        assignee_to_delete = session.query(Assignee).filter(Assignee.id == selected_assignee_id).first()
                        if assignee_to_delete:
                            try:
                                session.delete(assignee_to_delete)
                                session.commit()
                                st.write(f"The assignee _'{selected_assignee}'_ was successfully deleted.")
                            except Exception as e:
                                session.rollback()
                                st.write(f"An error occurred: {e}")
                            finally:
                                db_engine.close_session()
                        else:
                            st.write(f"The manager _'{selected_assignee}'_ could not be found.")
                    else:
                        st.write('To succeed please select input and smash a Submit button.')
