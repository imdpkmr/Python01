import mysql.connector
from mysql.connector import DatabaseError


def get_database():
    db_host = "localhost"
    __db_user = "root"
    __db_password = "root"
    __db_name = "TESTDB"
    database = mysql.connector.connect(host=db_host, user=__db_user, passwd=__db_password, database=__db_name)
    return database


def create_table():
    sql_query = """CREATE TABLE EMPLOYEE(
        FIRST_NAME VARCHAR(22) NOT NULL,
        LAST_NAME VARCHAR(22),
        AGE INT,
        GENDER VARCHAR(8),
        INCOME FLOAT);"""
    try:
        database = get_database()
        cursor = database.cursor()
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        cursor.execute(sql_query)
        print('table crated successfully')
    except DatabaseError as e:
        print("Error creating table", e)
        database.rollback()
    finally:
        database.close()


def read_records():
    fname = input("enter first name ")
    lname = input("enter last name ")
    gender = input("enter gender m or f")
    try:
        age = int(input("enter age "))
        income = int(input("enter income "))
    except ValueError as e:
        print("Enter valid numbers ")
        read_records()
    return (fname, lname, age, gender, income)


def enter_record():
    f_name, l_name, age, gender, income = read_records()
    sql_query = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, GENDER, INCOME)                 VALUES('%s','%s','%d','%s','%d')" % (
    f_name, l_name, age, gender, income)
    try:
        database = get_database()
        cursor = database.cursor()
        cursor.execute(sql_query)
        database.commit()
        print("data saved in the database")
    except DatabaseError as e:
        print("error while entering records", e)
        database.rollback()
    finally:
        database.close()


def print_records():
    sql_query = "SELECT * FROM EMPLOYEE"
    try:
        database = get_database()
        cursor = database.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            gender = row[3]
            income = row[4]
            # print('read records in individual vars')
            print('fname={}, lname={}, age={}, gender={}, income={}'.format(fname, lname, age, gender, income))
        database.commit()
    except DatabaseError as e:
        print("Error: unable to fetch data", e)
    finally:
        database.close()


def update_record(name=None, age=None, income=None):
    if name is not None:
        pass
    elif income is not None:
        pass
    elif age is not None:
        pass
    else:
        print("trying to update with multiple conditions")


def delete_record():
    name=input("enter name to delete record")
    sql_query = "DELETE FROM EMPLOYEE WHERE FIRST_NAME = '%s'" % name
    try:
        database = get_database()
        cursor = database.cursor()
        cursor.execute(sql_query)
        database.commit()
        print('entry successfully deteled')
    except DatabaseError as e:
        print('error deleting entry',e)
        database.rollback()
    finally:
        database.close()


def print_menu():
    print("*" * 15, "MENU", "*" * 15)
    print("Enter 1 to view records")
    print("Enter 2 to enter records")
    print("Enter 3 to update records")
    print("Enter 4 to delete records")
    print("Enter any other key to exit")
    print("*" * 40)


def menu_choice():
    choice = 0
    try:
        choice = int(input("Enter your choice \n"))
    except ValueError as e:
        print("Enter a valid value from menu")
    return choice


def perform_query(query_choice):
    repeat = True
    if query_choice == 1:
        print_records()
    elif query_choice == 2:
        enter_record()
    elif query_choice == 3:
        update_record()
    elif query_choice == 4:
        delete_record()
    else:
        repeat = False
    return repeat


if __name__ == '__main__':
    # create_table()
    take_input = True
    while take_input:
        print_menu()
        take_input = perform_query(menu_choice())
        # break
