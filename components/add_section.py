"""This File Serves New Item Section for Add Item Page."""
from typing import Any, List

import streamlit as st
from sqlalchemy.orm import Session

from src.base import db_engine
from src.models import Project, Assignee, Task, Manager
from src.utilities import make_a_list, make_persons_list, find_project_id


def add_section(session: Session, projects_from_query: list[Any], assignees_from_query: list[Any]) -> None:
    """Displays an interface section for adding new projects, tasks, and assignees to the database.

    This function creates a Streamlit interface section that allows users to add new projects,
    tasks, and assignees to the system. The interface includes forms for each type of item, and
    upon submission, the provided data is added to the database.

    Parameters:
    session : sqlalchemy.orm.session.Session
        The SQLAlchemy session used for querying and committing changes to the database. This session
        manages transactions and ensures that new records are properly added and committed.
    projects_from_query : list
        A list of project objects retrieved from the database, used to populate the project selection
        dropdown in the task creation form.
    assignees_from_query : list
        A list of assignee objects retrieved from the database, used to populate the assignee selection
        dropdown in the task creation form.

    Returns:
    None
        This function does not return any values. It directly updates the Streamlit interface based on
        user actions and the database operations performed.

    Notes:
    - The function handles each item type (project, task, assignee) in a separate tab within the Streamlit
      interface. Users can fill out the relevant forms to add new items to the database.
    - After each addition, the session is closed to ensure that resources are properly released.
    - Users are prompted to fill out all required fields and submit the form to successfully add a new item.
    """
    with st.container():
        st.write("---")
        left_column, right_column = st.columns([2, 1])
        with right_column:
            st.header("Insert New Item")
            st.write('Insert any new item - project, manager, task, assignee - to the system and provide \
                    the item details accordingly.')
        with left_column:
            tab1, tab2, tab3 = st.tabs(["add project", "add task", "add assignee"])
            with tab1:
                with st.form('add project', clear_on_submit=True):
                    st.write("Add New Project:")
                    project_name = st.text_input('Provide project name:')
                    project_aim = st.text_area('Describe project aim:')
                    project_budget = st.number_input('Provide budget value, $:', min_value=0.0,
                                                     max_value=1000000.0,
                                                     step=1.0, value=0.0)
                    provided_firstname = st.text_input('Provide manager first name:')
                    provided_lastname = st.text_input('Provide manager last name:')
                    provided_email = st.text_input('Provide manager email:')
                    provided_salary = st.number_input('Provide manager salary value, $:', min_value=40000.0,
                                                      max_value=100000.0, step=10.0, value=50000.0)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        manager_to_add = Manager(firstname=provided_firstname, lastname=provided_lastname,
                                                 salary=provided_salary, email=provided_email)
                        session.add(manager_to_add)
                        session.commit()
                        project_to_add = Project(project_name=project_name, project_aim=project_aim,
                                                 project_budget=project_budget, manager=manager_to_add)
                        session.add(project_to_add)
                        session.commit()
                        db_engine.close_session()
                        st.write(f"The project _'{project_name}'_ was created and manager "
                                 f"was _'{provided_firstname} {provided_lastname}'_ assigned to.")
                    else:
                        st.write('To succeed please fill and select inputs and smash a Submit button.')
            with tab2:
                with st.form('add task', clear_on_submit=True):
                    st.write("Add New Task:")
                    provided_task = st.text_input('Provide task name:')
                    provided_start_date = st.date_input('Provide start date:', value=None, format="YYYY/MM/DD")
                    provided_due_date = st.date_input('Provide due date:', value=None, format="YYYY/MM/DD")
                    selected_assignee = st.selectbox('Select a assignee:', make_persons_list(assignees_from_query))
                    selected_project = st.selectbox('Select a Project task is for:',
                                                    make_a_list(projects_from_query))
                    selected_project_id = find_project_id(projects_from_query, selected_project)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        task_to_add = Task(task_name=provided_task, start_date=provided_start_date,
                                           due_date=provided_due_date, status="not_started",
                                           project_id=selected_project_id)
                        session.add(task_to_add)
                        session.commit()
                        db_engine.close_session()
                        st.write(f"The task _'{provided_task}'_ to the project {selected_project} "
                                 f"was created and assigned to _'{selected_assignee}'_.")
                    else:
                        st.write('To succeed please select and fill inputs and smash a Submit button.')
            with tab3:
                with st.form('add assignee', clear_on_submit=True):
                    st.write("Add New Assignee:")
                    provided_firstname = st.text_input('Provide first name:')
                    provided_lastname = st.text_input('Provide last name:')
                    provided_email = st.text_input('Provide email:')
                    provided_salary = st.number_input('Provide salary value, $:', min_value=40000.0,
                                                      max_value=100000.0, step=10.0, value=50000.0)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        assignee_to_add = Assignee(firstname=provided_firstname, lastname=provided_lastname,
                                                   salary=provided_salary, email=provided_email)
                        session.add(assignee_to_add)
                        session.commit()
                        db_engine.close_session()
                        st.write(f"The assignee _'{provided_firstname} {provided_lastname}'_ was added.")
                    else:
                        st.write('To succeed please fill inputs and smash a Submit button.')
