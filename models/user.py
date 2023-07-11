from db.crud.users_crud import UsersDb


class User:

    def __init__(
            self,
            email,
            password,
            user_id=None,
            username=None,
            confirm_password=None
    ):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

        self.user_db = UsersDb()

    def check_in_db(self):
        users = self.user_db.read(email=self.email)
        if not users:
            raise Exception("No user found with this email")

        user = users[0]
        if user["password"] != self.password:
            raise Exception("Invalid password!")
        return True
