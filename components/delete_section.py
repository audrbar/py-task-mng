"""Delete Item Section."""
from typing import Any

import streamlit as st
from sqlalchemy.orm import Session

from src.base import db_engine
from src.models import Assignee, Project, Task, Manager
from src.utilities import make_a_list, find_project_id, make_persons_list, find_person_id


def delete_item_section(session: Session | Session, projects_from_query: list[Any], managers_from_query: list[Any],
                        tasks_from_query: list[Any], assignees_from_query: list[Any]) -> None:
    """Displays an interface section for deleting items from the database.

    This function creates a Streamlit interface section that allows users to delete projects, managers,
    tasks, and assignees from the database. Users can select an item from a dropdown menu, and upon
    submission, the selected item is deleted from the database.

    Parameters:
    session : sqlalchemy.orm.session.Session
     The SQLAlchemy session used for querying and committing changes to the database. This session
     manages transactions and ensures that deletions are properly executed and committed.
    projects_from_query : list
     A list of project objects retrieved from the database, used to populate the project deletion dropdown.
    managers_from_query : list
     A list of manager objects retrieved from the database, used to populate the manager deletion dropdown.
    tasks_from_query : list
     A list of task objects retrieved from the database, used to populate the task deletion dropdown.
    assignees_from_query : list
     A list of assignee objects retrieved from the database, used to populate the assignee deletion dropdown.

    Returns:
    None
     This function does not return any values. It directly updates the Streamlit interface based on
     user actions and the database operations performed.

    Notes:
    - The function handles any exceptions that occur during database operations by rolling back the session
    and displaying an error message to the user.
    - After each deletion, the session is closed to ensure that resources are properly released.
    - The user is prompted to select an item and confirm the deletion by pressing the Submit button. If the
    item cannot be found in the database, an appropriate message is displayed.
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
