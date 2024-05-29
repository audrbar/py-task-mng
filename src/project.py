from manager import Manager


class Project:
    def __init__(self, project_id: str, project_name: str, project_aim: str, project_budget: int, manager: Manager):
        self.project_id = project_id
        self.project_name = project_name
        self.project_aim = project_aim
        self.project_budget = project_budget
        self.manager = manager

    def get_project_details(self):
        return (f"Person {self.project_id}, {self.project_name}, {self.project_aim}, {self.project_budget}, "
                f"{self.manager}")
