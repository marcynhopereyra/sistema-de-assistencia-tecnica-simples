import os
import csv


def listar_pendentes():
    arquivo = "financeiro.csv"

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        pagamentos = list(leitor)

    pendentes = [p for p in pagamentos if p['status_pagamento'].lower() == "pendente"]

    if not pendentes:
        print("Nenhum pagamento pendente!")
        return

    total = sum(float(p['valor']) for p in pendentes)

    print("\n===== PAGAMENTOS PENDENTES =====")
    for p in pendentes:
        print(f"Pag: {p['id_pagamento']} | OS: {p['id_os']} | Cliente: {p['nome_cliente']} | Valor: R$ {float(p['valor']):.2f} | Data: {p['data_pagamento']}")
    print(f"\nTotal pendente: R$ {total:.2f}")
    print("================================\n")