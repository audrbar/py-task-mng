class Organization:

    def __init__(self, org_id: str, org_name: str, org_email: str, org_phone: str, org_address: str):
        self.org_id = org_id
        self.org_name = org_name
        self.org_email = org_email
        self.org_phone = org_phone
        self.org_address = org_address

    def get_org_details(self):
        return f"Person {self.org_id}, {self.org_name}, {self.org_email}, {self.org_phone}, {self.org_address}"
