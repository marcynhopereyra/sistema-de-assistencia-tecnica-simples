import os
import csv


def atualizar_quantidade():
    arquivo = "estoque.csv"

    id_peca = input("Digite o ID da peça que deseja atualizar: ")

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        pecas = list(leitor)

    encontrado = False

    for p in pecas:
        if p['id_peca'] == id_peca:
            print(f"Peça encontrada: {p['nome']} | Quantidade atual: {p['quantidade']}")
            nova_quantidade = int(input("Digite a nova quantidade: "))
            p['quantidade'] = nova_quantidade
            encontrado = True
            break

    if not encontrado:
        print(f"Peça com ID {id_peca} não encontrada!")
        return

    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["id_peca", "nome", "quantidade", "preco_custo", "preco_venda"])
        escritor.writeheader()
        escritor.writerows(pecas)

    print(f"Quantidade atualizada com sucesso!")