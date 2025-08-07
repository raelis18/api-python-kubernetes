import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import json

load_dotenv()

db_user = str(os.getenv("db_user"))
db_password = str(os.getenv("db_password"))

def insert_db(name, email):
    query = f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')"
    try:
        mydb = mysql.connector.connect(
            host="mysql-service.desafio-db",
            port=80,
            user=db_user,
            password=db_password,
            database="api-python"
        )
      
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
        mycursor.close()
        mydb.close()
        data = {
            "status": "Dados inseridos com sucesso"
            }
        return (data)
    except Error as e:
        data = {
            "status": "Falha ao inserir dados",
            "error": str(e) + query
            }
        return (data)
