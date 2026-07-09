import os
import csv


def cancelar_os():
    arquivo = "ordens_servico.csv"

    id_cancelar = input("Digite o número da OS que deseja cancelar: ")

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        ordens = list(leitor)

    ordens_filtradas = [o for o in ordens if o['id_os'] != id_cancelar]

    if len(ordens_filtradas) == len(ordens):
        print(f"OS Nº {id_cancelar} não encontrada!")
        return

    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["id_os", "id_cliente", "nome_cliente", "descricao", "status", "data_abertura"])
        escritor.writeheader()
        escritor.writerows(ordens_filtradas)

    print(f"OS Nº {id_cancelar} cancelada com sucesso!")