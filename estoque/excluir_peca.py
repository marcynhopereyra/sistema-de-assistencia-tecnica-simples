import os
import csv


def excluir_peca():
    arquivo = "estoque.csv"

    id_excluir = input("Digite o ID da peça que deseja excluir: ")

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        pecas = list(leitor)

    pecas_filtradas = [p for p in pecas if p['id_peca'] != id_excluir]

    if len(pecas_filtradas) == len(pecas):
        print(f"Peça com ID {id_excluir} não encontrada!")
        return

    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["id_peca", "nome", "quantidade", "preco_custo", "preco_venda"])
        escritor.writeheader()
        escritor.writerows(pecas_filtradas)

    print(f"Peça ID {id_excluir} excluída com sucesso!")