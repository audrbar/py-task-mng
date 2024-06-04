from person import Person


class Manager(Person):
    def __init__(self, person_name: str, person_surname: str, person_email: str):
        super().__init__(person_name, person_surname, person_email)
        self.projects = []
        self.managers = []
        self.managers.append(self)
        print(f"Success. Manager {self.person_fullname} was created.")

    def get_managers(self):
        for manager in self.managers:
            return f"\nManager {manager.person_fullname}, {manager.person_email}, (Id: {manager.person_id})."
