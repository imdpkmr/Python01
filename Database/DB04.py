import mysql.connector

db_host="localhost"
db_user="root"
db_password="root"
db_name="TESTDB"

database=mysql.connector.connect(host=db_host,user= db_user,passwd= db_password, database=db_name)

cursor=database.cursor()

sql="SELECT * FROM EMPLOYEE WHERE INCOME > '%d'"%(1000)

try:
    cursor.execute(sql)
    results=cursor.fetchall()
    # print("fetched cursor")
    for row in results:
        fname=row[0]
        lname=row[1]
        age=row[2]
        gender=row[3]
        income=row[4]

        print("fname=%s, lname=%s, age=%d, gender=%s, income=%d"%(fname,lname, age, gender, income))
except:
    print("Error: unable to fetch data")

database.close()
