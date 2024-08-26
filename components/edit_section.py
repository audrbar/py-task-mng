"""This File Holds Edit Items Section."""
from typing import Any

import streamlit as st
from sqlalchemy.orm import Session

from src.base import db_engine
from src.models import Assignee, Project, Task, AssigneeTask
from src.utilities import find_person_id, find_project_id, make_a_list, make_persons_list


def edit_section(session: Session | Session, projects_from_query: list[Any], managers_from_query: list[Any],
                 tasks_from_query: list[Any], assignees_from_query: list[Any]) -> None:
    """Displays an interface for updating various items in the database.

    The function uses Streamlit to create a user interface that allows users to select and update different
    attributes of projects, tasks, and assignees. The changes are applied to the database through SQLAlchemy
    sessions, and the interface provides feedback on successful operations.

    Parameters:
    session : sqlalchemy.orm.session.Session
        The SQLAlchemy session used for querying and updating the database.
    projects_from_query : list
        A list of project objects retrieved from the database.
    managers_from_query : list
        A list of manager objects retrieved from the database.
    tasks_from_query : list
        A list of task objects retrieved from the database.
    assignees_from_query : list
        A list of assignee objects retrieved from the database.

    Interface Sections:
    The interface is divided into five tabs, each handling a different type of update:
    1. **Assign Manager**:
       - Allows the user to select a project and assign a manager to it.
       - The selected manager is assigned to the selected project, and the change is committed to the database.
    2. **Edit Budget**:
       - Allows the user to select a project and update its budget.
       - The budget value is updated in the database for the selected project.
    3. **Assign Assignee**:
       - Allows the user to select a task and assign an assignee to it.
       - The selected assignee is linked to the selected task, and the relationship is stored in the database.
    4. **Change Status**:
       - Allows the user to select a task and update its status.
       - The task's status is updated in the database based on the selected value.
    5. **Set Salary**:
       - Allows the user to select an assignee and set their salary.
       - The assignee's salary is updated in the database with the provided value.

    Notes:
    - The forms within each tab clear upon submission to allow for additional updates.
    - The function commits each change to the database and closes the session after each operation.
    - If the form is submitted without making a selection, the interface prompts the user to provide the
    necessary input.
    - Users are encouraged to check the results of their updates on the _Data Overview Page_.
    """
    with (st.container()):
        st.write("---")
        left_column, right_column = st.columns([1, 3])
        with left_column:
            st.header("Update Items")
            st.write('Update existing data: assign manager, change project budget, assign task assignee, set salary, '
                     'change task status and check the results in _Data Overview Page_.')
        with right_column:
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["assign manager", "edit budget", "assign assignee",
                                                    "change status", "set salary"])
            with tab1:
                with st.form('project_manager', clear_on_submit=True):
                    st.write("Assign Project Manager:")
                    selected_project = st.selectbox('Select a Project task is for:',
                                                    make_a_list(projects_from_query))
                    selected_project_id = find_project_id(projects_from_query, selected_project)
                    selected_manager = st.selectbox('Select a manager:', make_persons_list(managers_from_query))
                    selected_manager_id = find_person_id(managers_from_query, selected_manager)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        session.query(Project).filter(Project.id == selected_project_id).update(
                            {Project.manager_id: selected_manager_id}, synchronize_session=False)
                        session.commit()
                        db_engine.close_session()
                        st.write(f"The project _'{selected_project}'_ management was assigned "
                                 f"to _'{selected_manager}'_.")
                    else:
                        st.write('To succeed please select and fill inputs and smash a Submit button.')
            with tab2:
                with st.form('project_budget', clear_on_submit=True):
                    st.write("Edit Project Budget:")
                    selected_project = st.selectbox('Select a Project task is for:',
                                                    make_a_list(projects_from_query))
                    provided_budget = st.number_input('Provide budget value, $')
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        session.query(Project).filter(Project.project_name == selected_project).update(
                            {Project.project_budget: provided_budget}, synchronize_session=False)
                        session.commit()
                        db_engine.close_session()
                        st.write(f"The project _'{selected_project}'_ budget was set to {provided_budget}$.")
                    else:
                        st.write('To succeed please select and fill inputs and smash a Submit button.')

            with tab3:
                with st.form('assign_assignee', clear_on_submit=True):
                    st.write('Assign Task Assignee:')
                    selected_task = st.selectbox('Select a task to edit:', make_a_list(tasks_from_query))
                    selected_assignee = st.selectbox('Select a Assignee to assign:',
                                                     make_persons_list(assignees_from_query))
                    selected_assignee_id = find_person_id(assignees_from_query, selected_assignee)
                    selected_task_id = find_project_id(tasks_from_query, selected_task)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        assignee_task_to_add = AssigneeTask(task_id=selected_task_id, assignee_id=selected_assignee_id)
                        session.add(assignee_task_to_add)
                        session.commit()
                        db_engine.close_session()
                        st.write(f"The task _'{selected_task}'_ was assigned to _'{selected_assignee}'_.")
                    else:
                        st.write('To succeed please select and fill inputs and smash a Submit button.')
            with tab4:
                with st.form('change_status', clear_on_submit=True):
                    st.write('Change Task status:')
                    selected_task = st.selectbox('Select a task to edit:', make_a_list(tasks_from_query))
                    selected_status = st.selectbox('Select a Task status to set', ['not_started', 'in_progres', 'done'])
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        session.query(Task).filter(Task.task_name == selected_task).update(
                            {Task.status: selected_status}, synchronize_session=False)
                        session.commit()
                        db_engine.close_session()
                        st.write(f"The task _'{selected_task}'_ status was changed to _'{selected_status}'_.")
                    else:
                        st.write('To succeed please select input and smash a Submit button.')
            with tab5:
                with st.form('set_salary', clear_on_submit=True):
                    st.write('Set Assignee salary:')
                    selected_assignee = st.selectbox('Select a Assignee to assign:',
                                                     make_persons_list(assignees_from_query))
                    provided_salary = st.number_input('Provide salary value, $')
                    selected_assignee_id = find_person_id(assignees_from_query, selected_assignee)
                    submit_button = st.form_submit_button(label='Submit')
                    if submit_button:
                        session.query(Assignee).filter(Assignee.id == selected_assignee_id).update(
                            {Assignee.salary: provided_salary}, synchronize_session=False)
                        session.commit()
                        db_engine.close_session()
                        st.write(f"The _{selected_assignee}\'s_ salary was set to _{provided_salary}$_.")
                    else:
                        st.write('To succeed please select and fill inputs and smash a Submit button.')
