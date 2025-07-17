import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=root.c90xs4reiydi.us-east-1.rds.amazonaws.com;'
        'DATABASE=auth_db;'
        'UID=admin;'
        'PWD=Distribuida123'
    )
    return conn, conn.cursor()
