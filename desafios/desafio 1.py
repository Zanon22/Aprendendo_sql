import pyodbc
import pandas as pd

banco_dados = r'C:\Users\felip\PycharmProjects\aprendendosql\salarios.sqlite'
dados_conexao = (f"Driver={'SQLite3 ODBC Driver'};Server=localhost;DataBase={banco_dados};") #"UID=login;PWD=senha;"

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM Salaries")

valores = cursor.fetchall()
descricao = cursor.description
colunas = [tuple[0] for tuple in descricao]

tabela_clientes = pd.DataFrame.from_records(valores, columns=colunas, index="Id")

print(tabela_clientes)
print(tabela_clientes.info())

cursor.close()
conexao.close()

