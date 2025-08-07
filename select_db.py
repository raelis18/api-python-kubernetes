import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import json

load_dotenv()

db_user = str(os.getenv("db_user"))
db_password = str(os.getenv("db_password"))

def select_db():
    try:
        mydb = mysql.connector.connect(
            host="mysql-service.desafio-db",
            port=80,
            user=db_user,
            password=db_password,
            database="api-python"
        )
        query = "select u.id, u.name, u.email from users u"
        mycursor = mydb.cursor()
        mycursor.execute(query)

        result = mycursor.fetchall()
        data = []
        for row in result:
            data.append({
                "id": row[0],
                "name": row[1],
                "email": row[2]
            })
        mycursor.close()    
        mydb.close()
        return (data)
    except Error as e:
        data = {
            "db_connection": "FAILED",
            "error": str(e)
            }
        return (data)
