"""
Utility Functions of the Project.
"""
import streamlit as st
import streamlit_lottie as lto
import requests
import pandas as pd
from datetime import datetime


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
    - `initial_sidebar_state`: Sets the initial state of the sidebar to "auto", which allows it to be expanded
       or collapsed automatically.
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
    The section is separated from the rest of the content by a horizontal line rendered using the `st.write("---")`
    method.
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


def header_section(section_title, section_description) -> None:
    """
    Renders the header section of the Streamlit page.

    This function uses Streamlit's container, title, and write methods to display the main title and a brief
    description of the Team Workflow Manager application. The header provides users with an overview of
    the application's purpose and functionality.
    :return: None
    """
    with st.container():
        st.header(section_title)
        st.write(section_description)


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
        st.write(f"© {datetime.now().year} audrbar. All rights reserved.")


def make_a_list(source: list) -> list:
    """
    Extracts and returns a list of elements from the second position in each record of a given list.

    This function processes a list of records (each represented as a list or tuple) and extracts
    the element located at the second position (index 1) from each record. These extracted elements
    are then compiled into a new list, which is returned.
    Parameters: source (list): A list of records, where each record is a list or tuple. The function
                   extracts the element at index 1 from each record.
    Returns: list: A list of elements extracted from the second position (index 1) of each record in the `source` list.
    """
    result = []
    for item in source:
        result.append(item[1])
    return result


def find_project_id(source: list, selected_project: str) -> int:
    """
    Finds and returns the ID of a project from a list of records based on the project's name.

    This function iterates through a list of records (each represented as a list or tuple),
    where each record contains a project's ID and name. The function compares the project
    name with the `selected_project` string. If a match is found, the function returns the
    corresponding project's ID.
    Parameters: source (list): A list of records, where each record is a list or tuple containing:
                   - item[0]: The ID of the project (int).
                   - item[1]: The name of the project (str).
    selected_project (str): The name of the project to find.
    Returns: int: The ID of the project if a match is found; otherwise, the function implicitly returns None
         if no match is found.
    """
    for item in source:
        if selected_project == item[1]:
            return item[0]


def make_persons_list(source: list) -> list:
    """
    Creates and returns a list of full names from a list of records.

    This function processes a list of records (each represented as a list or tuple),
    where each record contains a person's first name and last name. The function
    concatenates the first name and last name to form the full name and adds it to
    a result list.
    Parameters:
    source (list): A list of records, where each record is a list or tuple containing:
                   - item[1]: The first name of the person (str).
                   - item[2]: The last name of the person (str).
    Returns:
    list: A list of full names, where each name is a concatenation of the first name
          and last name from each record in the `source` list.
    """
    result = []
    for item in source:
        result.append(item[1] + ' ' + item[2])
    return result


def find_person_id(source: list, selected_person: str) -> int:
    """
    Finds and returns the ID of a person from a list of records based on the person's full name.

    This function iterates through a list of records (each represented as a list or tuple),
    where each record contains a person's ID, first name, and last name. The function
    concatenates the first name and last name to form the full name and compares it with
    the `selected_person` string. If a match is found, the function returns the corresponding
    person's ID.
    Parameters: source (list): A list of records, where each record is a list or tuple containing:
                   - item[0]: The ID of the person (int).
                   - item[1]: The first name of the person (str).
                   - item[2]: The last name of the person (str).
    selected_person (str): The full name of the person to find, formatted as "FirstName LastName".
    Returns: int: The ID of the person if a match is found; otherwise, the function implicitly returns None
         if no match is found.
    """
    for item in source:
        if selected_person == (item[1] + ' ' + item[2]):
            return item[0]


