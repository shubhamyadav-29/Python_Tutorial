<<<<<<< HEAD
# import sqlite3
# conn=sqlite3.connect("sqlite.db")


# ins='''
#      INSERT INTO student (st_name, st_class, st_email)
# VALUES 
#     ('kavi', '12th', 'kavi@gmail.com'),
#     ('SITA', '11th', 'sita@gmail.com'),
#     ('RAJU', '10th', 'raju@gmail.com')
# '''

# conn.execute(ins)
# conn.commit()
# conn.close()

import sqlite3
conn = sqlite3.connect("sqlite.db")

ins ='''
       INSERT INTO std (st_name ,st_class ,st_email )
        VALUES 
            
          ('shyam','12th','shyam@gmail.com'),
          ('kavi', '12th', 'kavi@gmail.com'),
          ('SITA', '11th', 'sita@gmail.com'),
          ('RAJU', '10th', 'raju@gmail.com')
       
          


'''

conn.execute(ins)
conn.commit()
=======
# import sqlite3
# conn=sqlite3.connect("sqlite.db")


# ins='''
#      INSERT INTO student (st_name, st_class, st_email)
# VALUES 
#     ('kavi', '12th', 'kavi@gmail.com'),
#     ('SITA', '11th', 'sita@gmail.com'),
#     ('RAJU', '10th', 'raju@gmail.com')
# '''

# conn.execute(ins)
# conn.commit()
# conn.close()

import sqlite3
conn = sqlite3.connect("sqlite.db")

ins ='''
       INSERT INTO std (st_name ,st_class ,st_email )
        VALUES 
          ('shubham','12th','shubham@gmail.com'),
          ('ram','12th','ram@gmail.com'),
          ('shyam','12th','shyam@gmail.com'),
          ('balaram','12th','balaram@gmail.com')
          


'''

conn.execute(ins)
conn.commit()
>>>>>>> b59cf522c424fbf6a2d18df329f6d34c6480da25
conn.close()