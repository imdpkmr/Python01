import mysql.connector

db_host = "localhost"
db_user = "root"
db_password = "root"
db_name = "TESTDB"

database = mysql.connector.connect(host=db_host, user=db_user, passwd=db_password, database=db_name)

cursor = database.cursor()
#
# sql="""INSERT INTO EMPLOYEE(FIRST_NAME,
#         LAST_NAME, AGE, GENDER, INCOME)
#         VALUES('Mac','Mohan', 20, 'M', 2000)"""
#
# try:
#     cursor.execute(sql)
#     database.commit()
# except:
#     database.rollback()
#
# database.close()


sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, GENDER, INCOME) VALUES('%s','%s','%d','%c','%d')" % (
'deepak', 'kumar', 21, 'M', 1998)
try:
    cursor.execute(sql)
    print("data entered")
    database.commit()
    print("data saved")
except:
    database.rollback()

database.close()
