class Task:
    def __init__(self, task_id: str, task_name: str, start_date: str, due_date: str, status='pending'):
        self.task_id = task_id
        self.task_name = task_name
        self.start_date = start_date
        self.due_date = due_date
        self.status = status
        self.tasks = []
        self.assignees = []
        self.tasks.append(self)
        print(f"Success. Task {self.task_name} was created.")

    def add_assignee(self, assignee):
        self.assignees.append(assignee)
        print(f"Success. Assignee {assignee} to the task {self.task_id} was added.")

    def get_task_details(self):
        return (f"Task {self.task_id}, {self.task_name}, {self.start_date}, {self.due_date}, {self.status},"
                f" {self.assignees}")

    def get_tasks(self):
        for task in self.tasks:
            return f"Task: {task.task_id}, {task.task_name}, {task.status}, {task.assignees}."
