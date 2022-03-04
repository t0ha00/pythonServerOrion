import pyodbc

DRIVER = r'ODBC Driver 17 for SQL Server'
SERVER_NAME = r'SRV-VT\Orion'
CONN_STRING = f"""
                Driver={{{DRIVER}}};
                SERVER={SERVER_NAME};
                Trust_connection=no;
                UID=Anton;
                PWD=3Wasdfghjkl;
            """


def get_get_tp_data():
    with pyodbc.connect(CONN_STRING) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT Имя, Код FROM Orion.dbo.Филиалы ORDER BY Имя;")
        row = cursor.fetchall()
        print(row)
    return row


def get_get_tp_names_data(tp_code):
    with pyodbc.connect(CONN_STRING) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ФИО, Пароль FROM Orion.dbo.Сотрудники WHERE Код_филиала =" + tp_code + " ORDER BY ФИО;")
        row = cursor.fetchall()
        print(row)
    return row


def get_get_login_passwd(login, passwd):
    with pyodbc.connect(CONN_STRING) as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT ФИО, Пароль FROM Orion.dbo.Сотрудники WHERE Логин = \'{login}\' AND Пароль = \'{passwd}\'")
        row = cursor.fetchall()
        if not row:
            return 'FALSE'
        else:
            return 'TRUE'


# -----------------------------------------Group Making Form

# Get Subdivision List
def get_get_subdivision_list(code):
    with pyodbc.connect(CONN_STRING) as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT Имя FROM Филиалы where Код = \'{code}\'")
        row = cursor.fetchall()
    return row


# Get Collaborator List with number of groups
def get_get_collaborator_list_num_groups(code):
    with pyodbc.connect(CONN_STRING) as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT [Сотрудники].[Код], substring([ФИО], 1, charindex(' ', [ФИО]))+substring([ФИО], "
                       f"charindex(' ', [ФИО])+1,1)+'.'+substring([ФИО], charindex(' ', [ФИО], "
                       f"charindex(' ', [ФИО])+1)+1,1)+'.' as i , COUNT(t.[id]) AS n "
                       f"FROM Orion.dbo.Сотрудники right OUTER JOIN "
                       f"(SELECT [Код], [Закрытие], [Ответственный], [id] "
                       f"FROM Orion.dbo.[Группы] WHERE ([Закрытие] = 0)) t ON [Сотрудники].[ФИО] = t.[Ответственный] "
                       f"WHERE ([Запись_удалена] = 0) And ([Ответственный_за_группы] = 1 And [Код_филиала] = {code}) "
                       f"GROUP BY [Сотрудники].[Код], [Сотрудники].[ФИО] ")
        row = cursor.fetchall()
    return row


def get_get_collaborator_list_num_groups_checked(code):
    with pyodbc.connect(CONN_STRING) as connection:
        cursor = connection.cursor()
        cursor.execute(f"select Код, substring(ФИО, 1, charindex(' ', ФИО))+substring(ФИО, charindex(' ', ФИО)+1,1)+'.'"
                       "+substring(ФИО, charindex(' ', ФИО, charindex(' ', ФИО)+1)+1,1)+'.' as i from "
                       "Orion.dbo.Сотрудники WHERE (Запись_удалена = 0) And (Ответственный_за_группы = 1 And "
                       f"Код_филиала = {code})")
        row = cursor.fetchall()
    return row
