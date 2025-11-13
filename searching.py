import sqlite3
conn=sqlite3.connect("sqlite.db")

data =conn.execute("Select * from std")

for i in data:
    print(i)

print("________________________________________________________")

ins=input("Enter the name of student:-")
# data=conn.execute("select * from std where st_name='"+ins+"'")
data=conn.execute("select * from std where st_name like '%"+ins+"%'")
for i in data:
    print(i)
