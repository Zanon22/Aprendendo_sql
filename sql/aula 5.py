import pyodbc
import pandas as pd

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;DataBase=chinook.db;") #"UID=login;PWD=senha;"

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("""
UPDATE customers SET Email='felipe@embraer.com.br' WHERE Email='luisg@embraer.com.br'
""") #executar comando sql

cursor.commit() #perpetuar no banco as alterações

cursor.close()
conexao.close() #finalizar a conexão
