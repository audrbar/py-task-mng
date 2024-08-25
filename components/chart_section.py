"""
This File Holds Chart Section.
"""
import streamlit as st
from sqlalchemy.orm import joinedload

from src.base import db_engine
from src.models import Assignee
from src.utilities import assignees_to_chart


def chart_section(session) -> None:
    """
    Displays a bar chart of tasks per assignee in the Streamlit application.

    This function creates a section in the Streamlit app that visualizes the distribution
    of tasks assigned to each assignee. It retrieves all assignees from the database, processes
    the data to calculate the number of tasks per assignee, and displays this information in
    a bar chart.
    Parameters: session (Session): The SQLAlchemy session used to query the database for assignee data.
    Process:
    - Retrieves all `Assignee` instances from the database using the provided SQLAlchemy session.
    - Converts the list of `Assignee` instances into a pandas DataFrame using the `assignees_to_chart` function.
    - Concatenates each assignee's first and last name to create a `full_name` column.
    - Sets the `full_name` column as the DataFrame's index for easy visualization.
    - Extracts the `tasks` column, which contains the count of tasks per assignee.
    - Displays a bar chart in the Streamlit app showing the number of tasks assigned to each assignee.
    Returns: None: This function does not return any value; it directly modifies the Streamlit UI.
    Example Usage: Call this function within the main Streamlit app function to display the tasks per assignee chart:
        chart_section(session)
    Notes: The bar chart provides a visual representation of task distribution among assignees, helping users
      quickly identify task allocation.
    """
    st.divider()
    st.write("Tasks per assignee:")
    all_assignees = []
    try:
        all_assignees = session.query(Assignee).options(joinedload(Assignee.tasks)).all()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        db_engine.close_session()
    df = assignees_to_chart(all_assignees)
    df['full_name'] = df['firstname'] + ' ' + df['lastname']
    df.set_index('full_name', inplace=True)
    tasks_per_assignee = df['tasks']
    st.bar_chart(tasks_per_assignee)
