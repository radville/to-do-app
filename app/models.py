import sqlite

class Schema:
    def __init__(self):
        # connect to database
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          _is_done boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)
    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          Name TEXT NOT NULL,
          Email TEXT,
          CreatedOn Date DEFAULT CURRENT_DATE,
        );
        """
        self.conn.execute(query)