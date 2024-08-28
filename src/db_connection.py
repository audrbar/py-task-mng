"""Sets up the connection and session management class."""
import os
from typing import Any

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL, exc
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base, Session


class DBEngine:
    """DBEngine is a utility class that manages the connection and session.

    This class sets up the database engine, manages sessions, and provides access to the declarative base class
    used to define ORM models.

    Attributes:
    engine : sqlalchemy.engine.Engine
        The SQLAlchemy engine instance that handles the database connection.
    Base : sqlalchemy.ext.declarative.api.Base
        The declarative base class used to define ORM models.
    Session : sqlalchemy.orm.scoping.scoped_session
        A factory for creating new SQLAlchemy session instances, scoped to the current thread.

    Methods:
    __init__() -> None
        Initializes the DBEngine instance by loading environment variables, setting up
        the database engine, and preparing the session factory.
    get_session() -> sqlalchemy.orm.session.Session
        Retrieves a new session instance from the scoped session factory.
    get_base() -> sqlalchemy.ext.declarative.api.Base
        Provides the declarative base class for defining ORM models.
    close_session() -> None
        Closes the current session, ensuring that all resources are properly released.
    """
    def __init__(self) -> None:
        """Initializes the DBEngine instance.

        This constructor loads environment variables using dotenv, creates a SQLAlchemy engine with connection
        pooling, and sets up a scoped session factory. The connection details such as the database name, username,
        password, host, and port are retrieved from the environment variables.
        """
        load_dotenv()
        database_url = URL.create(
            "postgresql+psycopg2",
            database=os.getenv('dbname'),
            username=os.getenv('user'),
            password=os.getenv('password'),
            host=os.getenv('host'),
            port=os.getenv('port')
        )
        self.engine = create_engine(
            database_url,
            echo=True,  # Set to True if you need to debug SQL queries
            pool_size=10,  # Adjust based on your expected load
            max_overflow=20,  # Allows for additional connections beyond pool_size
            pool_pre_ping=True,  # Ensures connections are alive
            pool_recycle=1800  # Recycle connections after 30 minutes
        )
        self.Base = declarative_base()
        self.Session = scoped_session(sessionmaker(
            autoflush=False,
            autocommit=False,
            bind=self.engine
        ))

    def get_session(self) -> Session | Session:
        """Retrieves a new session instance from the scoped session factory.

        This method returns a session instance that can be used to interact with the database.
        The session is scoped to the current thread.

        Returns:
        session : sqlalchemy.orm.session.Session: A new SQLAlchemy session instance.

        Raises:
        sqlalchemy.exc.SQLAlchemyError: If there is an error in creating the session.
        """
        try:
            return self.Session()
        except exc.SQLAlchemyError as e:
            print(f"Error getting a new session: {e}")
            raise

    def get_base(self) -> Any:
        """Provides the declarative base class for defining ORM models.

        This method returns the declarative base class that should be used as the base class for all ORM model classes.

        Returns:
        Base : sqlalchemy.ext.declarative.api.Base: The SQLAlchemy declarative base class.
        """
        return self.Base

    def close_session(self) -> None:
        """Provides the declarative base class for defining ORM models.

        This method returns the declarative base class that should be used as the base class for all ORM model classes.

        Returns:
        Base : sqlalchemy.ext.declarative.api.Base: The SQLAlchemy declarative base class.
        """
        try:
            self.Session.remove()
            print("Session closed successfully.")
        except exc.SQLAlchemyError as e:
            print(f"Error closing the session: {e}")
            raise
