import os
import csv


def buscar_os():
    arquivo = "ordens_servico.csv"

    id_busca = input("Digite o número da OS: ")

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        ordens = list(leitor)

    encontrada = None

    for o in ordens:
        if o['id_os'] == id_busca:
            encontrada = o
            break

    if not encontrada:
        print(f"OS Nº {id_busca} não encontrada!")
        return

    print("\n===== ORDEM DE SERVIÇO =====")
    print(f"OS:       {encontrada['id_os']}")
    print(f"Cliente:  {encontrada['nome_cliente']}")
    print(f"Serviço:  {encontrada['descricao']}")
    print(f"Status:   {encontrada['status']}")
    print(f"Data:     {encontrada['data_abertura']}")
    print("============================\n")