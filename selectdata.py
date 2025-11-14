<<<<<<< HEAD
# import sqlite3
# conn= sqlite3.connect("sqlite.db")
# data=conn.execute("SELECT * FROM student ")

# for n in data:
#     print(n[0],n[1],n[2],n[3])



import sqlite3 
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM std")
for i in data:
=======
# import sqlite3
# conn= sqlite3.connect("sqlite.db")
# data=conn.execute("SELECT * FROM student ")

# for n in data:
#     print(n[0],n[1],n[2],n[3])



import sqlite3 
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM std")
for i in data:
>>>>>>> b59cf522c424fbf6a2d18df329f6d34c6480da25
    print(i)