from typing import Any, List, Callable, TypeVar, Dict, Tuple, cast
import utils.utilities as func_to_test


F = TypeVar('F', bound=Callable[..., Any])


def my_decorator(func: F) -> F:
    """A simple decorator that prints a message before calling the decorated function.

    This decorator wraps a function, printing a message indicating the function that is about to be called.
    After printing the message, it proceeds to call the original function with the provided arguments and
    keyword arguments, returning the result.

    Parameters:
    func : F
      The function to be decorated. This is the original function that will be wrapped by the decorator.

    Returns:
    F
      The wrapped function, which prints a message before calling the original function.
    """
    def wrapper(*args: Tuple[str], **kwds: Dict[str, str]) -> Any:
        """The wrapper function that is executed in place of the original function when the decorator is applied.

        This function is responsible for:
        1. Printing a message that indicates the function being called.
        2. Invoking the original function with the arguments and keyword arguments provided.
        3. Returning the result of the original function.

        Parameters:
        *args : tuple
            Positional arguments to pass to the original function.
        **kwds : dict
            Keyword arguments to pass to the original function.

        Returns:
        Any
            The result of the original function after it has been called with the provided arguments.
        """
        print("Calling", func)
        return func(*args, **kwds)
    return cast(F, wrapper)


@my_decorator
def test_persons_list() -> List[Any]:
    """Provides a sample list of person data for testing purposes.

    This fixture returns a list of tuples representing mock person data. Each tuple contains information about
    a person, including their ID, first name, last name, salary, and email. This data can be used in tests that
    require a mock dataset representing individuals in the system.

    Returns:
    list[Any]
        A list of tuples, where each tuple represents a person and contains the following elements.
    """
    return [
        (1, 'Alice', 'Brown', 60000, 'alice.brown@example.com'),
        (2, 'Charlie', 'Davis', 70000, 'charlie.davis@example.com')
    ]


@my_decorator
def test_projects_list() -> List[Any]:
    """Provides a sample list of project data for testing purposes.

    This fixture returns a list of tuples representing mock project data. Each tuple contains information about
    a project, including the project ID, project name, project aim, project budget, manager details, and a list
    of associated tasks. The tasks themselves are represented as tuples containing task details such as the task
    name, start date, due date, status, and a list of assignees. The assignee information is also stored in tuples.

    This fixture is intended to be used in tests that require a mock dataset representing projects, managers, tasks,
    and assignees.

    Returns:
    list[Any]
        A list of tuples, where each tuple represents a project and contains the following elements.
    """
    return [
        (1, 'Wind Factory Project', 'To create Wind Factory for energy self sufficiency', 500000,
            {'Bernard', 'Shaw', 111000, 'bernard.shaw@ber.com'},
            [{'Organize Tech World', '2024-01-01', '2024-03-01', 'in_progres', [
                {1, 'Alice', 'Brown', 56000, 'alice.brown@example.com'}
            ]}]),

        (2, 'Sun Energy Project', 'To create Sun Energy Factory for energy self sufficiency', 600900,
            {'Warren', 'Buffett', 121000, 'warren.buffett@buf.com'},
            [{'Create Grocery Hub', '2024-01-01', '2024-03-01', 'in_progres', [
                {2, 'Charlie', 'Davis', 58000, 'charlie.davis@example.com'}
            ]}])
    ]


def test_make_a_list(test_persons_list_: List[Any]) -> None:
    """Tests the make_a_list function to ensure it correctly processes a list of person data.

    This test checks whether the make_a_list function correctly extracts and returns a list of first names
    from the provided list of person tuples. The function is expected to return a list containing the first
    names of the persons provided in the input list.

    Parameters:
    test_persons_list_ : list[Any]
        A list of tuples representing person data, provided by the test fixture. Each tuple contains
        information about a person, including their ID, first name, last name, salary, and email.

    Returns: None : This test function does not return any value. It asserts that the result of the make_a_list function
    matches the expected output.
    """
    result = func_to_test.make_a_list(test_persons_list_)
    assert result == ['Alice', 'Charlie']


def test_find_project_id(test_projects_list_: List[Any]) -> None:
    """Tests the find_project_id function to ensure it correctly identifies the project ID for a given project name.

    This test checks whether the find_project_id function correctly returns the ID of a project when provided
    with a list of project data and a specific project name. The function is expected to search through the list
    and return the ID associated with the specified project name.

    Parameters:
    test_projects_list_ : list[Any]
        A list of tuples representing project data, provided by the test fixture. Each tuple contains
        information about a project, including the project ID, name, aim, budget, manager details, and associated tasks.

    Returns: None : This test function does not return any value. It asserts that the result of the find_project_id
    function matches the expected project ID.
    """
    result = func_to_test.find_project_id(test_projects_list_, 'Wind Factory Project')
    assert result == 1


def test_make_assignees_list(test_persons_list_: List[Any]) -> None:
    """Tests the make_assignees_list function to ensure it correctly processes a list of person data.

    This test checks whether the make_assignees_list function correctly combines the first and last names
    of persons in the provided list and returns them as a list of full names. The function is expected to
    return a list containing the full names of the persons provided in the input list.

    Parameters:
    test_persons_list_ : list[Any]
        A list of tuples representing person data, provided by the test fixture. Each tuple contains
        information about a person, including their ID, first name, last name, salary, and email.

    Returns: None : This test function does not return any value. It asserts that the result of the make_assignees_list
    function matches the expected output, which is a list of full names in the format 'First Last'.
    """
    result = func_to_test.make_assignees_list(test_persons_list_)
    assert result == ['Alice Brown', 'Charlie Davis']


def test_find_person_id(test_persons_list_: List[Any]) -> None:
    """Tests the find_person_id function to ensure it correctly identifies the person ID for a given full name.

    This test checks whether the find_person_id function correctly returns the ID of a person when provided
    with a list of person data and a specific full name (first name and last name combined). The function is expected
    to search through the list and return the ID associated with the specified full name.

    Parameters:
    test_persons_list_ : list[Any]
        A list of tuples representing person data, provided by the test fixture. Each tuple contains
        information about a person, including their ID, first name, last name, salary, and email.

    Returns: None : This test function does not return any value. It asserts that the result of the find_person_id
    function matches the expected person ID.
    """
    result = func_to_test.find_person_id(test_persons_list_, 'Alice Brown')
    assert result == 1
