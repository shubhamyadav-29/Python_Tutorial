import sqlite3
conn = sqlite3.connect("sqlite.db")
st_id=input('Enter the student id : ')
st_id2=input('Enter the student id 2: ')
st_id3=input('Enter the student id 3: ')

conn.execute("DELETE FROM std where st_id=" + st_id,)
conn.commit()
conn.close()
