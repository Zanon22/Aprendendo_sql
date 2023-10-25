import pyodbc
import pandas as pd

#formatar os numeros grandes
def formatar(valor):
    return 'R${:,.2f}'.format(valor)

#Conectar com banco de dados
banco_dados = r'C:\Users\felip\PycharmProjects\aprendendosql\salarios.sqlite'
dados_conexao = (f"Driver={'SQLite3 ODBC Driver'};Server=localhost;DataBase={banco_dados};") #"UID=login;PWD=senha;"

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM Salaries")

valores = cursor.fetchall()
descricao = cursor.description
colunas = [tuple[0] for tuple in descricao]

#Transformar banco de dados em Dataframe
tabela_salarios = pd.DataFrame.from_records(valores, columns=colunas)

#Selecionar so San Francisco
tabela_salarios = tabela_salarios.loc[tabela_salarios["Agency"]=="San Francisco", :]

#media dos salarios por ano
tabela_salarios_sm = tabela_salarios.groupby("Year").mean(numeric_only=True)

#Quantidade de salarios no ano
tabela_qtde = tabela_salarios.groupby("Year").count()
tabela_qtde = tabela_qtde[["Id"]]
tabela_qtde = tabela_qtde.rename(columns={"Id": "Quantidade"})

#total dos salarios no ano
tabela_total = tabela_salarios.groupby("Year").sum()
tabela_total = tabela_total[["TotalPay", "TotalPayBenefits"]]
tabela_total["TotalPay"] = tabela_total["TotalPay"].apply(formatar)
tabela_total["TotalPayBenefits"] = tabela_total["TotalPayBenefits"].apply(formatar)

#print de tudo
print(tabela_salarios_sm[["TotalPay", "TotalPayBenefits"]])
print(tabela_qtde)
print(tabela_total)
#print(tabela_salarios.info())

#finalizar conexão
cursor.close()
conexao.close()

