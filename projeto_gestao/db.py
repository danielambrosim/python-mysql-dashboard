# db.py
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Senhaforte%TCCnoteBOOK123",
        database="loja_db"
    )
