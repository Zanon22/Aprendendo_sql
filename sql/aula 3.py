import pandas as pd
import sqlite3

conexao = sqlite3.connect("../chinook.db")

tabela_clientes = pd.read_sql("SELECT * FROM customers", conexao)
print(tabela_clientes)

conexao.close()
