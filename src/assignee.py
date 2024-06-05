from person import Person


class Assignee(Person):
    assignees = []

    def __init__(self, person_name: str, person_surname: str, person_email: str):
        super().__init__(person_name, person_surname, person_email)
        Assignee.assignees.append(self)
        print(f"Success. Assignee {self.person_fullname} was created.")

    def get_assignees(self):
        print(f"The assignees available: {Assignee.assignees}.")
        for assignee in Assignee.assignees:
            return f"\nAssignee {assignee.person_fullname}, {assignee.person_email}, (Id: {assignee.person_id})."
