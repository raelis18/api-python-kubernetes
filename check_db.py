import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import json

load_dotenv()

db_user = str(os.getenv("db_user"))
db_password = str(os.getenv("db_password"))

def check_db():
    try:
        mydb = mysql.connector.connect(
            host="mysql-service.desafio-db",
            port=80,
            user=db_user,
            password=db_password,
            database="api-python"
        )
        mycursor = mydb.cursor()
        #mycursor.execute("show databases")
        mycursor.close()
        mydb.close()
        data = {
            "db_connection": "Conexão OK"
            }
        return (data)
    except Error as e:
        data = {
            "db_connection": "FAILED",
            "error": str(e)
            }
        return (data)
