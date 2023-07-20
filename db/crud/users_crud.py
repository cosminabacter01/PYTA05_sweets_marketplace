"""
DB CRUD methods for Users table
"""
from db.crud.interface_crud import CrudABC


class UsersDb(CrudABC):

    def create(self, entry_to_create):
        SQL_QUERY = """
        INSERT INTO Users(id, username, password, email) 
        VALUES (:id, :username, :password, :email);
        """
        cursor = self.connection.cursor()
        cursor.execute(
            SQL_QUERY,
            entry_to_create
        )
        self.connection.commit()

    def read(self, username=None, email=None, id=None):
        sql_query = "SELECT * FROM Users "
        value = ''
        if id:
            sql_query += "WHERE id=?;"
            value = id
        elif username:
            sql_query += "WHERE username=?;"
            value = username
        elif email:
            sql_query += "WHERE email=?;"
            value = email
        cursor = self.connection.cursor()
        if not value:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, (value,))

        users = cursor.fetchall() # o lista cu liste

        users_json = []
        for user in users:
            users_json.append({
                "id": user[0],
                "username": user[1],
                "password": user[2],
                "email": user[3]
            })
        return users_json

    def update(self, entry_for_update):
        SQL_QUERY = """
        UPDATE Users SET id=:id, username=:username, password=:password, email=:email, is_logged=:is_logged WHERE id=:id;
        """
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY, entry_for_update.__dict__)
        self.connection.commit()

    def delete(self, id):
        SQL_QUERY = "DELETE FROM Users WHERE id=?;"
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY, (id,))
        self.connection.commit()
        print(f"ROW {cursor.rowcount}")
        return bool(cursor.rowcount)  # cursor.rowcount == 0 -> nici un rand a fost afectat
