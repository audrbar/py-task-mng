"""Panda Dataframe test."""
import pytest
import pandas as pd
from typing import List, TypeVar, Callable, Any, cast, Tuple, Dict
from src.models import Manager
from utils.utilities import managers_to_df


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


class MockProject:
    """A mock class representing a Project for testing purposes.

    The MockProject class is used to simulate a simple project object, primarily for use in testing scenarios.
    It contains only one attribute, `project_name`, which represents the name of the project. This mock class
    can be useful when testing functions or components that require a project-like object but do not need the
    full complexity of an actual Project model.

    Attributes:
    project_name : str
        The name of the project.

    Methods:
    __init__(self, project_name: str) -> None
        Initializes the MockProject with a given project name.
    """

    def __init__(self, project_name: str) -> None:
        self.project_name = project_name


class MockManager:
    """Initializes the MockManager instance with the specified attributes.

    Parameters:
    _id : int
        The unique identifier of the manager.
    firstname : str
        The first name of the manager.
    lastname : str
        The last name of the manager.
    salary : float
        The salary of the manager.
    email : str
        The email address of the manager.
    project : Optional[Any], default=None
        An optional attribute representing the project managed by this manager. If not provided,
        the manager will have no associated project.
    """

    def __init__(
            self, _id: int, firstname: str, lastname: str, salary: float, email: str,
            project: object = None
    ) -> None:
        self._id = id
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = email
        self.project = project


@my_decorator
def mock_managers() -> List[Manager]:
    """Provides a sample list of mock Manager objects for testing purposes.

    This fixture returns a list of `Manager` objects, each representing a manager with basic attributes
    such as first name, last name, salary, and email. These mock objects are useful for testing functions
    or components that interact with manager data, allowing tests to be performed without the need for
    actual database records.

    Returns:
    list[Manager]
        A list of mock `Manager` objects, each initialized with sample data.
    """
    return [
        Manager(firstname="John", lastname="Doe", salary=50000, email="john.doe@example.com"),
        Manager(firstname="Jane", lastname="Smith", salary=60000, email="jane.smith@example.com")
    ]


def test_managers_to_df(mock_managers: List[Manager]) -> None:
    """Tests the managers_to_df function to ensure it correctly converts a list of Manager objects into a DataFrame.

    This test checks whether the managers_to_df function correctly processes a list of Manager objects and
    converts it into a pandas DataFrame. The resulting DataFrame should have columns for "Full name", "Salary",
    and "Email", and the data in these columns should match the expected output.

    Parameters:
    mock_managers : list[Manager]
        A list of mock Manager objects provided by the fixture. Each Manager object contains attributes such as
        first name, last name, salary, and email.

    Returns: None : This test function does not return any value. It asserts that the DataFrame produced by
    the managers_to_df function matches the expected DataFrame.
    """
    expected_data = {
        "Full name": ["John Doe", "Jane Smith"],
        "Salary": [50000, 60000],
        "Email": ["john.doe@example.com", "jane.smith@example.com"]
    }
    expected_df = pd.DataFrame(expected_data)
    result_df = managers_to_df(mock_managers)
    print('Expected: ', expected_df)
    print('Result', result_df)
    pd.testing.assert_frame_equal(result_df, expected_df)
