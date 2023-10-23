import pyodbc
import pandas as pd

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;DataBase=chinook.db;") #"UID=login;PWD=senha;"

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("""
SELECT * FROM customers
""")

valores = cursor.fetchall()
descricao = cursor.description
colunas = [tuple[0] for tuple in descricao]
print(colunas)

tabela_clientes = pd.DataFrame.from_records(valores, columns=colunas, index="CustomerId")
print(tabela_clientes)
#tabela_clientes.to_csv("tabela_clientes.csv", sep=";")

cursor.close()
conexao.close()
