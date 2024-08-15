import streamlit as st
import streamlit_lottie as lto
import requests
from datetime import datetime
from components.header import header_section
from src.base import db_engine, Model
from src.person import Person
from src.project import Project
from src.task import Task
from src.persontasks import PersonTask


def page_config() -> None:
    """
    Configures the Streamlit page settings.

    This function sets the configuration for the entire Streamlit page, including the page title, icon, layout,
    and initial sidebar state. It uses Streamlit's `st.set_page_config` method to apply these settings globally
    to the app.
    The following configurations are applied:
    - `page_title`: Sets the title of the web page to "Project Management App".
    - `page_icon`: Sets the page icon to a globe emoji (🌐).
    - `layout`: Defines the layout as wide, allowing the app to take up the full width of the browser window.
    - `initial_sidebar_state`: Sets the initial state of the sidebar to "auto", which allows it to be expanded or collapsed automatically.
    - `menu_items`: No custom menu items are specified (defaults to `None`).

    :return: None
    """
    st.set_page_config(
        page_title="Project Management App",
        page_icon=":globe_with_meridians:",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items=None
    )


def hide_st_style() -> None:
    """
    Hides Streamlit's default interface elements from the page view.

    This function uses Streamlit's `st.markdown` method to inject custom CSS into the page. It hides the main menu,
    footer, and header typically provided by Streamlit's default interface, making the page cleaner and less cluttered
    for visitors.
    The following elements are hidden:
    - `#MainMenu`: The hamburger menu that typically appears in the top-right corner.
    - `footer`: The footer that usually contains "Made with Streamlit".
    - `header`: The header that might contain additional controls or branding.
    :return: None
    """
    st.markdown("""
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
            </style>
            """,
                unsafe_allow_html=True)


def load_lottie_url(url) -> object | None:
    """
    Loads a lightweight animation file from a given LottieFiles URL.

    This function sends a GET request to the specified URL to retrieve a Lottie animation file in JSON format.
    If the request is successful (status code 200), the function parses the JSON and returns the Lottie animation
    object for use in a Streamlit application. If the request fails, it returns `None`.
    :param url: The URL of the Lottie animation file to load.
    :return: The Lottie animation object if the request is successful, otherwise `None`.
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    animation = lto.st_lottie(r.json())
    return animation


def hero_section() -> None:
    """
    Renders the hero section of the Streamlit page.

    This function creates a visually engaging hero section at the top of the Streamlit page using a combination of
    text and animation. It uses Streamlit's container, columns, title, and write methods to display key information
    about the Team Workflow Manager application, including its technological stack and hosting details.
    The hero section is split into two columns:
    - The left column contains descriptive text about the application, highlighting its use of Python, hosting on
      Streamlit Community Cloud, and data storage on a PostgreSQL database managed by Supabase.
    - The right column loads and displays a Lottie animation via the `load_lottie_url` function, adding a dynamic
      visual element to the page.
    The section is separated from the rest of the content by a horizontal line rendered using the `st.write("---")` method.
    :return: None
    """
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2, gap="small")
        with left_column:
            st.write("Built with _Python_, *Team Workflow Manager* is hosted on *Streamlit Community Cloud*, offering "
                     "seamless access and real-time updates. All project data, including task details, budget "
                     "allocations, and team information, are securely stored in a *PostgreSQL* database hosted on "
                     "*Supabase*, ensuring reliability and scalability for your project management needs.")
        with right_column:
            load_lottie_url("https://lottie.host/5b073eca-e11c-4391-8593-b28f39ce0870/q0fz2A3kuN.json")


def footer_section() -> None:
    """
    Renders the footer section of the Streamlit page.

    This function creates a footer at the bottom of the Streamlit page, providing a clear separation from the rest
    of the content with a horizontal line. The footer includes a copyright notice with the current year and the
    name "audrbar".
    The footer section includes:
    - A horizontal line rendered using `st.write("---")` to visually separate the footer from the main content.
    - A dynamically generated copyright notice that uses the current year (retrieved from `datetime.now().year`).
    :return: None
    """
    with st.container():
        st.write("---")
        year = datetime.now().year
        st.write(f"© {year} audrbar. All rights reserved.")


def main():
    """
    The main entry point of the Streamlit application.

    This function orchestrates the rendering of the entire Streamlit page by calling the following functions in sequence:
    - `hide_st_style()`: Hides Streamlit's default interface elements (such as the menu and footer) to provide a cleaner user interface.
    - `header_section()`: Renders the page header, including the application title and a brief description of the app's functionality.
    - `hero_section()`: Renders the hero section, which includes key information about the application and a visual animation.
    - `footer_section()`: Renders the footer, which includes a horizontal separator and a dynamically generated copyright notice.
    This function serves as the central point for assembling and displaying the various sections of the application interface, ensuring
    that all content is presented in the correct order.
    :return: None
    """
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
