import streamlit as st
from sqlalchemy import desc

from Home import footer_section
from models.person import Person
from models.project import Project
from models.task import Task
from models.persontasks import PersonTask
from src.utilities import header_section


def metrics_section(number_of_projects, number_of_tasks, number_of_tasks_in_progres, number_of_tasks_done,
                    number_of_persons) -> None:
    with st.container():
        st.divider()
        col1, col2, col3, col4, col5= st.columns(5)
        col1.metric("Projects count", f"{number_of_projects}", "1")
        col2.metric("Tasks count", f"{number_of_tasks}", "-1")
        col3.metric("Tasks in progress", f"{number_of_tasks_in_progres}", "2")
        col4.metric("Tasks done", f"{number_of_tasks_done}", "0")
        col5.metric("Our Team", f"{number_of_persons}", "-1")


def charts_section(some_data) -> None:
    with st.container():
        st.divider()
        st.write("Your chart goes here.")
        st.bar_chart(some_data)


def main():
    header_section("Dashboard", "Find Team Workflow Cool Statistics.")
    number_of_persons = Person.query.count()
    number_of_projects = Project.query.count()
    number_of_tasks = Task.query.count()
    number_of_tasks_in_progres = Task.query.filter(Task.status == "in_progres").count()
    number_of_tasks_done = Task.query.filter(Task.status == "done").count()
    metrics_section(number_of_projects, number_of_tasks, number_of_tasks_in_progres, number_of_tasks_done,
                    number_of_persons)
    all_persons = Person.query.limit(20).all()
    expanded_persons = (
        Person.query
        .join(Person.tasks)
        .filter(Task.id == 6)
        .order_by(desc(Person.id))
        .all()
    )
    charts_section(expanded_persons)
    first_person = Person.query.first()
    alice = Person.query.filter_by(firstname="Alice").all()
    bob = Person.query.filter(Person.firstname == "Bob").all()
    mail_users = Person.query.filter(Person.email.like("%example.com")).all()
    st.dataframe(all_persons)
    st.write(expanded_persons)
    st.write(first_person)
    st.write(alice)
    st.write(bob)
    st.write(mail_users)
    footer_section()


if __name__ == "__main__":
    main()