from assignee import Assignee
from project import Project
from datetime import datetime


class Task:
    def __init__(self, task_id: str, task_name: str, start_date: datetime, due_date: datetime,
                 project: Project, assignee: Assignee):
        self.task_id = task_id
        self.task_name = task_name
        self.start_date = start_date
        self.due_date = due_date
        self.project = project
        self.assignee = assignee

    def get_task_details(self):
        return (f"Person {self.task_id}, {self.task_name}, {self.start_date}, {self.due_date}, "
                f"{self.project}, {self.assignee}")
