"""
This File Holds Edit Items Section.
"""
from models.person import Person
from models.project import Project
from models.task import Task
from models.persontasks import PersonTask
from src.utilities import *


def edit_section(session):
    persons_from_query = session.query(Person.id, Person.firstname, Person.lastname).all()
    projects_from_query = session.query(Project.id, Project.project_name, Project.project_aim,
                                        Project.project_budget).all()
    tasks_from_query = session.query(Task.id, Task.task_name, Task.status, Task.project_id).all()
    with ((st.container())):
        st.write("---")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["assign manager", "edit budget", "assign assignee",
                                                "change status", "set salary"])
        with tab1:
            with st.form('project_manager', clear_on_submit=True):
                st.write("Assign Project Manager:")
                selected_project = st.selectbox('Select a Project task is for:',
                                                make_a_list(projects_from_query))
                selected_project_id = find_project_id(projects_from_query, selected_project)
                selected_person = st.selectbox('Select a manager:', make_persons_list(persons_from_query))
                selected_person_id = find_person_id(persons_from_query, selected_person)
                submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    session.query(Project).filter(Project.id == selected_project_id).update(
                        {Project.person_id: selected_person_id}, synchronize_session=False)
                    session.commit()
                    st.cache_data.clear()
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
                    st.cache_data.clear()
                else:
                    st.write('To succeed please select and fill inputs and smash a Submit button.')

        with tab3:
            with st.form('assign_assignee', clear_on_submit=True):
                st.write('Assign Task Assignee:')
                selected_task = st.selectbox('Select a task to edit:', make_a_list(tasks_from_query))
                selected_person = st.selectbox('Select a Assignee to assign:', make_persons_list(persons_from_query))
                selected_person_id = find_person_id(persons_from_query, selected_person)
                submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    session.query(Task).filter(Task.task_name == selected_task).update(
                        {Task.person_id: selected_person_id}, synchronize_session=False)
                    session.commit()
                    st.cache_data.clear()
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
                    st.cache_data.clear()
                else:
                    st.write('To succeed please select input and smash a Submit button.')
        with tab5:
            with st.form('set_salary', clear_on_submit=True):
                st.write('Set Persons salary:')
                selected_person = st.selectbox('Select a Assignee to assign:', make_persons_list(persons_from_query))
                provided_salary = st.number_input('Provide salary value, $')
                selected_person_id = find_person_id(persons_from_query, selected_person)
                submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    session.query(Person).filter(Person.id == selected_person_id).update(
                        {Person.salary: provided_salary}, synchronize_session=False)
                    session.commit()
                    st.cache_data.clear()
                else:
                    st.write('To succeed please select and fill inputs and smash a Submit button.')
