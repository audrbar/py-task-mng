from manager import Manager
from task import Task


class Project:
    def __init__(self, project_id: str, project_name: str, project_aim: str, project_budget: int,
                 *task: Task, **manager: Manager):
        self.project_id = project_id
        self.project_name = project_name
        self.project_aim = project_aim
        self.project_budget = project_budget
        self.task = task
        self.tasks = []
        self.manager = manager
        self.projects = []

    def add_manager(self, manager):
        self.manager = manager
        print(f"The manager {self.manager} was assigned.")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"The task {self.task} was added.")

    def get_projects(self, projects):
        if len(projects) > 1:
            return f"Project {self.project_name}, {self.project_budget}."
        else:
            for project in self.projects:
                return f"Project {project.project_name}, {project.project_budget}.\n"

    def get_project_details(self):
        return (f"Project {self.project_id}, {self.project_name}, {self.project_aim}, {self.project_budget}, "
                f"{self.manager.__str__()}, {self.task}, {self.tasks}.")
