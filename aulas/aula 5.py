import pyodbc
import pandas as pd

banco_dados = r'C:\Users\felip\PycharmProjects\aprendendosql\chinook.db'
dados_conexao = (f"Driver={'SQLite3 ODBC Driver'};Server=localhost;DataBase={banco_dados};") #"UID=login;PWD=senha;"

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("""
UPDATE customers SET Email='felipe@embraer.com.br' WHERE Email='luisg@embraer.com.br'
""") #executar comando aulas

cursor.commit() #perpetuar no banco as alterações

cursor.close()
conexao.close() #finalizar a conexão
