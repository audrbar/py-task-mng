"""This Is The Main Entry File for Entire App."""
from utils.st_utils import header_section, footer_section, page_config, hide_st_style, hero_section


def main() -> None:
    """The main entry point of the Streamlit application.

    This function orchestrates the rendering of the entire Streamlit page by calling the following functions
    in sequence:
    - `hide_st_style()`: Hides Streamlit's default interface elements (such as the menu and footer) to provide
       a cleaner user interface.
    - `header_section()`: Renders the page header, including the application title and a brief description
       of the app's functionality.
    - `hero_section()`: Renders the hero section, which includes key information about the application and a visual
       animation.
    - `footer_section()`: Renders the footer, which includes a horizontal separator and a dynamically generated
    copyright notice.

    This function serves as the central point for assembling and displaying the various sections of the application
    interface, ensuring that all content is presented in the correct order.
    :return: None
    """
    page_config()
    section_title = "Team Workflow Manager"
    section_description = ("Team Workflow Manager is a comprehensive tool designed to streamline the management "
                           "of projects, including tracking tasks, managing budgets, and coordinating team activities. "
                           "The application provides a user-friendly interface for project managers and team members "
                           "to collaborate efficiently and effectively.")
    hide_st_style()
    header_section(section_title, section_description)
    hero_section()
    footer_section()


if __name__ == "__main__":
    main()
