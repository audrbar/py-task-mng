"""
This File Serves New Item Section for Add Item Page.
"""
import streamlit as st

from src.base import db_engine
from src.models import Project, Assignee, Task, Manager
from src.utilities import make_a_list, make_persons_list, find_project_id


def add_section(session, projects_from_query, assignees_from_query):
    """
    Displays a Streamlit section for inserting new items into the system.

    This function creates a Streamlit UI section that allows users to insert new items
    (projects, tasks, assignees) into the system. The section is divided into two columns
    with a header and description in the right column and data retrieval and input tabs
    in the left column.

    Layout:
    - Left Column:
      - Displays tabs for adding a new project, task, or assignee.
      - Retrieves data from the database for populating form fields and dropdowns:
        - `assignees_from_query`: A list of all assignees, including their ID, first name, and last name.
        - `managers_from_query`: A list of assignees who are not currently managing any projects.
        - `projects_from_query`: A list of all projects, including their ID, name, aim, and budget.
        - `last_tasks_query`: Retrieves the most recent task ID, used for ordering or reference.
    - Right Column:
      - Displays a header titled "Insert New Item".
      - Provides a brief description instructing the user to insert new items (projects, tasks, or assignees)
        and provide the necessary details.

    Components:
    - `st.container()`: Creates a container to group the UI elements together.
    - `st.write("---")`: Inserts a horizontal rule (divider) to visually separate sections.
    - `st.columns([2, 1])`: Creates two columns with a 2:1 width ratio. The left column is wider
      for data and input fields, and the right column is narrower for the header and description.
    - Right Column:
      - `st.header("Insert New Item")`: Adds a header to the right column.
      - `st.write(...)`: Adds a description explaining the purpose of the section.
    - Left Column:
      - Queries the `Assignee`, `Project`, and `Task` tables using SQLAlchemy to fetch the necessary data.
      - `st.tabs(...)`: Creates three tabs for different insertion operations.

    Parameters:
    session (Session): The SQLAlchemy session used to query the database.

    Tabs:
    - "add project": Tab for inserting a new project into the database.
    - "add task": Tab for inserting a new task into the database.
    - "add assignee": Tab for inserting a new assignee into the database.

    This structure provides a user-friendly interface for adding new entities to the system,
    with relevant data fetched from the database to assist in the process.
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
