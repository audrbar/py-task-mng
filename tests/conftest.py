"""Fixtures for tests."""
import pytest
from src.models import Assignee, Project, Manager, Task


@pytest.fixture
def test_assignees_list() -> list[Assignee]:
    """Provides a sample list of person data for testing purposes.

    This fixture returns a list of tuples representing mock person data. Each tuple contains information about
    a person, including their ID, first name, last name, salary, and email. This data can be used in tests that
    require a mock dataset representing individuals in the system.

    Returns:
    list[Assignee]
        A list of tuples, where each tuple represents a person and contains the following elements.
    """
    return [
        Assignee(id=1, firstname='Alice', lastname='Brown', salary=56000, email='alice.brown@example.com'),
        Assignee(id=2, firstname='Charlie', lastname='Davis', salary=70000, email='charlie.davis@example.com')
    ]


@pytest.fixture
def test_projects_list() -> list[Project]:
    """Provides a sample list of project data for testing purposes.

    This fixture returns a list of tuples representing mock project data. Each tuple contains information about
    a project, including the project ID, project name, project aim, project budget, manager details, and a list
    of associated tasks. The tasks themselves are represented as tuples containing task details such as the task
    name, start date, due date, status, and a list of assignees. The assignee information is also stored in tuples.

    This fixture is intended to be used in tests that require a mock dataset representing projects, managers, tasks,
    and assignees.

    Returns:
    list[Project]
        A list of tuples, where each tuple represents a project and contains the following elements.
    """
    return [
        Project(id=1, project_name='Wind Factory Project', project_budget=500000,
                project_aim='To create Wind Factory for energy self sufficiency',
                manager=Manager(id=1, firstname='Bernard', lastname='Shaw', salary=111000,
                                email='bernard.shaw@ber.com'),
                tasks=[Task(id=1, task_name='Organize Tech World', start_date='2024-01-01',
                            due_date='2024-03-01', status='in_progres')]),

        Project(id=2, project_name='Sun Energy Project', project_budget=600900,
                project_aim='To create Sun Energy Factory for energy self sufficiency',
                manager=Manager(id=2, firstname='Warren', lastname='Buffett', salary=121000,
                                email='warren.buffett@buf.com'),
                tasks=[Task(id=2, task_name='Create Grocery Hub', start_date='2024-01-01',
                            due_date='2024-03-01', status='in_progres')]),
    ]
