"""Sets up the base model class and session management for an SQLAlchemy ORM setup."""
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float

from src.db_connection import DBEngine

"""This code snippet sets up the base model class and session management for an SQLAlchemy ORM setup.

Attributes:
    Model (Base): The declarative base class for all ORM models, with should inherit from this base class.
    db_engine (DBEngine): An instance of the DBEngine class, which handles the connection to the database
    and session creation.
    session (scoped_session): A scoped session object created from the DBEngine instance, providing thread-safe
    session handling.
    Model.query (Query): A SQLAlchemy query property attached to the `Model` base class. This allows for querying
    directly on model classes (e.g., `User.query.all()`) when using Flask-SQLAlchemy-like syntax.
"""

db_engine = DBEngine()
session = db_engine.get_session()
Model = db_engine.get_base()


class TimeStampedModel(Model):  # type: ignore
    """An abstract base class model that provides self-updating 'created_at' and 'updated_at' fields.

    Attributes:
        created_at (DateTime): Stores the timestamp when the record was created.
            Automatically set to the current date and time when the record is created.
        updated_at (DateTime): Stores the timestamp when the record was last updated.
            Automatically updated to the current date and time whenever the record is updated.
    """
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())


class PersonModel(TimeStampedModel):
    """Abstract base class representing a person entity with common attributes.

    This class is intended to be inherited by other classes that represent specific types of persons
    (e.g., Employee, Manager) in a system. It defines common attributes such as `firstname`, `lastname`,
    `salary`, and `email`. The class is marked as abstract with `__abstract__ = True`, meaning it cannot
    be instantiated directly and should be used as a base class.

    Attributes:
    firstname : str - The first name of the person. This field is mandatory.
    lastname : str - The last name of the person. This field is mandatory.
    salary : float - The salary of the person. This field is mandatory and should be a positive float value.
    email : str - The email address of the person. This field is mandatory and must be unique within the system.
    __abstract__ : bool - A special attribute indicating that this is an abstract class, and SQLAlchemy should not
                   map it to a table.
    __allow_unmapped__ : bool - Allows for unmapped columns or attributes. This is useful in some complex inheritance
                   structures or when integrating with legacy systems.
    Inherits From: TimeStampedModel
    """
    __abstract__ = True
    __allow_unmapped__ = True

    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    salary = Column(Float, nullable=False)
    email = Column(String(80), nullable=False, unique=True)
