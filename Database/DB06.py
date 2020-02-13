import mysql.connector

db_name="TESTDB"
db_user="root"
db_password="root"
db_host="localhost"

database=mysql.connector.connect(host=db_host, user=db_user, passwd=db_password, database=db_name)

cursor=database.cursor()

sql="DELETE FROM EMPLOYEE WHERE AGE < '%d'"%(22)

try:
    cursor.execute(sql)
    database.commit()
except:
    database.rollback()

database.close()