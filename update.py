import sqlite3
conn = sqlite3.connect("sqlite.db")
ins = input("Enter the student_id:")
# conn.execute("update std set st_id='shubham' where st_id="+ins)
conn.execute("UPDATE std SET st_name = ? WHERE st_id = ?", ('shubham', ins))

conn.commit()
conn.close()

