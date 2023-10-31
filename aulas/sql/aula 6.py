import pyodbc
import pandas as pd

banco_dados = r'C:\Users\felip\PycharmProjects\pythonintegrado\chinook.db'
dados_conexao = (f"Driver={'SQLite3 ODBC Driver'};Server=localhost;DataBase={banco_dados};") #"UID=login;PWD=senha;"

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("""
DELETE FROM albums WHERE Title='Felipe MC'
""")

cursor.commit()

cursor.close()
conexao.close()
