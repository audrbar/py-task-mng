"""Utility Functions."""
import streamlit_lottie as lto
import requests
import pandas as pd
from typing import Any
from src.models import Manager, Assignee, Project, Task


def load_lottie_url(url: str) -> None | lto.st_lottie:
    """Loads a lightweight animation file from a given LottieFiles URL.

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


def make_tasks_list(source: list[Task]) -> list[Any]:
    """Extracts and returns a list of elements from the second position in each record of a given list.

    This function processes a list of records (each represented as a list or tuple) and extracts
    the element located at the second position (index 1) from each record. These extracted elements
    are then compiled into a new list, which is returned.

    Parameters: source (list): A list of records, where each record is a list or tuple. The function
                   extracts the element at index 1 from each record.

    Returns: list: A list of elements extracted from the second position (index 1) of each record in the `source` list.
    """
    result = []
    for item in source:
        result.append(item.task_name)
    return result


def find_task_id(source: list[Task], selected_task: str) -> Any:
    """Finds and returns the ID of a task from a list of records based on the task's name.

    This function iterates through a list of records (each represented as a list or tuple),
    where each record contains a project's ID and name. The function compares the task
    name with the `selected_task` string. If a match is found, the function returns the
    corresponding project's ID.

    Parameters: source (list): A list of records, where each record is a list or tuple containing:
                   - item.id: The ID of the task (int).
                   - item.task_name: The name of the task (str).
    selected_task (str): The name of the task to find.

    Returns: int: The ID of the project if a match is found; otherwise, the function implicitly returns None
         if no match is found.
    """
    for item in source:
        if selected_task == item.task_name:
            return item.id


def make_projects_list(source: list[Project]) -> list[str]:
    """Creates and returns a list of full names from a list of records.

    This function processes a list of records (each represented as a list or tuple),
    where each record contains a person's first name and last name. The function
    concatenates the first name and last name to form the full name and adds it to
    a result list.

    Parameters: source (list): A list of records, where each record is a list or tuple containing:
                   - item[1]: The first name of the person (str).
                   - item[2]: The last name of the person (str).

    Returns:
    list: A list of full names, where each name is a concatenation of the first name
          and last name from each record in the `source` list.
    """
    result = []
    for item in source:
        result.append(item.project_name)
    return result


def find_project_id(source: list[Project], selected_project: str) -> Any:
    """Finds and returns the ID of a project from a list of records based on the project's name.

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
        if selected_project == item.project_name:
            return item.id


def make_assignees_list(source: list[Assignee]) -> list[str]:
    """Creates and returns a list of full names from a list of records.

    This function processes a list of records (each represented as a list or tuple),
    where each record contains a person's first name and last name. The function
    concatenates the first name and last name to form the full name and adds it to
    a result list.

    Parameters: source (list): A list of records, where each record is a list or tuple containing:
                   - item[1]: The first name of the person (str).
                   - item[2]: The last name of the person (str).

    Returns:
    list: A list of full names, where each name is a concatenation of the first name
          and last name from each record in the `source` list.
    """
    result = []
    for item in source:
        result.append(item.firstname + ' ' + item.lastname)
    return result


def make_managers_list(source: list[Manager]) -> list[str]:
    """Creates and returns a list of full names from a list of records.

    This function processes a list of records (each represented as a list or tuple),
    where each record contains a person's first name and last name. The function
    concatenates the first name and last name to form the full name and adds it to
    a result list.

    Parameters: source (list): A list of records, where each record is a list or tuple containing:
                   - item[1]: The first name of the person (str).
                   - item[2]: The last name of the person (str).

    Returns:
    list: A list of full names, where each name is a concatenation of the first name
          and last name from each record in the `source` list.
    """
    result = []
    for item in source:
        result.append(item.firstname + ' ' + item.lastname)
    return result


def find_person_id(source: list[Assignee], selected_person: str) -> Any:
    """Finds and returns the ID of a person from a list of records based on the person's full name.

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
        if selected_person == (item.firstname + ' ' + item.lastname):
            return item.id


def assignees_to_df(all_assignees: list[Assignee]) -> pd.DataFrame:
    """Converts a list of Assignee objects into a pandas DataFrame.

    This function processes a list of Assignee instances, extracting relevant information to construct a DataFrame.
    Each row in the DataFrame represents an assignee, with columns for the assignee's ID, first name, last name,
    salary, email, associated project name and a list of task names assigned to the assignee.

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


def managers_to_df(all_managers: list[Manager]) -> pd.DataFrame:
    """Converts a list of Manager objects who are project managers into a pandas DataFrame.

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


def projects_to_df(all_projects: list[Project]) -> pd.DataFrame:
    """Converts a list of Project objects into a pandas DataFrame.

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


def tasks_to_df(all_tasks: list[Task]) -> pd.DataFrame:
    """Converts a list of Task objects into a pandas DataFrame.

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


def assignees_to_chart(all_assignees: list[Assignee]) -> pd.DataFrame:
    """Converts a list of Assignee objects into a pandas DataFrame for charting tasks per assignee.

    This function processes a list of assignee instances and compiles relevant details into a structured DataFrame.
    Each row in the DataFrame represents an assignee, with columns for their ID, first name, last name, and the number
    of tasks they are assigned. This DataFrame is specifically designed to be used for generating charts that
    visualize the distribution of tasks among assignees.

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
