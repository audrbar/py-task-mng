from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Relationship

from src.base import TimeStampedModel


class Person(TimeStampedModel):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    salary = Column(Float, nullable=False)
    email = Column(String(80), nullable=False, unique=True)

    # one person to one project
    project = Relationship("Project", back_populates="person", uselist=False, passive_deletes=False)
    # many users to many tasks
    tasks = Relationship("Task", secondary="person_tasks", back_populates="persons", passive_deletes=True)

    def __repr__(self):
        return (f"{self.__class__.__name__}, id: {self.id}, full name: {self.firstname} {self.lastname}, "
                f"salary: {self.salary}, email: {self.email}")
