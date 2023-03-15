import pymysql
from auth import user, password, database, host

class MySQL():
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
        login = str(input())
        user_password = str(input())
        try:
            with mydb.cursor() as cursor:
                sql_zapros = f"SELECT first_name, Last_name, age, informachion from users, connect where connect.login = '{login}' and connect.password = '{user_password}' and connect.id = users.fk_id;"
                cursor.execute(sql_zapros)
                vivod = cursor.fetchall()
                print(vivod)
        finally:
            mydb.close()
    except Exception as ex:
        print("Connection failed....")
        print(ex)

