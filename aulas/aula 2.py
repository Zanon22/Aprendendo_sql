import pyodbc

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;DataBase=chinook.db;") #"UID=login;PWD=senha;"

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
