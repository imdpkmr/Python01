import mysql.connector

# host="localhost"
# user="root"
# passwd="root"
mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="db01")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

results = mycursor.fetchone()

for result in results:
    print(result)
