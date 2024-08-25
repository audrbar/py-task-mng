import streamlit as st
from sqlalchemy.orm import joinedload

from src.base import db_engine
from src.models import Assignee, Project, Task, Manager
from src.utilities import assignees_to_df, projects_to_df, tasks_to_df, managers_to_df


def overview_section(session) -> None:
    all_projects = []
    all_managers = []
    all_tasks = []
    all_assignees = []
    try:
        all_projects = (session.query(Project).options(joinedload(Project.manager),
                                                       joinedload(Project.tasks)).order_by(Project.id).all())
        all_tasks = (session.query(Task).options(joinedload(Task.project),
                                                 joinedload(Task.assignees)).order_by(Task.id).all())
        all_assignees = session.query(Assignee).options(joinedload(Assignee.tasks)).order_by(Assignee.id).all()
        all_managers = session.query(Manager).options(joinedload(Manager.project)).order_by(Manager.id).all()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        db_engine.close_session()
    with st.container():
        st.divider()
        tab1, tab2, tab3, tab4 = st.tabs(["projects", "managers", "tasks", "assignees"])
        tab1.dataframe(projects_to_df(all_projects), hide_index=True)
        tab2.dataframe(managers_to_df(all_managers), hide_index=True)
        tab3.dataframe(tasks_to_df(all_tasks), hide_index=True)
        tab4.dataframe(assignees_to_df(all_assignees), hide_index=True)
