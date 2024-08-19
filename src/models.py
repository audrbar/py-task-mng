from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import Relationship

from models.base import TimeStampedModel, Model


class Person(TimeStampedModel):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    salary = Column(Float, nullable=False)
    email = Column(String(320), nullable=False, unique=True)

    # one person to one project
    project = Relationship("Project", back_populates="person", uselist=False, passive_deletes=False)
    # many users to many tasks
    tasks = Relationship("Task", secondary="person_tasks", back_populates="persons", passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.firstname} {self.lastname}"


class Project(TimeStampedModel):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(80), nullable=False)
    project_aim = Column(String(80), nullable=False)
    project_budget = Column(Float, nullable=False)
    person_id = Column(Integer, ForeignKey("persons.id"), nullable=True, index=True, unique=True)

    # one person to one project
    person = Relationship("Person", back_populates="project")
    # one project to many tasks
    tasks = Relationship("Task", back_populates="project", passive_deletes=False)  # one to many tasks

    def __repr__(self):
        return f"<Project({self.id}, name: {self.project_name})>"


class Task(TimeStampedModel):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String(80), nullable=False)
    start_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    done_date = Column(Date, nullable=True)
    status = Column(String(80), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False, index=True)  # one to many tasks

    # many tasks to many users
    persons = Relationship("Person", secondary="person_tasks", back_populates="tasks", passive_deletes=True)
    # one project to many tasks
    project = Relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, name: {self.task_name})>"


class PersonTask(TimeStampedModel):
    __tablename__ = "person_tasks"

    person_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True)
