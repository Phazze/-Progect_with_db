import pymysql
# import _mysql_connector
from auth import user, password, database, host


class MySQL(object):

    def __init__(self, host, password, port, user, database):
        try:
            self.mydb = pymysql.connect(
                host=host,
                password=password,
                port=port,
                user=user,
                database=database,
                # cursorclass= pymysql.cursors.DictCursor
            )
            print("all good")
            print("######" * 10)
        except Exception as ex:
            print("Connection failed....")
            print(ex)
    def vxod(self):
        print("Input login: ")
        login = str(input())
        print("Input password: ")
        user_password = str(input())
        try:
            with self.mydb.cursor() as cursor:
                sql_zapros = f"SELECT first_name, Last_name, age, information from users, connect where connect.login = '{login}' and connect.password = '{user_password}' and connect.id = users.fk_id;"
                cursor.execute(sql_zapros)
                vivod = cursor.fetchall()
                print(vivod)
        finally:
            self.mydb.close()

    def register(self):
        print("Input your name:")
        name = str(input())
        print("Input your last name:")
        last_name = str(input())
        print("Input your age: ")
        age = int(input())
        print("Input information about you: ")
        information = str(input())
        print("Create your login: ")
        login = str(input())
        print("Create your password: ")
        user_password = str(input())
        print("Repeat your password: ")
        user_password2 = str(input())
        if user_password == user_password2:
            try:
                with self.mydb.cursor() as cursor:
                    sql_zapros = f"INSERT connect(login, password) VALUES ('{login}', '{user_password}');"
                    sql_zapros2 = f"INSERT users(first_name, last_name, age, information, login) VALUES ('{name}', '{last_name}', {age}, '{information}', '{login}');"
                    sql_dop = f"UPDATE users set fk_id = (SELECT id from connect where connect.login = users.login);"
                    cursor.execute(sql_zapros)
                    self.mydb.commit()
                    cursor.execute(sql_zapros2)
                    cursor.execute(sql_dop)
                    self.mydb.commit()
            except Exception as er:
                print(er)
            finally:
                self.mydb.close()


q= MySQL(host = host, port = 3306, password = password, database= database, user = user,)
q.register()

