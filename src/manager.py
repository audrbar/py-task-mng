from person import Person
from organization import Organization


class Manager(Person):
    def __init__(self, person_id: str, person_name: str, person_surname: str, person_email: str, person_phone: str,
                 organization: Organization):
        super().__init__(person_id, person_name, person_surname, person_email, person_phone, organization)
        self.person_id = person_id
        self.person_name = person_name
        self.person_surname = person_surname
        self.person_email = person_email
        self.person_phone = person_phone
        self.organization = organization

    def get_manager_details(self):
        return (f"Person {self.person_id}, {self.person_name}, {self.person_surname}, {self.person_email}, "
                f"{self.person_phone}")
