class Organization:
    org_count = 0

    def __init__(self, org_name: str, org_email: str, org_count=None):
        self.org_name = input("Enter Organization Name: ")
        self.org_email = input("Enter Organization Email: ")
        org_count.Organization += 1

    def get_org_details(self):
        return f"Person {self.org_name}, {self.org_email}"

    def __str__(self):
        return f"{self.org_name}, {self.org_email}"
