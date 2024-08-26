"""Tests to test DB connection."""
import unittest
from typing import Any
from unittest.mock import MagicMock, patch

from src.db_connection import DBEngine


class TestDBEngine(unittest.TestCase):
    """Unit tests for the DBEngine class, which manages the database connection and session handling.

    This test class uses the unittest framework and mocks to verify that the DBEngine class
    correctly initializes the database engine, creates sessions, and closes sessions. The tests
    are designed to ensure that the DBEngine class behaves as expected in various scenarios.
    """
    @patch('src.db_connection.create_engine')
    @patch('src.db_connection.load_dotenv')
    def test_db_engine_init(self, mock_load_dotenv: object, mock_url_create: Any, mock_create_engine: Any) -> None:
        """Test the initialization of the DBEngine class.

        This test verifies that the DBEngine class correctly initializes the database engine and
        session factory. It mocks the environment variable loading and the SQLAlchemy engine creation
        to ensure that the correct parameters are used and that the necessary components (Base and Session)
        are set up correctly.

        Parameters:
        mock_load_dotenv : unittest.mock.MagicMock
            A mock object that simulates the behavior of the load_dotenv function, ensuring that environment
            variables are loaded without side effects.
        mock_url_create : unittest.mock.MagicMock
            A mock object that simulates the behavior of the URL.create function, ensuring that the correct
            database URL is generated and used during engine creation.
        mock_create_engine : unittest.mock.MagicMock
            A mock object that simulates the behavior of the SQLAlchemy create_engine function, ensuring that
            the engine is created with the correct configuration.

        Asserts:
        - Ensures that load_dotenv is called once to load environment variables.
        - Ensures that create_engine is called once to create the SQLAlchemy engine.
        - Ensures that the DBEngine.Base and DBEngine.Session are initialized correctly.
        """
        # Mock the environment variables
        mock_load_dotenv.return_value = None
        mock_create_engine.return_value = MagicMock()

        # Initialize DBEngine
        db_engine = DBEngine()

        # Check if the engine was created with the correct URL
        mock_url_create.assert_called_once_with(
            "postgresql+psycopg2",
            database='dbname',
            username='user',
            password='pass',
            host='localhost',
            port=None
        )
        mock_create_engine.assert_called_once()

        # Ensure the Base and Session are set up correctly
        self.assertIsNotNone(db_engine.Base)
        self.assertIsNotNone(db_engine.Session)

    @patch('src.db_connection.scoped_session')
    def test_get_session(self, mock_scoped_session: Any) -> Any:
        """Test the get_session method of the DBEngine class.

        This test verifies that the get_session method returns a new SQLAlchemy session. It mocks
        the scoped_session function to ensure that a session is returned correctly when requested.

        Parameters:
        mock_scoped_session : unittest.mock.MagicMock
            A mock object that simulates the behavior of the SQLAlchemy scoped_session function, ensuring that
            a session is created and returned as expected.

        Asserts:
        - Ensures that get_session returns the mocked session object.
        - Ensures that the session returned by get_session matches the mock session.
        """
        # Mock the session creation
        mock_session = MagicMock()
        mock_scoped_session.return_value = mock_session

        # Initialize DBEngine and get a session
        db_engine = DBEngine()
        session = db_engine.get_session()

        # Check if the session is returned
        self.assertEqual(session, mock_session)

    @patch('src.db_connection.scoped_session')
    def test_close_session(self, mock_scoped_session: Any) -> None:
        """Test the close_session method of the DBEngine class.

        This test verifies that the close_session method correctly closes the current session.
        It mocks the scoped_session function to ensure that the session's remove method is called
        to close the session.

        Parameters:
        mock_scoped_session : unittest.mock.MagicMock
            A mock object that simulates the behavior of the SQLAlchemy scoped_session function, ensuring that
            the session removal is handled correctly.

        Asserts:
        - Ensures that the session's remove method is called once to close the session.
        """
        # Mock the session removal
        mock_session_remove = MagicMock()
        mock_scoped_session.return_value.remove = mock_session_remove

        # Initialize DBEngine and close the session
        db_engine = DBEngine()
        db_engine.close_session()

        # Check if the session removal was called
        mock_session_remove.assert_called_once()


if __name__ == '__main__':
    unittest.main()
