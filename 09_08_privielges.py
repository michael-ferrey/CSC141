class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can edit post",
        ]

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin:
    def __init__(self, username):
        self.username = username
        self.privileges = Privileges()

    def show_admin_privileges(self):
        self.privileges.show_privileges()

if __name__ == "__main__":
    admin_user = Admin("admin1")
    admin_user.show_admin_privileges()
