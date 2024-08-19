from Home import footer_section
from components.edit_section import edit_section
from models.base import db_engine
from src.utilities import *


def main():
    header_section("Edit Items", "Edit different aspects of your projects and choose for "
                                 "that the tab accordingly and check the results write above.")
    session = db_engine.Session
    edit_section(session)
    footer_section()


if __name__ == "__main__":
    main()
