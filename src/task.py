from assignee import Assignee


class Task:
    def __init__(self, task_id: str, task_name: str, start_date: str, due_date: str, status='pending',
                 *assignee: Assignee):
        self.task_id = task_id
        self.task_name = task_name
        self.start_date = start_date
        self.due_date = due_date
        self.status = status
        self.assignee = assignee
        self.assignees = []

    def add_assignee(self, assignee):
        self.assignees.append(assignee)
        print(f"Assignee {assignee} was added.")

    def get_task_details(self):
        return (f"Task {self.task_id}, {self.task_name}, {self.start_date}, {self.due_date}, {self.status},"
                f", {self.assignee.__repr__()}")