def assignees_to_df(all_assignees):
    """
    Converts a list of Assignee objects into a pandas DataFrame.

    This function processes a list of Assignee instances, extracting relevant information
    to construct a DataFrame. Each row in the DataFrame represents a assignee, with columns
    for the assignee's ID, first name, last name, salary, email, associated project name,
    and a list of task names assigned to the assignee.
    Parameters: all_assignees (list): A list of Assignee instances.
    Returns: pd.DataFrame: A pandas DataFrame.
    """
    data = []
    for assignee in all_assignees:
        data.append({
            "id": assignee.id,
            "Full name": assignee.firstname + ' ' + assignee.lastname,
            "Salary": assignee.salary,
            "Email": assignee.email,
            "Tasks": ', '.join([task.task_name for task in assignee.tasks])
        })
    df = pd.DataFrame(data)
    return df


def managers_to_df(all_managers):
    """
    Converts a list of Manager objects who are project managers into a pandas DataFrame.

    This function processes a list of Manager instances, filtering out those who
    are not managing any projects, and compiles relevant details into a structured
    DataFrame. Each row in the DataFrame represents a manager who is managing a project,
    with columns for their ID, first name, last name, salary, email, and the name of
    the project they are managing.
    Parameters: all_managers (list): A list of Manager instances.
    Returns: pd.DataFrame: A pandas DataFrame.
    """
    data = []
    for manager in all_managers:
        if manager.project:
            data.append({
                "id": manager.id,
                "Full name": manager.firstname + ' ' + manager.lastname,
                "Salary": manager.salary,
                "Email": manager.email,
                "Project": manager.project.project_name
            })
    df = pd.DataFrame(data)
    return df


def projects_to_df(all_projects):
    """
    Converts a list of Project objects into a pandas DataFrame.

    This function processes a list of Project instances, extracting key details
    and compiling them into a structured DataFrame. Each row in the DataFrame
    represents a project, with columns for the project's ID, name, aim, budget,
    and the name of the person managing the project.
    Parameters: all_projects (list): A list of Project instances.
    Returns: pd.DataFrame: A pandas DataFrame.
    """
    data = []
    for project in all_projects:
        manager_name = None
        if project.manager:
            manager_name = project.manager.firstname + ' ' + project.manager.lastname

        data.append({
            "id": project.id,
            "Project name": project.project_name,
            "Project aim": project.project_aim,
            "Budget": project.project_budget,
            "Manager": manager_name,
            "Tasks": ', '.join([task.task_name for task in project.tasks])
        })
    df = pd.DataFrame(data)
    return df


def tasks_to_df(all_tasks):
    """
    Converts a list of Task objects into a pandas DataFrame.

    This function takes a list of Task instances and extracts relevant information to
    construct a DataFrame. Each row in the DataFrame represents a task, with columns
    for the task's ID, name, start date, due date, status, associated project name,
    and a list of assignees (persons assigned to the task).
    Parameters: all_tasks (list): A list of Task instances.
    Returns: pd.DataFrame: A pandas DataFrame.
    """
    data = []
    for task in all_tasks:
        data.append({
            "id": task.id,
            "Task name": task.task_name,
            "Start date": task.start_date,
            "Due date": task.due_date,
            "Status": task.status,
            "Project": task.project.project_name if task.project else None,
            "Assignees": ', '.join([assignee.firstname + ' ' + assignee.lastname for assignee in task.assignees])
        })
    df = pd.DataFrame(data)
    return df


def assignees_to_chart(all_assignees):
    """
    Converts a list of Assignee objects into a pandas DataFrame for charting tasks per assignee.

    This function processes a list of assignee instances and compiles relevant details into a
    structured DataFrame. Each row in the DataFrame represents a assignee, with columns for
    their ID, first name, last name, and the number of tasks they are assigned. This DataFrame
    is specifically designed to be used for generating charts that visualize the distribution
    of tasks among assignees.
    Parameters: all_assignees (list): A list of Assignee instances.
    Returns:pd.DataFrame: A pandas DataFrame.
    """
    data = []
    for assignee in all_assignees:
        data.append({
            "id": assignee.id,
            "firstname": assignee.firstname,
            "lastname": assignee.lastname,
            "tasks": len(assignee.tasks)
        })
    df = pd.DataFrame(data)
    return df
