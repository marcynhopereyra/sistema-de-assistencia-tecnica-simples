import os
import csv


def listar_os_concluidas():
    arquivo = "ordens_servico.csv"

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        ordens = list(leitor)

    concluidas = [o for o in ordens if o['status'].lower() == "concluída"]

    if not concluidas:
        print("Nenhuma OS concluída!")
        return

    print("\n===== OS CONCLUÍDAS =====")
    for o in concluidas:
        print(f"OS: {o['id_os']} | Cliente: {o['nome_cliente']} | Serviço: {o['descricao']} | Status: {o['status']} | Data: {o['data_abertura']}")
    print("=========================\n")