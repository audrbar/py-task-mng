"""
This File Holds Edit Items Section.
"""
import streamlit as st

from src.base import db_engine
from src.models import Assignee, Project, Task, AssigneeTask
from src.utilities import find_person_id, find_project_id, make_a_list, make_persons_list


def edit_section(session, projects_from_query, managers_from_query, tasks_from_query, assignees_from_query):
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
