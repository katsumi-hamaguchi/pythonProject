import sqlite3

con = sqlite3.connect("test.db")

cursor = con.cursor()

create_user_table_query = """
CREATE TABLE IF NOT EXISTS User (
    UserId INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER
)
"""

cursor.execute(create_user_table_query)

insert_query = """
INSERT INTO User VALUES(4,"test",20)
INSERT INTO User VALUES(2,"test",20)
INSERT INTO User VALUES(3,"test",20)
"""

cursor.execute(insert_query)
con.commit()