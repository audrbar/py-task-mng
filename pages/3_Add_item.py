from Home import footer_section
from components.add_section import new_item_section
from models.base import db_engine
from src.utilities import *


def main():
    header_section("Insert New Item", "Insert any new item - project, task, person - "
                                      "to the system and provide the item details accordingly.")
    session = db_engine.Session
    new_item_section(session)
    footer_section()


if __name__ == "__main__":
    main()
