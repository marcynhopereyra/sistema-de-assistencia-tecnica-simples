import os
import csv


def buscar_peca():
    arquivo = "estoque.csv"

    nome_busca = input("Digite o nome da peça para buscar: ")

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        pecas = list(leitor)

    encontradas = [p for p in pecas if nome_busca.lower() in p['nome'].lower()]

    if not encontradas:
        print(f"Nenhuma peça encontrada com o nome '{nome_busca}'!")
        return

    print(f"\n===== RESULTADO DA BUSCA: '{nome_busca}' =====")
    for p in encontradas:
        print(f"ID: {p['id_peca']} | Peça: {p['nome']} | Qtd: {p['quantidade']} | Custo: R$ {p['preco_custo']} | Venda: R$ {p['preco_venda']}")
    print("=============================================\n")