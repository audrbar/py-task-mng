"""Panda Dataframe test."""
import pandas as pd
from typing import List
from src.models import Project
from utils.utilities import projects_to_df
from tests.test_functions import test_projects_list


def test_projects_to_df(test_projects_list: List[Project]) -> None:
    """Tests the projects_to_df function to ensure it correctly converts a list of Project objects into a DataFrame.

    This test checks whether the projects_to_df function correctly processes a list of Project objects and
    converts it into a pandas DataFrame. The resulting DataFrame should have columns for "id", "Project name",
    "Project aim", "Budget", "Manager", and an optional "Tasks" column.

    Parameters:
    test_projects_list : list[Project]
        A list of Project objects provided by the fixture.

    Returns: None : This test function does not return any value. It asserts that the DataFrame produced by
    the projects_to_df function matches the expected DataFrame.
    """
    expected_data = {
        "id": [1, 2],
        "Project name": ['Wind Factory Project', 'Sun Energy Project'],
        "Project aim": ['To create Wind Factory for energy self sufficiency',
                        'To create Sun Energy Factory for energy self sufficiency'],
        "Budget": [500000, 600900],
        "Manager": ['Bernard Shaw', 'Warren Buffett'],
        "Tasks": ['Organize Tech World', 'Create Grocery Hub'],
    }
    expected_df = pd.DataFrame(expected_data)
    result_df = projects_to_df(test_projects_list)
    pd.testing.assert_frame_equal(result_df, expected_df)
