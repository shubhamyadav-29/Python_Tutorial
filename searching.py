<<<<<<< HEAD
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
=======
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
>>>>>>> b59cf522c424fbf6a2d18df329f6d34c6480da25
