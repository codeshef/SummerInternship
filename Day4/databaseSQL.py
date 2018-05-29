import mysql.connector

# Establish connection with mysql using connector

conn = mysql.connector.connect(user='root', password='anchal', host='127.0.0.1')

myCursor = conn.cursor()

# Create Database
# myCursor.execute("CREATE DATABASE studentDb")

# Use database
myCursor.execute("Use studentDb")

# Create Table

#myCursor.execute(
   # 'CREATE TABLE userTbl(id int primary key AUTO_INCREMENT, name varchar(30), salary int)')


# myCursor.execute("""Insert into studentTbl(id,name,salary,city) values(10,'"""+name+"""','"""+str(salary)+"""',
# 'CHD')""")

# myCursor.execute("Insert into studentTbl values(1,'user',10000,'CHD')")

# myCursor.execute("""Insert into studentTbl(id,name,salary,city) values(10,'"""+name+"""','"""+str(salary)+"""',
# 'CHD')""")

# myCursor.execute("SELECT*FROM studentTbl")

# print("id ")

#myList = myCursor.fetchall()

#for i in myList:

    #j = int(i[0])

    #print(str(j)+" "+i[1] + " "+str(i[2])+" "+i[3])
#print(type(myList))

name = input('Enter Name : ')
salary = input('Enter Salary : ')


myCursor.execute("Insert into userTbl(name,salary) values('"+name+"','"+str(salary)+"')")




# add conn.commit() in case of insertion and updation

conn.commit()
conn.close()

