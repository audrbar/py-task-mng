"""Sets up the connection and session management class."""
import os
from typing import Any

from dotenv import load_dotenv  # type: ignore
from sqlalchemy import create_engine, URL, exc  # type: ignore
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base, Session  # type: ignore


class DBEngine:
    """Sets up the connection and session management class."""
    def __init__(self) -> None:
        try:
            # Load environment variables
            load_dotenv()

            # Retrieve database connection details
            database_url = URL.create(
                    "postgresql+psycopg2",
                    database=os.getenv('dbname'),
                    username=os.getenv('user'),
                    password=os.getenv('password'),
                    host=os.getenv('host'),
                    port=os.getenv('port')
            )

            # Create the engine with connection pooling
            self.engine = create_engine(
                database_url,
                echo=True,  # Set to True if you need to debug SQL queries
                pool_size=10,  # Adjust based on your expected load
                max_overflow=20,  # Allows for additional connections beyond pool_size
                pool_pre_ping=True,  # Ensures connections are alive
                pool_recycle=1800  # Recycle connections after 30 minutes
            )

            # Base class for ORM models
            self.Base = declarative_base()

            # Session factory using scoped_session for thread-safe sessions
            self.Session = scoped_session(sessionmaker(
                    autoflush=False,
                    autocommit=False,
                    bind=self.engine
                ))

            # Add query property to Base class
            self.Base.query = self.Session.query_property()
            print("Database engine initialized successfully.")

        except exc.SQLAlchemyError as e:
            print(f"Error initializing the database engine: {e}")
            raise

    def get_session(self) -> Session | Session:
        """Get a new session instance from the scoped session factory.

        Returns: session: A new SQLAlchemy session instance.
        """
        try:
            return self.Session()
        except exc.SQLAlchemyError as e:
            print(f"Error getting a new session: {e}")
            raise

    def get_base(self) -> Any:
        """Get the declarative base class for defining ORM models.

        Returns: Base: The SQLAlchemy declarative base class.
        """
        return self.Base

    def close_session(self) -> None:
        """Closes the scoped session."""
        try:
            self.Session.remove()
            print("Session closed successfully.")
        except exc.SQLAlchemyError as e:
            print(f"Error closing the session: {e}")
            raise
