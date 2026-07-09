import os
import csv
import datetime
from utils import verificar_arquivo_financeiro

def registrar_pagamento():
    verificar_arquivo_financeiro()
    arquivo = "financeiro.csv"
   
    id_pagamento = 1
    id_os        = input("Digite o número da OS: ")
    nome_cliente = input("Digite o nome do cliente: ")
    valor        = float(input("Digite o valor do serviço: "))

    print("\nForma de pagamento:")
    print("1 - Dinheiro")
    print("2 - Pix")
    print("3 - Cartão")
    opcao = input("Escolha uma opção: ")

    formas = {
        "1": "Dinheiro",
        "2": "Pix",
        "3": "Cartão"
    }

    if opcao not in formas:
        print("Opção inválida!")
        return

    forma_pagamento  = formas[opcao]

    print("\nStatus do pagamento:")
    print("1 - Pago")
    print("2 - Pendente")
    opcao_status = input("Escolha uma opção: ")

    status_opcoes = {
        "1": "Pago",
        "2": "Pendente"
    }

    if opcao_status not in status_opcoes:
        print("Opção inválida!")
        return

    status_pagamento = status_opcoes[opcao_status]
    data_pagamento   = datetime.date.today().strftime("%d/%m/%Y")

    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = list(csv.reader(f))
        if len(linhas) > 1:
            id_pagamento = int(linhas[-1][0]) + 1

    with open(arquivo, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([id_pagamento, id_os, nome_cliente, valor, forma_pagamento, status_pagamento, data_pagamento])

    print(f"Pagamento Nº {id_pagamento} registrado com sucesso!")
    print(f"Cliente: {nome_cliente} | Valor: R$ {valor:.2f} | Forma: {forma_pagamento} | Status: {status_pagamento}")