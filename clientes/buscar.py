import os
import csv


def buscar_cliente():
    arquivo = "clientes.csv"

    nome_busca = input("Digite o nome do cliente que deseja buscar: ")
    
    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        clientes = list(leitor)

    encontrados = []

    for cliente in clientes:
        if nome_busca.lower() in cliente['nome'].lower():
            encontrados.append(cliente)

    if not encontrados:
        print(f"Nenhum cliente encontrado com o nome '{nome_busca}'!")
        return

    print(f"\n===== RESULTADO DA BUSCA: '{nome_busca}' =====")
    for cliente in encontrados:
        print(f"ID: {cliente['id']} | Nome: {cliente['nome']} | Telefone: {cliente['telefone']} | Email: {cliente['email']}")
    print("=============================================\n")