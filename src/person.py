class Person:
    def __init__(self, person_id: str, person_name: str, person_surname: str, person_email: str):
        self.person_id = person_id
        self.person_name = person_name
        self.person_surname = person_surname
        self.person_fullname = f"{person_name} {person_surname}"
        self.person_email = person_email
