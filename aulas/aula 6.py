import pyodbc
import pandas as pd

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;DataBase=chinook.db;") #"UID=login;PWD=senha;"

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("""
DELETE FROM albums WHERE Title='Felipe MC'
""")

cursor.commit()

cursor.close()
conexao.close()
