import sqlite3

def conectar():
    conexao = sqlite3.connect('crud.db')
    return conexao

def desconectar(conexao):
    conexao.close()

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')
    conexao.commit()

def incluir(conexao, nome, idade):
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO pessoas (nome, idade) VALUES ('{nome}', {idade})")
    conexao.commit()

def listar(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    for pessoa in pessoas:
        print(pessoa)

def atualizar(conexao, id, nome, idade):
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE pessoas SET nome = '{nome}', idade = {idade} WHERE id = {id}")
    conexao.commit()

def excluir(conexao, id):
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM pessoas WHERE id = {id}")
    conexao.commit()

conexao = conectar()
criar_tabela(conexao)
opcao = 0
while opcao != 5:
    print("--- Menu ---")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        incluir(conexao, nome, idade)
    elif opcao == 2:
        listar(conexao)
    elif opcao == 3:
        id = int(input("ID: "))
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        atualizar(conexao, id, nome, idade)
    elif opcao == 4:
        id = int(input("ID: "))
        excluir(conexao, id)
desconectar(conexao)