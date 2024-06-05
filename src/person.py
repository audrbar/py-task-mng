import uuid


class Person:
    def __init__(self, person_name: str, person_surname: str, person_email: str):
        self.person_id = uuid.uuid4()
        self.person_name = person_name
        self.person_surname = person_surname
        self.person_fullname = f"{person_name} {person_surname}"
        self.person_email = person_email

    def get_person_details(self):
        return f"Details: {self.person_fullname}, {self.person_email}, (Id: {self.person_id})."
