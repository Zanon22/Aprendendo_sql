import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Jogador05',
    database='db_teste',
)

cursor = conexao.cursor


cursor.close()
conexao.close()
