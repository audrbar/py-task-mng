"""This File Serves Edit Data page."""
from sqlalchemy import select

from components.edit_section import edit_section
from components.add_section import add_section
from components.delete_section import delete_item_section
from src.base import session, db_engine
from src.models import Assignee, Manager, Project, Task
from utils.st_utils import header_section, footer_section


def main() -> None:
    """Main function to display and manage the project items in the Streamlit application.

    This function orchestrates the main sections of the Streamlit app, allowing users
    to edit, add, and delete items related to projects. It organizes the UI into
    various sections for different operations, such as editing, adding, and deleting
    project-related items. Additionally, it includes a header and footer for the application.

    Sections:
    - Header Section:
      - Displays a header with the title "Edit Your Project's Items".
      - Provides a description guiding the user to select the appropriate tab to edit
        different aspects of their projects and view the results displayed above.
    - Edit Section:
      - Calls `edit_section(session)` to provide the UI for editing various project items.
    - Add Section:
      - Calls `add_section(session)` to provide the UI for adding new items (projects, tasks, persons)
        to the system.
    - Delete Item Section:
      - Calls `delete_item_section(session)` to provide the UI for deleting existing items from the system.
    - Footer Section:
      - Calls `footer_section()` to display the footer of the application.

    Parameters: None

    Notes:
    - The function assumes the existence of a global `session` object representing the SQLAlchemy session
      used for database operations.
    - Each section function (`header_section`, `edit_section`, `add_section`, `delete_item_section`,
      `footer_section`) is responsible for rendering a specific part of the UI and handling user interactions.

    This function serves as the entry point for the Streamlit app, organizing the layout and flow of the
    application, and ensuring that users can manage their project items efficiently.
    """
    header_section("Edit Your Project's Items", "Edit different aspects of your projects "
                                                "and choose for that the tab accordingly and check the results write "
                                                "above.")
    projects_from_query = []
    managers_from_query = []
    tasks_from_query = []
    assignees_from_query = []
    try:
        projects_from_query = session.execute(select(Project).order_by(Project.id)).scalars().all()
        managers_from_query = session.execute(select(Manager).order_by(Manager.id)).scalars().all()
        tasks_from_query = session.execute(select(Task).order_by(Task.id)).scalars().all()
        assignees_from_query = session.execute(select(Assignee).order_by(Assignee.id)).scalars().all()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        db_engine.close_session()
    edit_section(projects_from_query, tasks_from_query, assignees_from_query)
    add_section(projects_from_query, assignees_from_query)
    delete_item_section(projects_from_query, managers_from_query, tasks_from_query, assignees_from_query)
    footer_section()


if __name__ == "__main__":
    main()
