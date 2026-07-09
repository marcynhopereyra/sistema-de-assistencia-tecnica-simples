import os
import csv


def listar_os_abertas():
    arquivo = "ordens_servico.csv"

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        ordens = list(leitor)

    abertas = [o for o in ordens if o['status'].lower() in ["aberta", "em andamento"]]

    if not abertas:
        print("Nenhuma OS em aberto!")
        return

    print("\n===== OS EM ABERTO =====")
    for o in abertas:
        print(f"OS: {o['id_os']} | Cliente: {o['nome_cliente']} | Serviço: {o['descricao']} | Status: {o['status']} | Data: {o['data_abertura']}")
    print("========================\n")