import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def create_connection():
    """Cria uma conexão com o banco de dados MySQL."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            print("Conexão ao MySQL foi estabelecida com sucesso!")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def close_connection(connection):
    """Fecha a conexão com o banco de dados."""
    if connection and connection.is_connected():
        connection.close()
        print("Conexão ao MySQL foi encerrada.")