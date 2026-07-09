import os
import csv
import datetime


def relatorio_faturamento_periodo():
    arquivo = "financeiro.csv"

    data_inicio = input("Digite a data de início (dd/mm/aaaa): ")
    data_fim    = input("Digite a data de fim (dd/mm/aaaa): ")

    try:
        inicio = datetime.datetime.strptime(data_inicio, "%d/%m/%Y")
        fim    = datetime.datetime.strptime(data_fim,    "%d/%m/%Y")
    except ValueError:
        print("Data inválida! Use o formato dd/mm/aaaa")
        return

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        pagamentos = list(leitor)

    filtrados = []

    for p in pagamentos:
        data_pag = datetime.datetime.strptime(p['data_pagamento'], "%d/%m/%Y")
        if inicio <= data_pag <= fim:
            filtrados.append(p)

    if not filtrados:
        print(f"Nenhum pagamento encontrado entre {data_inicio} e {data_fim}!")
        return

    total_geral    = sum(float(p['valor']) for p in filtrados)
    total_pago     = sum(float(p['valor']) for p in filtrados if p['status_pagamento'].lower() == "pago")
    total_pendente = sum(float(p['valor']) for p in filtrados if p['status_pagamento'].lower() == "pendente")

    print("\n========================================")
    print("     FATURAMENTO POR PERÍODO            ")
    print("========================================")
    print(f"  Período: {data_inicio} até {data_fim}")
    print("----------------------------------------")
    for p in filtrados:
        print(f"  Pag {p['id_pagamento']} | OS {p['id_os']} | {p['nome_cliente']} | R$ {float(p['valor']):.2f} | {p['status_pagamento']} | {p['data_pagamento']}")
    print("----------------------------------------")
    print(f"  Total no período    : R$ {total_geral:.2f}")
    print(f"  Total recebido      : R$ {total_pago:.2f}")
    print(f"  Total pendente      : R$ {total_pendente:.2f}")
    print("========================================\n")