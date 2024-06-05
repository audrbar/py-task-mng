from task import Task
from manager import Manager


class Project:
    tasks = []
    managers = []

    def __init__(self, project_id: str, project_name: str, project_aim: str, project_budget: int, *task: Task,
                 **manager: Manager):
        self.project_id = project_id
        self.project_name = project_name
        self.project_aim = project_aim
        self.project_budget = project_budget
        self.manager = manager
        self.task = task
        print(f"Success. Project {self.project_name} was created.")

    def add_manager(self, manager):
        Project.managers.append(manager)
        print(f"The manager {manager} was to the project {self.project_id} assigned.")

    def add_task(self, task):
        Project.tasks.append(task)
        print(f"The task {task} was to the project {self.project_id} added.")

    def get_project_tasks(self):
        for task in Project.tasks:
            return f"{task.__dict__}"

    def get_project_managers(self):
        for manager in Project.managers:
            return f"{manager.__dict__}"

    def get_project_details(self):
        return (f"-------------\nProject Id {self.project_id}\nName: {self.project_name}\nAim: {self.project_aim}\n"
                f"Budget: {self.project_budget}\nManager: {self.get_project_managers()}\nTasks: {self.get_project_tasks()}.")
