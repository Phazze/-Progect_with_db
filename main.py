import pymysql
from auth import user, password, database, host


try:
    mydb = pymysql.connect(
        host=host,
        password=password,
        port=3306,
        user=user,
        database=database
    )
    print("all good")
    print("######" * 10)

    try:
        with mydb.cursor() as cursor:
            cursor.execute("SELECT * from connect;")
            print(cursor.fetchall())
    finally:
        mydb.close()



except Exception as ex:
    print("Connection failed....")
    print(ex)

