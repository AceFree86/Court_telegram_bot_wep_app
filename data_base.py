import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("subscriber.db")
        self.cursor = self.connection.cursor()

    def sql_insert_user(self, user_id, first_name):
        with self.connection:
            self.cursor.execute("INSERT INTO list_user (user_id, first_name) VALUES (?, ?)",
                                       (user_id, first_name))

    def sql_insert_search_value(self, user_input):
        with self.connection:
            self.cursor.execute("INSERT INTO list_user_input (USER_ID, USER_INPUT, STATE) VALUES (?, ?, ?)",
                                       tuple(user_input.values()))

    def sql_insert_meetings(self, user_id, meetings, state_number):
        with self.connection:
            self.cursor.execute("INSERT INTO list_meetings (USER_ID, MEETINGS, STATE) VALUES (?, ?, ?)",
                                       (user_id, meetings,state_number,))

    def sql_update_meetings(self, user_id, meetings, state_number):
        with self.connection:
            self.cursor.execute("UPDATE list_meetings SET STATE=? WHERE USER_ID=? AND MEETINGS=?",
                                (state_number, user_id, meetings))

    def sql_get_user_list_input(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM list_user_input WHERE USER_ID = ?", (user_id,)).fetchall()

    def sql_get_user_list(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM list_user").fetchall()

    def sql_get_user_input(self, user_state):
        with self.connection:
            return self.cursor.execute("SELECT * FROM list_user_input WHERE STATE = ?", (user_state,)).fetchall()

    def sql_get_meetings(self, user_state):
        with self.connection:
            return self.cursor.execute("SELECT * FROM list_meetings WHERE STATE = ?", (user_state,)).fetchall()

    def sql_exists_user(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM list_user WHERE user_id = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def sql_exists_list_input(self, user_id, user_input):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM list_user_input WHERE USER_ID = ? AND USER_INPUT = ?",
                                         (user_id, user_input)).fetchall()
            return bool(len(result))

    def sql_exists_meetings(self, user_id, meetings):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM list_meetings WHERE USER_ID = ? AND MEETINGS = ?",
                                         (user_id, meetings)).fetchall()
            return bool(len(result))

    def sql_exists_list_id(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM list_user_input WHERE USER_ID = ?", (user_id,)).fetchall()
            return bool(len(result))

    def sql_delete_search_value(self, user_id, user_input):
        with self.connection:
            self.cursor.execute("DELETE FROM list_user_input WHERE USER_ID = ? AND USER_INPUT = ?",
                                (user_id, user_input))

    def sql_delete_all_search_value(self, user_id):
        with self.connection:
            rows_deleted = self.cursor.execute("DELETE FROM list_user_input WHERE USER_ID = ?", (user_id,)).rowcount
            return rows_deleted
