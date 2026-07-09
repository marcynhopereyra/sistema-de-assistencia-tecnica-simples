import os
import csv


def deletar_cliente():
    arquivo = "clientes.csv"

    id_deletar = int(input("Digite o ID do cliente que deseja deletar: "))

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        clientes = list(leitor)

    clientes_filtrados = [c for c in clientes if c['id'] != str(id_deletar)]

    if len(clientes_filtrados) == len(clientes):
        print(f"Cliente com ID {id_deletar} não encontrado!")
        return

    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["id", "nome", "telefone", "email"])
        escritor.writeheader()
        escritor.writerows(clientes_filtrados)

    print(f"Cliente ID {id_deletar} deletado com sucesso!")