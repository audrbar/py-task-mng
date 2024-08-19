from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import Relationship

from models.base import TimeStampedModel


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
