import os 
import csv


def editar_cliente():
    arquivo = "clientes.csv"

    id_editar     = int(input("Digite o ID do cliente que deseja editar: "))
    novo_nome     = input("Digite o novo nome: ")
    novo_telefone = input("Digite o novo telefone: ")
    novo_email    = input("Digite o novo email: ")

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        clientes = list(leitor)

    encontrado = False

    for cliente in clientes:
        if cliente['id'] == str(id_editar):
            cliente['nome']     = novo_nome
            cliente['telefone'] = novo_telefone
            cliente['email']    = novo_email
            encontrado = True
            break

    if not encontrado:
        print(f"Cliente com ID {id_editar} não encontrado!")
        return

    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["id", "nome", "telefone", "email"])
        escritor.writeheader()
        escritor.writerows(clientes)

    print(f"Cliente ID {id_editar} atualizado com sucesso!")