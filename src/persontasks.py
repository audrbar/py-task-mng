from sqlalchemy import Column, Integer, ForeignKey

from src.base import TimeStampedModel


class PersonTask(TimeStampedModel):
    __tablename__ = "person_tasks"

    person_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, person_id: {self.person_id}, task_id: {self.task_id}"
