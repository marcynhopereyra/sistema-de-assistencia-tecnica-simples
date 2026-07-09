import os
import csv


def relatorio_faturamento():
    arquivo = "financeiro.csv"

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        pagamentos = list(leitor)

    if not pagamentos:
        print("Nenhum pagamento registrado!")
        return

    total_geral    = sum(float(p['valor']) for p in pagamentos)
    total_pago     = sum(float(p['valor']) for p in pagamentos if p['status_pagamento'].lower() == "pago")
    total_pendente = sum(float(p['valor']) for p in pagamentos if p['status_pagamento'].lower() == "pendente")

    total_dinheiro = sum(float(p['valor']) for p in pagamentos if p['forma_pagamento'].lower() == "dinheiro" and p['status_pagamento'].lower() == "pago")
    total_pix      = sum(float(p['valor']) for p in pagamentos if p['forma_pagamento'].lower() == "pix"      and p['status_pagamento'].lower() == "pago")
    total_cartao   = sum(float(p['valor']) for p in pagamentos if p['forma_pagamento'].lower() == "cartão"   and p['status_pagamento'].lower() == "pago")

    qtd_pagamentos = len(pagamentos)
    qtd_pagos      = len([p for p in pagamentos if p['status_pagamento'].lower() == "pago"])
    qtd_pendentes  = len([p for p in pagamentos if p['status_pagamento'].lower() == "pendente"])

    print("\n========================================")
    print("        RELATÓRIO DE FATURAMENTO        ")
    print("========================================")
    print(f"  Total de pagamentos : {qtd_pagamentos}")
    print(f"  Pagos               : {qtd_pagos}")
    print(f"  Pendentes           : {qtd_pendentes}")
    print("----------------------------------------")
    print(f"  Total faturado      : R$ {total_geral:.2f}")
    print(f"  Total recebido      : R$ {total_pago:.2f}")
    print(f"  Total pendente      : R$ {total_pendente:.2f}")
    print("----------------------------------------")
    print("  Recebido por forma de pagamento:")
    print(f"    Dinheiro          : R$ {total_dinheiro:.2f}")
    print(f"    Pix               : R$ {total_pix:.2f}")
    print(f"    Cartão            : R$ {total_cartao:.2f}")
    print("========================================\n")