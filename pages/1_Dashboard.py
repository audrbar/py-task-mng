import streamlit as st
import streamlit_lottie as lto
import requests
from Home import footer_section
from components.header import header_section
from datetime import datetime
from src.base import db_engine, Model
from src.person import Person
from src.project import Project
from src.task import Task
from src.persontasks import PersonTask


def metrics_section() -> None:
    with st.container():
        st.divider()
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Įgyvendinama projektų", "3", "1")
        col2.metric("Vykdoma užduočių", "12", "-1")
        col3.metric("Atlikta užduočių", "9", "2")
        col4.metric("Žmogiškieji ištekliai", "15", "-1")


def main():
    section_title = "Dashboard"
    section_description = ("Team Workflow Manager is a comprehensive tool designed to streamline the management of "
                           "projects, including tracking tasks, managing budgets, and coordinating team activities. "
                           "The application provides a user-friendly interface for project managers and team members "
                           "to collaborate efficiently and effectively.")
    header_section(section_title, section_description)
    metrics_section()
    footer_section()


if __name__ == "__main__":
    main()