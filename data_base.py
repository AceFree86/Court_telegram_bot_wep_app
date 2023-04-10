import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("subscriber.db")
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM list_user WHERE user_id = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id, first_name):
        with self.connection:
            return self.cursor.execute("INSERT INTO list_user (user_id, first_name) VALUES (?, ?)",
                                       (user_id, first_name))

    def sql_add_search_value(self, user_input):
        with self.connection:
            return self.cursor.execute("INSERT INTO list_user_input (USER_ID, USER_INPUT, STATE) VALUES (?, ?, ?)",
                                       tuple(user_input.values()))

    def user_list_input(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM list_user_input WHERE USER_ID = ?", (user_id,)).fetchall()

    def user_list(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM list_user").fetchall()

    def exists_list_input(self, user_input):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM list_user_input WHERE USER_INPUT = ?", (user_input,)).fetchall()
            return bool(len(result))

    def exists_list_id(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM list_user_input WHERE USER_ID = ?", (user_id,)).fetchall()
            return bool(len(result))

    def delete_user_list_input(self, user_input):
        with self.connection:
            self.cursor.execute("DELETE FROM list_user_input WHERE USER_INPUT = ?", (user_input,))

    def delete_all_user_list_input(self, user_id):
        with self.connection:
            rows_deleted = self.cursor.execute("DELETE FROM list_user_input WHERE USER_ID = ?", (user_id,)).rowcount
            return rows_deleted
