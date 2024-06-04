class Project:
    def __init__(self, project_id: str, project_name: str, project_aim: str, project_budget: int):
        super().__init__()
        self.project_id = project_id
        self.project_name = project_name
        self.project_aim = project_aim
        self.project_budget = project_budget
        self.projects = []
        self.managers = []
        self.tasks = []
        self.projects.append(self)
        print(f"Success. Project {self.project_name} was created.")

    def add_manager(self, manager):
        self.managers.append(manager)
        print(f"The manager {manager} was to the project {self.project_id} assigned.")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"The task {task} was to the project {self.project_id} added.")

    def get_projects(self):
        for project in self.projects:
            return f"Project {project.project_name}, {project.project_budget}."

    def get_project_details(self):
        return (f"Project {self.project_id}, {self.project_name}, {self.project_aim}, {self.project_budget}, "
                f"{self.managers}, {self.tasks}.")
