import mysql.connector

database=mysql.connector.connect(host="localhost", user="root", passwd="root",database="TESTDB")

cursor = database.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql="""CREATE TABLE EMPLOYEE (
FIRST_NAME CHAR(20) NOT NULL,
LAST_NAME CHAR(20),
AGE INT,
GENDER CHAR(1),
INCOME FLOAT)"""

cursor.execute(sql)

database.close()