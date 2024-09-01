"""This File Serves Dashboard page."""

from components.chart_section import chart_section
from components.metrics_section import metrics_section
from src.base import session
from utils.st_utils import header_section, footer_section


def main() -> None:
    """Main function to display the dashboard in the Streamlit application.

    This function orchestrates the key sections of the Streamlit app, providing a dashboard
    that displays team workflow statistics. It organizes the UI into various sections,
    including a header, metrics, charts, and a footer, to give users a comprehensive view
    of their team's performance and workflow.

    Sections:
    - Header Section:
      - Calls `header_section("Dashboard", "Find Inspiring Team Workflow Statistics.")` to display
        the title of the dashboard and a motivational subtitle.
    - Metrics Section:
      - Calls `metrics_section(session)` to display key metrics related to team performance,
        such as completed tasks, active projects, and more. This section uses the SQLAlchemy
        session to query the necessary data from the database.
    - Chart Section:
      - Calls `chart_section(session)` to visualize task distribution among team members
        using a bar chart. This section also queries the database for relevant data.
    - Footer Section:
      - Calls `footer_section()` to display the footer of the application, providing any
        additional information or links.

    Parameters: None
    Notes:
    - The function assumes the existence of a global `session` object representing the SQLAlchemy session
      used for database operations.
    - Each section function (`header_section`, `metrics_section`, `chart_section`, `footer_section`)
      is responsible for rendering a specific part of the UI and handling user interactions.
    This function serves as the entry point for the Streamlit dashboard, organizing the layout
    and ensuring that users can access and interpret their team workflow statistics effectively.
    """
    header_section("Dashboard", "Find Inspiring Team Workflow Statistics: "
                                "_total count of items, recent updates and deletes_.")
    metrics_section(session)
    chart_section(session)
    footer_section()


if __name__ == "__main__":
    main()
