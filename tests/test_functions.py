"""Functions tests."""
from typing import List
import utils.utilities as func_to_test
from src.models import Assignee, Project
from tests.conftest import test_assignees_list, test_projects_list


def test_make_assignees_list(test_assignees_list: List[Assignee]) -> None:
    """Tests the make_assignees_list function to ensure it correctly processes a list of person data.

    This test checks whether the make_assignees_list function correctly combines the first and last names
    of persons in the provided list and returns them as a list of full names. The function is expected to
    return a list containing the full names of the persons provided in the input list.

    Parameters:
    test_assignees_list : list[Assignee]
        A list of tuples representing person data, provided by the test fixture. Each tuple contains
        information about a person, including their ID, first name, last name, salary, and email.

    Returns: None : This test function does not return any value. It asserts that the result of the make_assignees_list
    function matches the expected output, which is a list of full names in the format 'First Last'.
    """
    result = func_to_test.make_assignees_list(test_assignees_list)
    assert result == ['Alice Brown', 'Charlie Davis']


def test_find_assignee_id(test_assignees_list: List[Assignee]) -> None:
    """Tests the find_person_id function to ensure it correctly identifies the person ID for a given full name.

    This test checks whether the find_person_id function correctly returns the ID of a person when provided
    with a list of person data and a specific full name (first name and last name combined). The function is expected
    to search through the list and return the ID associated with the specified full name.

    Parameters:
    test_assignees_list : list[Assignee]
        A list of tuples representing person data, provided by the test fixture. Each tuple contains
        information about a person, including their ID, first name, last name, salary, and email.

    Returns: None : This test function does not return any value. It asserts that the result of the find_person_id
    function matches the expected person ID.
    """
    result = func_to_test.find_assignee_id(test_assignees_list, 'Alice Brown')
    assert result == 1


def test_make_projects_list(test_projects_list: List[Project]) -> None:
    """Tests the make_projects_list function to ensure it correctly processes a list of projects data.

    This test checks whether the make_projects_list function correctly makes list of projects names. The function
    is expected to return a list containing the names of the projects provided in the input list.

    Parameters:
    test_projects_list : list[Project]
        A list of tuples representing project data, provided by the test fixture. Each tuple contains
        information about a project, including their ID, name, aim, budget, manager and tasks.

    Returns: None : This test function does not return any value. It asserts that the result of the make_projects_list
    function matches the expected output, which is a list of projects names.
    """
    result = func_to_test.make_projects_list(test_projects_list)
    assert result == ['Wind Factory Project', 'Sun Energy Project']


def test_find_project_id(test_projects_list: List[Project]) -> None:
    """Tests the find_project_id function to ensure it correctly identifies the project ID for a given project name.

    This test checks whether the find_project_id function correctly returns the ID of a project when provided
    with a list of project data and a specific project name. The function is expected to search through the list
    and return the ID associated with the specified project name.

    Parameters:
    test_projects_list : list[Project]
        A list of tuples representing project data, provided by the test fixture. Each tuple contains
        information about a project, including the project ID, name, aim, budget, manager details, and associated tasks.

    Returns: None : This test function does not return any value. It asserts that the result of the find_project_id
    function matches the expected project ID.
    """
    result = func_to_test.find_project_id(test_projects_list, 'Wind Factory Project')
    assert result == 1
