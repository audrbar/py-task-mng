from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import Relationship

from src.base import TimeStampedModel


class Project(TimeStampedModel):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(80), nullable=False)
    project_aim = Column(String(80), nullable=False)
    project_budget = Column(Float, nullable=False)
    person_id = Column(Integer, ForeignKey("persons.id"), nullable=True, index=True)

    # one person to one project
    person = Relationship("Person", back_populates="project")
    # one project to many tasks
    tasks = Relationship("Task", back_populates="project", passive_deletes=False)

    def __repr__(self):
        return (f"{self.__class__.__name__}, id: {self.id}, name: {self.project_name}, aim: {self.project_aim}, "
                f"budget: {self.project_budget}")
