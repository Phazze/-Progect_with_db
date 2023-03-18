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
                sql_zapros = f"SELECT first_name, last_name, age, information from users, connect where connect.login = '{login}' and connect.password = '{user_password}' and connect.id = users.fk_id;"
                cursor.execute(sql_zapros)
                vivod = cursor.fetchall()
                print(*vivod)
        except Exception as er:
            print("Something was wrong...... maybe login or password not correct")
            print(er)
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

    def delete(self):
        print("Input login and we delete it: ")
        login = str(input())
        print("Do you delete your profile? Input y or n. ")
        soglasie = str(input())
        if soglasie == "y":
            try:
                with self.mydb.cursor() as cursor:
                    sql_zapros = f"DELETE from users where login = '{login}';"
                    sql_zapros2 = f"DELETE from connect where login = '{login}';"
                    cursor.execute(sql_zapros)
                    cursor.execute(sql_zapros2)
                    self.mydb.commit()
            except Exception as ex:
                print(ex)
            finally:
                self.mydb.close()


class User_Action(MySQL):
    q = MySQL(host=host, port=3306, password=password, database=database, user=user, )
    print("What do you like do? If you would like registrate profile print(reg), if you would like to connect your profile print(con), if you would like delete profile print(del)")
    action = str(input())
    if action == 'reg':
        q.register()
    elif action == "con":
        q.vxod()
    elif action =="del":
        q.delete()
    else: print("Command unknow....")