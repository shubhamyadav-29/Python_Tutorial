import pymysql as mq

# Server Name -> localhost
#Username-> root 
#Password -> ';'
myobj = mq.connect("localhost","root","")
cursorobj=myobj.cursor()