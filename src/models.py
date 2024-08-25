"""
Data Model for Entire App.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import Relationship

from src.base import TimeStampedModel, PersonModel


class Project(TimeStampedModel):
    __tablename__ = "projects"

    project_name = Column(String(80), nullable=False)
    project_aim = Column(String(80), nullable=False)
    project_budget = Column(Float, nullable=False)

    # One-to-one relationship with Manager
    manager_id = Column(Integer, ForeignKey('managers.id', ondelete='CASCADE'), unique=True, nullable=False)
    manager = Relationship("Manager", back_populates="project", uselist=False, single_parent=True)

    # One-to-many relationship with Tasks
    tasks = Relationship("Task", back_populates="project", cascade="all, delete-orphan", passive_deletes=True)

    def __repr__(self):
        return f"<Project(name={self.project_name}, budget={self.project_budget})>"


class Manager(PersonModel):
    __tablename__ = "managers"

    # One-to-one relationship with Project
    project = Relationship("Project", back_populates="manager", cascade="all, delete-orphan", uselist=False)

    def __repr__(self):
        return (f"<Manager(firstname={self.firstname}, lastname={self.lastname}, salary={self.salary}, "
                f"email={self.email})>")


class Assignee(PersonModel):
    __tablename__ = "assignees"

    # Many-to-many relationship with Tasks
    tasks = Relationship("Task", secondary="assignee_tasks", back_populates="assignees", cascade="all, delete")

    def __repr__(self):
        return (f"<Assignee(firstname={self.firstname}, lastname={self.lastname}, salary={self.salary}, "
                f"email={self.email}, tasks={len(self.tasks)})>")


class Task(TimeStampedModel):
    __tablename__ = "tasks"

    task_name = Column(String(80), nullable=False)
    start_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    done_date = Column(Date, nullable=True)
    status = Column(String(80), nullable=False)

    # Many-to-one relationship with Project
    project_id = Column(Integer, ForeignKey("projects.id", ondelete='CASCADE'), nullable=False, index=True)
    project = Relationship("Project", back_populates="tasks")

    # Many-to-many relationship with Assignees
    assignees = Relationship("Assignee", secondary="assignee_tasks", back_populates="tasks",
                             cascade="all, delete")

    def __repr__(self):
        return f"<Task(id={self.id}, name={self.task_name})>"


class AssigneeTask(TimeStampedModel):
    __tablename__ = "assignee_tasks"

    assignee_id = Column(Integer, ForeignKey("assignees.id", ondelete="CASCADE"), primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True)

    def __repr__(self):
        return f"<AssigneeTask(assignee_id={self.assignee_id}, task_id={self.task_id})>"
