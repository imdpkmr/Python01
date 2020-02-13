import mysql.connector

# Open database connection
db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
print("Database version : %s " % data)

# disconnect from server
db.close()