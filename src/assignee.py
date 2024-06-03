from person import Person


class Assignee(Person):
    def __init__(self, person_id: str, person_name: str, person_surname: str, person_email: str):
        self.assignees = []
        super().__init__(person_id, person_name, person_surname, person_email)
        self.person_id = person_id
        self.person_name = person_name
        self.person_surname = person_surname
        self.person_fullname = f"{person_name} {person_surname}"
        self.person_email = person_email
        self.assignees.append(self)

    def get_assignee_details(self):
        return f"Assignee {self.person_id}, {self.person_fullname}, {self.person_email}."
