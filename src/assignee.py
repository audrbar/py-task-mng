from person import Person


class Assignee(Person):
    def __init__(self, person_name: str, person_surname: str, person_email: str):
        super().__init__(person_name, person_surname, person_email)
        self.assignees = []
        self.assignees.append(self)
        print(f"Success. Assignee {self.person_fullname} was created.")

    def get_assignees(self):
        for manager in self.assignees:
            return f"\nAssignee {manager.person_fullname}, {manager.person_email}, (Id: {manager.person_id})."
