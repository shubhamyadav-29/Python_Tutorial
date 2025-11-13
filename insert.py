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
conn.close()