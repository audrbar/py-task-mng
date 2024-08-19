"""
This File Holds New Item Section.
"""
import streamlit as st

from models.project import Project
from models.person import Person
from models.task import Task
from models.persontasks import PersonTask
from src.utilities import make_a_list, make_persons_list, find_person_id, find_project_id


def new_item_section(session):
    persons_from_query = session.query(Person.id, Person.firstname, Person.lastname).all()
    projects_from_query = session.query(Project.id, Project.project_name, Project.project_aim,
                                        Project.project_budget).all()
    with st.container():
        st.write("---")
        tab1, tab2, tab3 = st.tabs(["add project", "add task", "add person"])
        with tab1:
            with st.form('add project', clear_on_submit=True):
                st.write("Add New Project:")
                project_name = st.text_input('Provide project name:')
                project_aim = st.text_area('Describe project aim:')
                project_budget = st.number_input('Provide budget value, $:', min_value=0.0,
                                                 max_value=10000000.0,
                                                 step=1.0, value=0.0)
                selected_person = st.selectbox('Select a manager:', make_persons_list(persons_from_query))
                selected_person_id = find_person_id(persons_from_query, selected_person)
                submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    project_to_add = Project(project_name=project_name, project_aim=project_aim,
                                             project_budget=project_budget, person_id=selected_person_id)
                    st.write(project_to_add)
                    session.add(project_to_add)
                    session.commit()
                else:
                    st.write('To succeed please fill and select inputs and smash a Submit button.')
        with tab2:
            with st.form('add task', clear_on_submit=True):
                st.write("Add New Task:")
                provided_task = st.text_input('Provide task name:')
                provided_start_date = st.date_input('Provide start date:', value=None, format="YYYY/MM/DD")
                provided_due_date = st.date_input('Provide due date:', value=None, format="YYYY/MM/DD")
                selected_person = st.selectbox('Select a assignee:', make_persons_list(persons_from_query))
                selected_person_id = find_person_id(persons_from_query, selected_person)
                selected_project = st.selectbox('Select a Project task is for:',
                                                make_a_list(projects_from_query))
                selected_project_id = find_project_id(projects_from_query, selected_project)
                submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    task_to_add = Task(task_name=provided_task, start_date=provided_start_date,
                                       due_date=provided_due_date, status="not_started", project_id=selected_project_id)
                    st.write(task_to_add)
                    session.add(task_to_add)
                    session.commit()
                else:
                    st.write('To succeed please select and fill inputs and smash a Submit button.')
        with tab3:
            with st.form('add person', clear_on_submit=True):
                st.write("Add New Person:")
                provided_firstname = st.text_input('Provide first name:')
                provided_lastname = st.text_input('Provide last name:')
                provided_email = st.text_input('Provide email:')
                provided_salary = st.number_input('Provide salary value, $:', min_value=40000.0,
                                                  max_value=100000.0, step=10.0, value=50000.0)
                submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    person_to_add = Person(firstname=provided_firstname, lastname=provided_lastname,
                                           salary=provided_salary, email=provided_email)
                    session.add(person_to_add)
                    session.commit()
                else:
                    st.write('To succeed please fill inputs and smash a Submit button.')
