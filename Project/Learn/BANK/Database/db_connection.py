import pyodbc

# def get_db_connection():
#     conn = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};'
#         r'SERVER=ADMIN-PC\SQLEXPRESS;'
#         'DATABASE=BANK;'
#     )
#     return conn



def get_db_connection():
    server = r'ADMIN-PC\SQLEXPRESS'
    database = 'BANK'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    conn = pyodbc.connect(connection_string)
    return conn

