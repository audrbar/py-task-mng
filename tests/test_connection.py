"""Tests to test DB connection."""
import os
import unittest
from typing import Any
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError
from src.db_connection import DBEngine


class TestDBEngine(unittest.TestCase):
    """Unit tests for the DBEngine class, which manages the database connection and session handling.

    This test class uses the unittest framework along with the mock library to patch and test different components
    of the DBEngine class. The tests ensure that the DBEngine class correctly initializes the database engine,
    creates sessions, and handles errors appropriately.

    Methods:
    test_db_engine_init(self, mock_create_engine, mock_scoped_session, mock_url_create)
        Tests the initialization of the DBEngine class, ensuring that all components
        are correctly set up, including the database URL, engine, and session factory.
    test_get_session(self, mock_scoped_session)
        Tests the get_session method of the DBEngine class, verifying that a new session
        is correctly created and returned.
    test_close_session(self, mock_scoped_session)
        Tests the close_session method of the DBEngine class, ensuring that the session
        is properly removed and resources are released.
    test_db_engine_init_sqlalchemy_error(self, mock_scoped_session, mock_create_engine)
        Tests the initialization of the DBEngine class when an SQLAlchemyError is raised,
        verifying that the error is handled correctly.
    """
    @patch('src.db_connection.URL.create')
    @patch('src.db_connection.scoped_session')
    @patch('src.db_connection.create_engine')
    def test_db_engine_init(self, mock_create_engine: Any, mock_scoped_session: Any, mock_url_create: Any) -> None:
        """Test the initialization of the DBEngine class.

        This test ensures that the DBEngine class correctly initializes by:
        - Mocking the URL creation to return a predefined database URL.
        - Mocking the SQLAlchemy engine creation to return a mock engine instance.
        - Mocking the session factory to return a mock session factory.
        - Verifying that the URL creation, engine creation, and session factory setup are called with the expected
        arguments and that the DBEngine attributes are correctly assigned.
        """
        # Mock URL creation
        mock_url_create.return_value = 'postgresql+psycopg2://user:pass@localhost/dbname'

        # Mock SQLAlchemy engine creation
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        # Mock session factory
        mock_session_factory = MagicMock()
        mock_scoped_session.return_value = mock_session_factory

        # Initialize the DBEngine
        db_engine = DBEngine()

        # Assertions
        mock_url_create.assert_called_once_with(
            "postgresql+psycopg2",
            database=os.getenv('dbname'),
            username=os.getenv('user'),
            password=os.getenv('password'),
            host=os.getenv('host'),
            port=os.getenv('port')
        )

        mock_create_engine.assert_called_once_with(
            'postgresql+psycopg2://user:pass@localhost/dbname',
            echo=True,
            pool_size=10,
            max_overflow=20,
            pool_pre_ping=True,
            pool_recycle=1800
        )
        self.assertEqual(db_engine.engine, mock_engine)
        self.assertEqual(db_engine.Session, mock_session_factory)
        self.assertIsNotNone(db_engine.Base)

    @patch('src.db_connection.scoped_session')
    def test_get_session(self, mock_scoped_session: Any) -> None:
        """Test the get_session method of the DBEngine class.

        This test verifies that a new SQLAlchemy session is correctly created and returned by the get_session method.
        The test mocks the session creation process and ensures that the returned session matches the expected mock
        session.
        """
        # Mock session creation
        mock_session = MagicMock()
        mock_scoped_session.return_value = mock_session

        # Initialize DBEngine and get a session
        db_engine = DBEngine()
        session = db_engine.get_session()

        # Assertions
        self.assertEqual(session, mock_session())

    @patch('src.db_connection.scoped_session')
    def test_close_session(self, mock_scoped_session: Any) -> None:
        """Test the close_session method of the DBEngine class.

        This test ensures that the close_session method correctly removes the session and releases resources.
        The test mocks the session removal process and verifies that the remove method is called exactly once.
        """
        # Mock the session removal
        mock_session_remove = MagicMock()
        mock_scoped_session.return_value.remove = mock_session_remove

        # Initialize DBEngine and close the session
        db_engine = DBEngine()
        db_engine.close_session()

        # Assertions
        mock_session_remove.assert_called_once()

    @patch('src.db_connection.create_engine')
    def test_db_engine_init_sqlalchemy_error(self, mock_create_engine: Any) -> None:
        """Test initialization when SQLAlchemyError is raised.

        This test simulates a failure during the engine creation process by making the create_engine method raise
        an SQLAlchemyError. The test ensures that the DBEngine class correctly handles the exception and that
        the error is raised as expected.
        """
        # Mock create_engine to raise SQLAlchemyError
        mock_create_engine.side_effect = SQLAlchemyError("Initialization failed")

        # Initialize DBEngine and expect it to raise SQLAlchemyError
        with self.assertRaises(SQLAlchemyError):
            DBEngine()

        # Ensure that the error message is printed
        mock_create_engine.assert_called_once()


if __name__ == '__main__':
    unittest.main()
