import pyodbc

DRIVER = r'ODBC Driver 17 for SQL Server'
SERVER_NAME = r'SRV-VT\Orion'
CONN_STRING = f"""
                Driver={{{DRIVER}}};
                SERVER={SERVER_NAME};
                Trust_connection=no;
                UID=Anton;
                PWD=QAZxswedc321;
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

