class user:
    def __init__(self,username, email):
        self.username = username
        self.email = email
    def display(self):
        print("Username:", self.username)
        print("Email:", self.email)
class admin(user):
    def __init__(self, role, username, email):
        super().__init__(username, email)
        self.role = role
    def display(self):
        super().display()
        print("Role:", self.role)
a = admin("Super Admin", "admin_user", "kgmd@gmail.com")
a.display()