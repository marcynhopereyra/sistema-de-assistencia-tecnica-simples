import os
import csv


def relatorio_os_por_status():
    arquivo = "ordens_servico.csv"

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        ordens = list(leitor)

    if not ordens:
        print("Nenhuma OS registrada!")
        return

    abertas      = [o for o in ordens if o['status'].lower() == "aberta"]
    em_andamento = [o for o in ordens if o['status'].lower() == "em andamento"]
    concluidas   = [o for o in ordens if o['status'].lower() == "concluída"]

    print("\n========================================")
    print("         RELATÓRIO DE OS POR STATUS     ")
    print("========================================")
    print(f"  Total de OS         : {len(ordens)}")
    print("----------------------------------------")
    print(f"  Abertas             : {len(abertas)}")
    for o in abertas:
        print(f"    OS {o['id_os']} | {o['nome_cliente']} | {o['data_abertura']}")
    print("----------------------------------------")
    print(f"  Em andamento        : {len(em_andamento)}")
    for o in em_andamento:
        print(f"    OS {o['id_os']} | {o['nome_cliente']} | {o['data_abertura']}")
    print("----------------------------------------")
    print(f"  Concluídas          : {len(concluidas)}")
    for o in concluidas:
        print(f"    OS {o['id_os']} | {o['nome_cliente']} | {o['data_abertura']}")
    print("========================================\n")