import mysql.connector


def db_connection():
    conn = mysql.connector.connect(
        host="3.138.156.32",
        port=3309,
        database="habi_db",
        user="pruebas",
        password="VGbt3Day5R",
    )
    return conn
