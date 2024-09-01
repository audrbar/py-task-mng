"""This File Holds Overview Section."""
import streamlit as st
from sqlalchemy.orm import joinedload, Session

from src.base import db_engine
from src.models import Assignee, Project, Task, Manager
from utils.utilities import assignees_to_df, projects_to_df, tasks_to_df, managers_to_df


def overview_section(session: Session | Session) -> None:
    """Displays an overview of projects, managers, tasks, and assignees in the application.

    This function is responsible for querying and displaying data from the database in a tabbed
    interface using Streamlit. It retrieves all projects, managers, tasks, and assignees from
    the database, along with their associated relationships, and presents this data in a series
    of tabs within the application interface.

    Parameters:
    session : sqlalchemy.orm.session.Session
        The SQLAlchemy session used for querying the database. This session manages transactions
        and ensures that all queries are executed within the context of the current session.

    Returns:
    None
        This function does not return any values. It directly updates the Streamlit interface with
        the retrieved data.

    Notes:
    - The function handles any exceptions that occur during database queries by rolling back the
      session and printing an error message to the console.
    - The session is closed in the `finally` block to ensure that all resources are properly released
      after the function completes.
    - The data is displayed in a tabbed format, with separate tabs for projects, managers, tasks, and
      assignees. Each tab contains a dataframe showing the relevant data.

    Streamlit Interface:
    - **Projects Tab**: Displays a dataframe of all projects, including their managers and tasks.
    - **Managers Tab**: Displays a dataframe of all managers, including their associated projects.
    - **Tasks Tab**: Displays a dataframe of all tasks, including their associated projects and assignees.
    - **Assignees Tab**: Displays a dataframe of all assignees, including their assigned tasks.
    """
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
