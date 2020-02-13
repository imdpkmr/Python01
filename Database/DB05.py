import mysql.connector

db_host="localhost"
db_user="root"
db_password="root"
db_name="TESTDB"
# open database connection
database=mysql.connector.connect(host=db_host, user=db_user, passwd=db_password, database=db_name)
# prepare a cursor object usign cursor() method
cursor=database.cursor()
# prepare SQL query to UPDATE required records
sql="UPDATE EMPLOYEE SET AGE=AGE+1 WHERE GENDER='%c'"%('M')

try:
    # execute the sql command
    print('before cursor.execute()')
    cursor.execute(sql)
    print('cursor executed command')
    # commit your changes in the database
    database.commit()
    print('data updated')
except:
    # rollback in case of there is any error
    database.rollback()

database.close()