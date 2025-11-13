# import sqlite3
# conn=sqlite3.connect("sqlite.db")

# ##Here We have created the table with name stu 

# conn.execute('''
#         Create table stu (
#              st_id INT AUTO_INCREMENT PRIMARY KEY,
#              st_name VARCHAR(50),
#              st_class VARCHAR(10),
#              st_email VARCHAR(30)
#          )

#     ''')

# conn.close()


import sqlite3

conn = sqlite3.connect("sqlite.db")

# Create table with proper SQLite syntax
conn.execute('''
CREATE TABLE std (
    st_id INTEGER PRIMARY KEY AUTOINCREMENT,
    st_name TEXT,
    st_class TEXT,
    st_email TEXT
)
''')

conn.close()




