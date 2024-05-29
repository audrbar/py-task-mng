from organization import Organization
from person import Person


class Assignee(Person):
    def __init__(self, person_id: str, person_name: str, person_surname: str, person_email: str, person_phone: str,
                 organization: Organization):
        super().__init__(person_id, person_name, person_surname, person_email, person_phone, organization)
