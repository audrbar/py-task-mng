from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_base

from src.db_conn import DBEngine

"""
This code snippet sets up the base model class and session management for an SQLAlchemy ORM setup.

Attributes:
    Model (Base): The declarative base class for all ORM models, with should inherit from this base class.
    db_engine (DBEngine): An instance of the DBEngine class, which handles the connection to the database 
    and session creation.
    session (scoped_session): A scoped session object created from the DBEngine instance, providing thread-safe 
    session handling.
    Model.query (Query): A SQLAlchemy query property attached to the `Model` base class. This allows for querying 
    directly on model classes (e.g., `User.query.all()`) when using Flask-SQLAlchemy-like syntax.
"""
Model = declarative_base()
db_engine = DBEngine()
session = db_engine.Session
Model.query = session.query_property()


class TimeStampedModel(Model):
    """
    An abstract base class model that provides self-updating 'created_at' and 'updated_at' fields.

    Attributes:
        created_at (DateTime): Stores the timestamp when the record was created.
            Automatically set to the current date and time when the record is created.
        updated_at (DateTime): Stores the timestamp when the record was last updated.
            Automatically updated to the current date and time whenever the record is updated.
    """
    __abstract__ = True
    __allow_unmapped__ = True

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
