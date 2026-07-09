import os
import csv


def listar_clientes():
    arquivo = "clientes.csv"

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        clientes = list(leitor)

    if not clientes:
        print("Nenhum cliente cadastrado!")
        return

    print("\n===== LISTA DE CLIENTES =====")
    for cliente in clientes:
        print(f"ID: {cliente['id']} | Nome: {cliente['nome']} | Telefone: {cliente['telefone']} | Email: {cliente['email']}")
    print("=============================\n")