# import sqlite3
# conn= sqlite3.connect("sqlite.db")
# data=conn.execute("SELECT * FROM student ")

# for n in data:
#     print(n[0],n[1],n[2],n[3])



import sqlite3 
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM std")
for i in data:
    print(i)