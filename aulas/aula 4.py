import pyodbc
import pandas as pd

banco_dados = r'C:\Users\felip\PycharmProjects\aprendendosql\chinook.db'
dados_conexao = (f"Driver={'SQLite3 ODBC Driver'};Server=localhost;DataBase={banco_dados};") #"UID=login;PWD=senha;"

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
