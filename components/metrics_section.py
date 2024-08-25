from datetime import datetime, timedelta

import streamlit as st
from sqlalchemy import and_

from src.models import Assignee, Project, Task


def metrics_section(session) -> None:
    five_days_ago = datetime.now() - timedelta(days=5)
    number_of_projects = []
    number_of_tasks = []
    number_of_tasks_in_progres = []
    number_of_tasks_done = []
    number_of_assignees = []
    number_of_projects_new = []
    number_of_tasks_new = []
    number_of_tasks_in_progres_upd = []
    number_of_tasks_done_upd = []
    number_of_assignees_new = []
    try:
        number_of_assignees = session.query(Assignee).count()
        number_of_assignees_new = session.query(Assignee).filter(Assignee.updated_at >= five_days_ago).count()
        number_of_projects = session.query(Project).count()
        number_of_projects_new = session.query(Project).filter(Project.updated_at >= five_days_ago).count()
        number_of_tasks = session.query(Task).count()
        number_of_tasks_new = session.query(Task).filter(Task.updated_at >= five_days_ago).count()
        number_of_tasks_in_progres = session.query(Task).where(and_(Task.status == "in_progres",
                                                                    Task.updated_at >= five_days_ago)).count()
        number_of_tasks_in_progres_upd = session.query(Task).where(and_(Task.status == "in_progres",
                                                                        Task.updated_at >= five_days_ago)).count()
        number_of_tasks_done = session.query(Task).filter(Task.status == "done").count()
        number_of_tasks_done_upd = session.query(Task).where(and_(Task.status == "done",
                                                                  Task.updated_at >= five_days_ago)).count()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    with st.container():
        st.divider()
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Projects count", f"{number_of_projects}", f"{number_of_projects_new}")
        col2.metric("Tasks count", f"{number_of_tasks}", f"{number_of_tasks_new}")
        col3.metric("Tasks in progress", f"{number_of_tasks_in_progres}", f"{number_of_tasks_in_progres_upd}")
        col4.metric("Tasks done", f"{number_of_tasks_done}", f"{number_of_tasks_done_upd}")
        col5.metric("Our Team", f"{number_of_assignees}", f"{number_of_assignees_new}")
