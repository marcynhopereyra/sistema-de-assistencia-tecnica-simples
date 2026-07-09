import os
import csv


def listar_pecas():
    arquivo = "estoque.csv"

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        pecas = list(leitor)

    if not pecas:
        print("Nenhuma peça cadastrada no estoque!")
        return

    print("\n===== ESTOQUE DE PEÇAS =====")
    for p in pecas:
        print(f"ID: {p['id_peca']} | Peça: {p['nome']} | Qtd: {p['quantidade']} | Custo: R$ {p['preco_custo']} | Venda: R$ {p['preco_venda']}")
    print("============================\n")