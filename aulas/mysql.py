import sys
sys.path.insert(0, r"c:\users\felip\pycharmprojects\aprendendosql\venv\lib\site-packages")

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Jogador05',
    database='bd_teste',
)

cursor = conexao.cursor()

#CRUD#
nome_produto = "Chocolate"
valor = 10
comando = f'INSERT INTO vendas (Nomes_produtos, Valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()

conexao.close()
cursor.close()

# CREATE
# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados


# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)


# UPDATE
# nome_produto = "todynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# DELETE
# nome_produto = "todynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados
