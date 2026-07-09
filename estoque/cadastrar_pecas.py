import os 
import csv
from utils import verificar_arquivo_estoque


def cadastrar_peca():
    verificar_arquivo_estoque()
    
    arquivo = "estoque.csv"
    id_peca = 1

    nome        = input("Digite o nome da peça: ")
    quantidade  = int(input("Digite a quantidade em estoque: "))
    preco_custo = float(input("Digite o preço de custo: "))
    preco_venda = float(input("Digite o preço de venda: "))

    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = list(csv.reader(f))
        if len(linhas) > 1:
            id_peca = int(linhas[-1][0]) + 1

    with open(arquivo, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([id_peca, nome, quantidade, preco_custo, preco_venda])

    print(f"Peça '{nome}' cadastrada com ID {id_peca}!")