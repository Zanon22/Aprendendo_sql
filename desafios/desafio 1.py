import pyodbc
import pandas as pd

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;DataBase=salarios.sqlite;") #"UID=login;PWD=senha;"

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM Salarios")

valores = cursor.fetchall()
print(valores[:10])

cursor.close()
conexao.close()

