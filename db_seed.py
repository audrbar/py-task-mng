from src.base import db_engine, session, Model
from src.person import Person
from src.project import Project
from src.task import Task
from models.persontasks import PersonTask
from dummy_data import persons_list, projects_list, tasks_list, person_tasks_list


def session_add(data_list: list[dict], class_name: type, conn_session: session) -> None:
    """
    Adds a list of data to the database using SQLAlchemy.

    :param data_list: List of dictionaries where each dictionary contains data for one record.
    :param class_name: The SQLAlchemy model class to instantiate with the data.
    :param conn_session: The SQLAlchemy session object to use for database operations.
    """
    try:
        for item in data_list:
            # Create an instance of class_name with the data and add it to the session
            conn_session.add(class_name(**item))
        conn_session.commit()
    except Exception as ex:
        session.rollback()  # Roll back the session in case of an error
        raise ex


def get_all_query(class_name: type, conn_session: session) -> list | None:
    """
    Fetches and returns all records of the given SQLAlchemy model class.

    :param class_name: The SQLAlchemy model class to query.
    :param conn_session: The SQLAlchemy session to use for the query (optional).
    :return: A list of all records, or None if the query fails.
    """
    try:
        results = conn_session.query(class_name).all()
        print(f"\n{class_name.__name__} table contains ({type(results)}):")  # Print the results
        for item in results:
            print(item)
        return results
    except Exception as e:
        print(f"An error occurred while querying {class_name.__name__}: {e}")
        return None


def main():
    # Drop All Database Tables if exists
    Model.metadata.reflect(db_engine.engine)
    Model.metadata.drop_all(db_engine.engine)
    # Create Database Tables Model provides
    Model.metadata.create_all(db_engine.engine)
    # Ceed Database Tables with dummy data
    session_add(persons_list, Person, session)
    session_add(projects_list, Project, session)
    session_add(tasks_list, Task, session)
    session_add(person_tasks_list, PersonTask, session)
    # Check if Database fed successfully
    get_all_query(Person, session)
    get_all_query(Project, session)
    get_all_query(Task, session)
    get_all_query(PersonTask, session)


if __name__ == "__main__":
    main()
