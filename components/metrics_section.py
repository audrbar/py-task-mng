"""This File Holds Overview Section."""
from datetime import datetime, timedelta

import streamlit as st
from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.base import db_engine
from src.models import Assignee, Project, Task
from utils.st_utils import chart_section


def metrics_section(session: Session | Session) -> None:
    """Displays a metrics section in the application interface, summarizing key statistics.

    This function queries the database to retrieve and display various metrics, including the total count of
    projects, tasks, tasks in progress, tasks completed, and assignees. It also provides the count of new
    entries and updates within the last five days. The metrics are presented in a grid format using Streamlit's
    `metric` component.

    Parameters:
    session : sqlalchemy.orm.session.Session
        The SQLAlchemy session used for querying the database. This session manages transactions and ensures
        that all queries are executed within the context of the current session.

    Returns:
    None
        This function does not return any values. It directly updates the Streamlit interface with the retrieved data.

    Notes:
    - The function handles any exceptions that occur during database queries by rolling back the session and
      printing an error message to the console.
    - The metrics displayed include:
      1. **Projects count**: The total number of projects and the number of new or updated projects in the last 5 days.
      2. **Tasks count**: The total number of tasks and the number of new or updated tasks in the last 5 days.
      3. **Tasks in progress**: The total number of tasks currently in progress and the number of these updated
        in the last 5 days.
      4. **Tasks done**: The total number of completed tasks and the number of these updated in the last 5 days.
      5. **Our Team**: The total number of assignees and the number of new or updated assignees in the last 5 days.

    Streamlit Interface:
    - The metrics are displayed in a single row using Streamlit's column layout, with each metric occupying one column.
    - Each metric includes a label, the total count, and the count of new or updated entries in the specified
    time frame.
    """
    five_days_ago = datetime.now() - timedelta(days=5)
    all_assignees = []
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
        all_assignees = session.query(Assignee)
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
    finally:
        db_engine.close_session()
    with st.container():
        st.divider()
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Projects count", f"{number_of_projects}", f"{number_of_projects_new}")
        col2.metric("Tasks count", f"{number_of_tasks}", f"{number_of_tasks_new}")
        col3.metric("Tasks in progress", f"{number_of_tasks_in_progres}", f"{number_of_tasks_in_progres_upd}")
        col4.metric("Tasks done", f"{number_of_tasks_done}", f"{number_of_tasks_done_upd}")
        col5.metric("Our Team", f"{number_of_assignees}", f"{number_of_assignees_new}")
    chart_section(all_assignees)
