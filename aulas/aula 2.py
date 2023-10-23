import pyodbc

banco_dados = r'C:\Users\felip\PycharmProjects\aprendendosql\chinook.db'
dados_conexao = (f"Driver={'SQLite3 ODBC Driver'};Server=localhost;DataBase={banco_dados};") #"UID=login;PWD=senha;"


conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("""
INSERT INTO albums (Title, ArtistId)
VALUES
('Felipe MC', 4) 
""")

cursor.commit()

cursor.close()
conexao.close()
