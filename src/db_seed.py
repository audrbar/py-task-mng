"""Deletes, Creates Database Tables and Feeds them with Dummy Data for Testing Purposes."""
from typing import Any

from sqlalchemy.exc import IntegrityError

from src.base import db_engine, session, Model
from src.models import Project, Task, Assignee, Manager
from src.dummy_data import projects_list_full


def drop_tables() -> None:
    """Drops all tables in the database, specifically targeting the 'projects' table and its dependent objects.

    This function first reflects the existing database schema into SQLAlchemy's
    `Model.metadata`, allowing it to work with the current state of the database.
    It then calls `Model.metadata.drop_all()` to drop all tables that are part of the current SQLAlchemy
    model metadata.

    If any errors occur during the process, the function will roll back the current transaction
    to ensure the database remains in a consistent state.

    Finally, the database session is closed to free up resources.

    Exceptions: If an error occurs during the dropping of the 'projects' table, an error message
    is printed, and the transaction is rolled back to maintain database integrity.

    Notes:
    - This function should be used with caution, as it will irreversibly drop the
      'projects' table along with all its dependent objects.
    - Ensure that you have backups or are working in a development environment before
      running this function.
    """
    try:
        db_engine.close_session()
        Model.metadata.drop_all(db_engine.engine)
        print("Success. All tables where dropped")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        db_engine.close_session()


def create_database() -> None:
    """Creates all tables in the database according to the SQLAlchemy models defined in the metadata.

    This function uses the SQLAlchemy `Model.metadata.create_all()` method to create all
    tables that are part of the current model's metadata. If the tables already exist,
    they will not be recreated, making this method safe to run multiple times.

    The function is typically used to set up the database schema at the start of an application
    or during a deployment process, ensuring that all necessary tables are created according to
    the defined SQLAlchemy models.

    Notes:
    - This function should be run after the database connection has been established and
      the models have been defined.
    - If there are any changes to the models, running this function again will not update
      the schema; migrations are required for schema updates.
    """
    Model.metadata.create_all(db_engine.engine)


def seed_database(projects_data: list[dict[str, Any]]) -> None:
    """Populates the database with initial data for projects, managers, tasks, and assignees.

    This function iterates over a predefined list of project data and populates the database with `Manager`,
    `Project`, `Task`, and `Assignee` records. It ensures that existing managers and assignees are not duplicated
    by checking their presence based on the email field. The function also manages the associations between
    projects, tasks, and assignees.
    Process:
    1. For each project in `projects_data`:
        - Check if the manager exists in the database by email. If not, create and add the manager.
        - Create the project and associate it with the manager.
        - For each task in the project:
            - Create the task and associate it with the project.
            - For each assignee in the task:
                - Check if the assignee exists in the database by email. If not, create and add the assignee.
                - Associate the task with the assignee.

    2. Commit the session after adding each project and its associated tasks and assignees.
    Error Handling: - If an `IntegrityError` occurs (e.g., due to unique constraint violations), the transaction is
    rolled back,  and an error message is printed.
    Finalization: - The database session is closed in the `finally` block to ensure that resources are properly
    released.

    Notes:
    - This function assumes that the database schema has already been created (e.g., using `create_database()`).
    - Be cautious when running this function multiple times as it may lead to data duplication if not properly handled.
    - The function commits changes incrementally to avoid holding open transactions for too long, which could
      lead to locks or other performance issues.
    """
    try:
        for project_data in projects_data:
            # Create or get the Manager object
            manager = session.query(Manager).filter_by(email=project_data['manager']['email']).first()
            if not manager:
                manager = Manager(
                    firstname=project_data['manager']['firstname'],
                    lastname=project_data['manager']['lastname'],
                    salary=project_data['manager']['salary'],
                    email=project_data['manager']['email']
                )
                session.add(manager)
                session.commit()

            # Create the Project object
            project = Project(
                project_name=project_data['project_name'],
                project_aim=project_data['project_aim'],
                project_budget=project_data['project_budget'],
                manager=manager
            )
            session.add(project)

            for task_data in project_data['tasks']:
                # Create the Task object
                task = Task(
                    task_name=task_data['task_name'],
                    start_date=task_data['start_date'],
                    due_date=task_data['due_date'],
                    status=task_data['status'],
                    project=project
                )
                session.add(task)

                # Associate Assignees with the Task
                for assignee_data in task_data['assignees']:
                    assignee = session.query(Assignee).filter_by(email=assignee_data['email']).first()
                    if not assignee:
                        assignee = Assignee(
                            firstname=assignee_data['firstname'],
                            lastname=assignee_data['lastname'],
                            salary=assignee_data['salary'],
                            email=assignee_data['email']
                        )
                        session.add(assignee)
                        session.commit()  # Commit the new Assignee to generate its ID

                    # Associate the Task with the Assignee
                    task.assignees.append(assignee)

            session.commit()

    except IntegrityError as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        db_engine.close_session()


def main() -> None:
    """Displays a menu to the user for executing various database management functions.

    This function presents the user with a menu of options to manage the database. The user
    can choose to drop all tables, create database tables as defined by the models, seed
    the database with dummy data, or simply exit the program. Based on the user's choice,
    the corresponding function is executed.

    Menu Options:
    1. Drop all tables in the database:
       - Calls the `drop_tables()` function to drop all existing tables in the database.
         This is typically used for resetting the database to a clean state.
    2. Create database tables as defined by the models:
       - Calls the `create_database()` function to create the necessary tables based on
         the current SQLAlchemy models. This step is essential for setting up the schema.
    3. Seed database with dummy data:
       - Calls the `seed_database()` function to populate the database with initial dummy data.
         This is useful for testing and development purposes.
    4. Exit the program:
       - Calls `db_engine.close_session()` to close the database session and exits the program
         without making any changes to the database.

    User Input: The user is prompted to enter their choice (1, 2, 3, or 4). The input is then evaluated,
      and the corresponding function is executed.

    Notes: The function provides a simple interface for performing common database operations,
      making it easier for developers or users to manage the database during development
      or testing phases.

    Based on the input, the appropriate action is taken.
    """
    print('\nPlease select function your intended to execute:\n'
          '1. Drop all tables in database.\n'
          '2. Create database tables Model provides.\n'
          '3. Seed database with dummy data.\n'
          '4. Just exit.'
          )
    use_choice = input('\nYour choice: ', )
    if use_choice == '1':
        drop_tables()
    elif use_choice == '2':
        create_database()
    elif use_choice == '3':
        seed_database(projects_list_full)
    else:
        db_engine.close_session()


if __name__ == "__main__":
    main()
