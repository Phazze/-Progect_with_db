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
    except Exception as ex:
        print("Connection failed....")
        print(ex)
class deistvie(MySQL):
    def vxod(self, mydb):
        print("Input login: ")
        login = str(input())
        print("Input password: ")
        user_password = str(input())
        try:
            with mydb.cursor() as cursor:
                sql_zapros = f"SELECT first_name, Last_name, age, informachion from users, connect where connect.login = '{login}' and connect.password = '{user_password}' and connect.id = users.fk_id;"
                cursor.execute(sql_zapros)
                vivod = cursor.fetchall()
                print(vivod)
        finally:
            mydb.close()
    def register(self,mydb):
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
                with mydb.cursor as cursor:
                    sql_zapros=(f""" INSERT connect(login, password) VALUES ({login}, {user_password});
                    INSERT users(first_name, last_name, age, information, fk_id ) VALUES ({name}, {last_name}, {age}, {information}, fk_id = connect.id);""")
                    cursor.execute(sql_zapros)
                    cursor.commit()
            finally:
                mydb.close()

if __name__ == "__main__":
    mydb = pymysql.connect(
        host=host,
        password=password,
        port=3306,
        user=user,
        database=database
    )
    deistvie.register(mydb = mydb, self=deistvie)












