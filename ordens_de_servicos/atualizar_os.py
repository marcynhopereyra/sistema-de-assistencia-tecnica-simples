import os
import csv


def atualizar_status_os():
    arquivo = "ordens_servico.csv"

    id_os = input("Digite o número da OS que deseja atualizar: ")

    print("\nEscolha o novo status:")
    print("1 - Aberta")
    print("2 - Em andamento")
    print("3 - Concluída")
    opcao = input("Escolha uma opção: ")

    status_opcoes = {
        "1": "Aberta",
        "2": "Em andamento",
        "3": "Concluída"
    }

    if opcao not in status_opcoes:
        print("Opção inválida!")
        return

    novo_status = status_opcoes[opcao]

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        ordens = list(leitor)

    encontrado = False

    for ordem in ordens:
        if ordem['id_os'] == id_os:
            ordem['status'] = novo_status
            encontrado = True
            break

    if not encontrado:
        print(f"OS Nº {id_os} não encontrada!")
        return

    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["id_os", "id_cliente", "nome_cliente", "descricao", "status", "data_abertura"])
        escritor.writeheader()
        escritor.writerows(ordens)

    print(f"OS Nº {id_os} atualizada para '{novo_status}' com sucesso!")