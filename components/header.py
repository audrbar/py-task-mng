"""
This File Holds Components of the Streamlit page.
"""
import streamlit as st
import streamlit_lottie as lto
import requests
from datetime import datetime


def header_section(section_title, section_description, divider="gray") -> None:
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
