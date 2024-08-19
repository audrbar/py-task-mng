import os
import pytz
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
from dotenv import load_dotenv

load_dotenv()


class DBEngine:
    """
    A class to manage the SQLAlchemy engine and session for connecting to a PostgreSQL database.

    This class is responsible for creating the engine, managing sessions, and providing utilities
    for session handling. It also includes an event listener that sets the time zone for each new
    database connection.
    """
    def __init__(self):
        """
        Initializes the DBEngine class by creating the SQLAlchemy engine and session factory.

        The engine is created using connection details provided through environment variables.
        A scoped session is initialized to manage database transactions in a thread-safe manner.
        """
        self.engine = self.create_engine()
        self.Session = self.create_session()

    @staticmethod
    def create_engine():
        """
        Creates and returns a SQLAlchemy engine for connecting to the PostgreSQL database.

        The connection parameters (database, username, password, host, port) are fetched from
        environment variables. The engine is configured with `echo=True` to output SQL statements
        executed by SQLAlchemy.
        Returns: Engine: An instance of SQLAlchemy's Engine connected to the PostgreSQL database.
        Raises: Exception: If the connection to the PostgreSQL database fails.
        """
        try:
            engine = create_engine(URL.create(
                "postgresql+psycopg2",
                database=os.getenv('dbname'),
                username=os.getenv('user'),
                password=os.getenv('password'),
                host=os.getenv('host'),
                port=os.getenv('port')
            ), echo=True)
            print("\nConnected to PostgreSQL database. Congratulations!")
        except Exception as error:
            raise Exception("Error while connecting to PostgreSQL", error)

        return engine

    def create_session(self):
        """
        Creates and returns a scoped session factory for managing database transactions.

        The session factory is configured to use the engine created during initialization and is set
        to not automatically flush or commit changes to the database.
        Returns: scoped_session: A thread-safe scoped session factory.
        """
        print("\ncreate_session method executed.")
        return scoped_session(
            sessionmaker(
                autoflush=False,
                autocommit=False,
                bind=self.engine
            )
        )

    def get_session(self):
        """
        Returns an active session from the scoped session factory.

        This method provides a session that can be used to perform database operations. The session
        is obtained from the scoped session, ensuring thread safety.
        Returns: Session: An active SQLAlchemy session.
        """
        print("\nget_session method executed.")
        return self.Session()

    def close_session(self):
        """
        Closes the current session by removing it from the scoped session registry.

        This method should be called after completing database operations to ensure that the session
        is properly cleaned up and that resources are released.
        """
        self.Session.remove()
        print("\nSession closed. That is it.")

#
# @event.listens_for(Engine, "connect")
# def event_listener(dbapi_connection, connection_record):
#     """
#     Event listener that sets session parameters when a new database connection is established.
#
#     This listener sets the time zone to 'Europe/Vilnius' for each new connection. It is executed
#     automatically whenever a connection is made using the SQLAlchemy engine.
#     Args:
#         dbapi_connection: The database API connection object.
#         connection_record: The connection record associated with the event.
#     """
#     tz = pytz.timezone('Europe/Vilnius')
#     cursor = dbapi_connection.cursor()
#     cursor.execute(f"SET TIME ZONE '{tz}'")
#     cursor.close()
#     print('Session parameters set on connection.')
