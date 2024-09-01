"""This File Serves Data Overview page."""

from components.overview_section import overview_section
from src.base import session
from utils.st_utils import header_section, footer_section


def main() -> None:
    """Main function to display the data overview in the Streamlit application.

    This function organizes and displays the main sections of the Streamlit app, providing an overview of the
    content present in the system, such as projects, tasks, managers, and assignees. The UI is structured into a
    header, an overview section, and a footer, guiding the user through the available data and insights.

    Sections:
    - Header Section: Calls `header_section("Data Overview", "The section explores the content present on the system:
    *projects*, **tasks**, _managers_, **assignees**.")` to display the title of the section and a descriptive
    subtitle that highlights the focus on various content types.
    - Overview Section: Calls `overview_section(session)` to present an overview of the system's data, querying the
    database using  the provided SQLAlchemy session. This section typically includes summaries or key insights into
    the available  projects, tasks, managers, and assignees.
    - Footer Section:
    - Calls `footer_section()` to display the footer of the application, providing any additional information or links.

    Parameters: None

    Notes:
    - The function assumes the existence of a global `session` object representing the SQLAlchemy session used for
    database operations.
    - Each section function (`header_section`, `overview_section`, `footer_section`) is responsible for rendering
    a specific part of the UI and handling user interactions.
    This function serves as the entry point for the Streamlit app's data overview section, organizing the layout
    and ensuring that users can explore and understand the various content present in the system.
    """
    header_section("Data Overview", "The section explores the content present \
                on the system:  *projects*, **tasks**, _managers_, **assignees**.")
    overview_section(session)
    footer_section()


if __name__ == "__main__":
    main()
