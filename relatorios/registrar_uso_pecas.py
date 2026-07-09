import os
import csv


def registrar_uso_peca():
    arquivo_uso   = "uso_pecas.csv"
    arquivo_estoque = "estoque.csv"

    if not os.path.exists(arquivo_uso):
        with open(arquivo_uso, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["id_os", "id_peca", "nome_peca", "quantidade_usada"])

    id_os          = input("Digite o número da OS: ")
    id_peca        = input("Digite o ID da peça usada: ")
    quantidade_usada = int(input("Digite a quantidade usada: "))

    with open(arquivo_estoque, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        pecas = list(leitor)

    peca_encontrada = None
    for p in pecas:
        if p['id_peca'] == id_peca:
            peca_encontrada = p
            break

    if not peca_encontrada:
        print(f"Peça ID {id_peca} não encontrada no estoque!")
        return

    if int(peca_encontrada['quantidade']) < quantidade_usada:
        print(f"Estoque insuficiente! Disponível: {peca_encontrada['quantidade']}")
        return

    with open(arquivo_uso, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([id_os, id_peca, peca_encontrada['nome'], quantidade_usada])

    for p in pecas:
        if p['id_peca'] == id_peca:
            p['quantidade'] = int(p['quantidade']) - quantidade_usada
            break

    with open(arquivo_estoque, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["id_peca", "nome", "quantidade", "preco_custo", "preco_venda"])
        escritor.writeheader()
        escritor.writerows(pecas)

    print(f"Peça '{peca_encontrada['nome']}' registrada na OS {id_os}!")
    print(f"Estoque atualizado! Nova quantidade: {int(peca_encontrada['quantidade']) - quantidade_usada}")