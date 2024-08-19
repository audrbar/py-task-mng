"""
This File Holds Utility Functions of the Project.
"""
import streamlit as st


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


def make_a_list(source: list) -> list:
    result = []
    for item in source:
        result.append(item[1])
    return result


def find_project_id(source: list, selected_project: str) -> int:
    for item in source:
        if selected_project == item[1]:
            return item[0]


def make_persons_list(source: list) -> list:
    result = []
    for item in source:
        result.append(item[1] + ' ' + item[2])
    return result


def find_person_id(source: list, selected_person: str) -> int:
    for item in source:
        if selected_person == (item[1] + ' ' + item[2]):
            return item[0]
