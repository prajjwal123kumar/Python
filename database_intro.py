# Database Connectivity 


 #Create the data
 import pymysql as pm
 con=pm.connect(host="localhost",user="root",password="9554",database="student_db")
 cursor=con.cursor()

 while True:
     name=input("Enter your name:")
     age=int(input("Enter your age:"))
     marks=float(input("Enter your marks:"))
     query="Insert into info values('{}',{},{})".format(name,age,marks)
     cursor.execute(query)
     con.commit()
     print("Data Entered Successfully.")
     option=int(input("Enter your choice:\n 1. Enter more data.\n 2.Exit."))
     if option ==2:
         break

 #update the data
 import pymysql as pm
 con=pm.connect(host="localhost",user="root",password="9554",database="student_db")
 cursor=con.cursor()
 name=input("Enter name:")
 age=int(input("Enter age:"))
 marks=float(input("Enter marks:"))
 # query="Update info set name='{}' where age={}".format(name,age)
 # query="Update info set age={} where name='{}'".format(age,name)
 query="Update info set marks={} where name='{}'".format(marks,name)
 cursor.execute(query)
 con.commit()
 if cursor.rowcount>0:
     print("Update Successfully..")
 else:
     print("No Updation")

 #Delete the data

 import pymysql as pm
 con=pm.connect(host="localhost",user="root",password="9554",database="student_db")
 cursor=con.cursor()
 name=input("Enter name:")
 query="delete from info where name='{}'".format(name)
 cursor.execute(query)
 con.commit()
 if cursor.rowcount>0:
     print("Delete Successfully.")
 else:
     print("No Deletion")

# Data Fetch from table

import pymysql as pm
con=pm.connect(host="localhost",user="root",password="9554",database="student_db")
cursor=con.cursor()
query="select * from info"
cursor.execute(query)
# data=cursor.fetchone() # data given a single tuple
# data=cursor.fetchmany(2) # data given a List inside Tuple(Tuple inside Tuple)
data=cursor.fetchall() # all data given a List inside Tuple(Tuple inside Tuple)
print(data)