from person import Person


class Manager(Person):
    def __init__(self, person_id: str, person_name: str, person_surname: str, person_email: str):
        super().__init__(person_id, person_name, person_surname, person_email)
        self.person_id = person_id
        self.person_name = person_name
        self.person_surname = person_surname
        self.person_fullname = f"{person_name} {person_surname}"
        self.person_email = person_email
        self.managers = []
        self.managers.append(self)

    def get_managers(self, managers):
        for manager in managers:
            return f"Project {manager.person_fullname}, {manager.person_email}.\n"

    def get_manager_details(self):
        return f"Manager {self.person_id}, {self.person_fullname}, {self.person_email}."
