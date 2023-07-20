import uuid

from db.crud.users_crud import UsersDb


class User:

    def __init__(
            self,
            email,
            password,
            user_id=None,
            username=None,
            confirm_password=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.user_db = UsersDb()

    def validate_create(self):
        """
        1. Verificam ca am primit toate campurile necesare pentru creare user nou.
        2. Validam parola -> self._validate_password()
        3. Verificam ca parolele introduse coincid
        :return:
        """
        self._check_fields()
        self._validate_username()
        self._validate_password()
        self._check_passwords()

    def _check_fields(self):
        if not self.email or not self.password or not self.username or not self.confirm_password:
            raise Exception("Some values were empty!")

    def _validate_password(self):
        """
        1. verificam ca avem lungimea de minim 8 caractere
        2. Verificam ca avem cel putin o litera mare
        3. Verificam ca avem cel putin un caracter special (-, /, ?, @ etc)
        special_chars = "!@#$%^&*()-=_+[]{}|;':\"<>,./?\\"
        """
        # TODO: implement _validate_password
        pass

    def _validate_username(self):
        """
        1. verificam ca username-ul nu contine caractere speciale
        invalid_chars = "!#$%^&*()+=`~/?<>,\\|\"\'|țșăîâÂÎȚȘĂ"
        """
        # TODO: implement _validate_username
        pass

    def _check_passwords(self):
        if self.password != self.confirm_password:
            raise Exception("Passwords do not match!")

    def add(self):
        self.validate_create()
        get_by_username = self.user_db.read(username=self.username)
        get_by_email = self.user_db.read(email=self.email)
        print(f"BY USERNAME {get_by_username}")
        print(f"BY EMAIL {get_by_email}")

        if get_by_email or get_by_username:
            raise Exception("Username or email already exists!")
        self.user_db.create(self._to_dict_create())

    def check_in_db(self):
        users = self.user_db.read(email=self.email)
        if not users:
            raise Exception("No user found for this email!")
        user = users[0]
        if user["password"] != self.password:
            raise Exception("Invalid password!")
        return True

    def _to_dict_create(self):
        return {
            'id': str(uuid.uuid4()),
            'username': self.username,
            'password': self.password,
            'email': self.email
        }
