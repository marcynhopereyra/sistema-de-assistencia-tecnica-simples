import os
import csv

def verificar_arquivo_financeiro():
    arquivo = "financeiro.csv"

    if not os.path.exists(arquivo):
        with open(arquivo, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["id_pagamento", "id_os", "nome_cliente", "valor", "forma_pagamento", "status_pagamento", "data_pagamento"])
        print("Arquivo 'financeiro.csv' criado com sucesso!")

def verificar_arquivo_estoque():
    arquivo = "estoque.csv"

    if not os.path.exists(arquivo):
        with open(arquivo, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["id_peca", "nome", "quantidade", "preco_custo", "preco_venda"])
        print("Arquivo 'estoque.csv' criado com sucesso!")

def verificar_arquivo_os():
    arquivo = "ordens_servico.csv"
    if not os.path.exists(arquivo):
        with open(arquivo, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["id_os", "id_cliente", "nome_cliente", "descricao", "status", "data_abertura"])
        print("Arquivo 'ordens_servico.csv' criado com sucesso!")

def verificar_arquivo():
    arquivo = "clientes.csv"

    if not os.path.exists(arquivo):
        with open(arquivo, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["id", "nome", "telefone", "email"])
        print("Arquivo 'clientes.csv' criado com sucesso!")
    else:
        print("Arquivo 'clientes.csv' já existe!")
        
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
 
def pausar():
    input("\nPressione ENTER para continuar...")