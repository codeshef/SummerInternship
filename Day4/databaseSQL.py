import mysql.connector

# Establish connection with mysql using connector

conn = mysql.connector.connect(user='root', password='anchal', host='127.0.0.1')

myCursor = conn.cursor()

# Create Database
# myCursor.execute("CREATE DATABASE studentDb")

# Use database
myCursor.execute("Use studentDb")

# Create Table

# myCursor.execute("CREATE TABLE studentTbl(id int primary key, name varchar(30), salary int, city varchar(30))")


# myCursor.execute("""Insert into studentTbl(id,name,salary,city) values(10,'"""+name+"""','"""+str(salary)+"""',
# 'CHD')""")

# myCursor.execute("Insert into studentTbl values(1,'user',10000,'CHD')")

# add conn.commit() in case of insertion and updation
conn.commit()
conn.close()

