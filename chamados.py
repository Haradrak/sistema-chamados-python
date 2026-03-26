import sqlite3
from datetime import datetime

conn = sqlite3.connect("chamados.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    status TEXT,
    prioridade TEXT,
    data_criacao TEXT
)
""")

# Criar chamado
def criar_chamado():
    titulo = input("Digite o título do chamado: ")

    print("Prioridade: ")
    print("1 - Baixa")
    print("2 - Média")
    print("3 - Alta")

    prioridade_opcao = input("Escolha: ")

    if prioridade_opcao == "1":
        prioridade = "Baixa"
    elif prioridade_opcao == "2":
        prioridade = "Média"
    elif prioridade_opcao == "3":
        prioridade = "Alta"
    else:
        prioridade = "Média"

    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO chamados (titulo, status, prioridade, data_criacao) VALUES (?, ?, ?, ?)",
        (titulo, "aberto", prioridade, data)
    )
    conn.commit()

    print("Chamado criado com sucesso!")

# Listar chamados
def listar_chamados():
    cursor.execute("SELECT * FROM chamados")
    chamados = cursor.fetchall()

    if not chamados:
        print("Nenhum chamado encontrado.")
        return

    for chamado in chamados:
        print(f"ID: {chamado[0]} | Título: {chamado[1]} | Status: {chamado[2]} | Prioridade: {chamado[3]} | Data: {chamado[4]}")

# Listar apenas abertos
def listar_abertos():
    cursor.execute("SELECT * FROM chamados WHERE status = 'aberto'")
    chamados = cursor.fetchall()

    if not chamados:
        print("Nenhum chamado aberto.")
        return

    for chamado in chamados:
        print(f"ID: {chamado[0]} | Título: {chamado[1]} | Prioridade: {chamado[3]} | Data: {chamado[4]}")

# Fechar chamado
def fechar_chamado():
    listar_abertos()
    id_chamado = input("Digite o ID do chamado que deseja fechar: ")

    cursor.execute("SELECT * FROM chamados WHERE id = ?", (id_chamado,))
    chamado = cursor.fetchone()

    if chamado is None:
        print("Chamado não encontrado.")
        return

    cursor.execute("UPDATE chamados SET status = 'fechado' WHERE id = ?", (id_chamado,))
    conn.commit()

    print("Chamado fechado com sucesso!")

# Menu
while True:
    print("\n===== SISTEMA DE CHAMADOS =====")
    print("1 - Criar chamado")
    print("2 - Listar todos")
    print("3 - Listar abertos")
    print("4 - Fechar chamado")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        criar_chamado()
    elif opcao == "2":
        listar_chamados()
    elif opcao == "3":
        listar_abertos()
    elif opcao == "4":
        fechar_chamado()
    elif opcao == "5":
        break
    else:
        print("Opção inválida!")

conn.close()