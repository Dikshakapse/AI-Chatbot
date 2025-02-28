import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Diksha@404",
        database="supplier_chatbot"
    )