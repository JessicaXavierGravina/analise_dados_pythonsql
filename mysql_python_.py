#  pip install mysql-connector-python

import mysql.connector

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='..',
    password='..',
    database='bdempresa',
)
cursor = conexao.cursor()

# CRUD
#CREATE
nome_produto = "pao de queijo"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # le o banco de dados
# print(resultado)


# UPDATE
# nome_produto = "geleia"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# DELETE
# nome_produto = "geleia"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

cursor.close()
conexao.close()
