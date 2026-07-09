import os
import csv


def relatorio_pecas_mais_usadas():
    arquivo = "uso_pecas.csv"

    if not os.path.exists(arquivo):
        print("Nenhum uso de peças registrado ainda!")
        return

    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        usos = list(leitor)

    if not usos:
        print("Nenhum uso de peças registrado!")
        return

    contagem = {}

    for uso in usos:
        nome  = uso['nome_peca']
        qtd   = int(uso['quantidade_usada'])

        if nome in contagem:
            contagem[nome] += qtd
        else:
            contagem[nome] = qtd

    ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    print("\n========================================")
    print("       PEÇAS MAIS USADAS                ")
    print("========================================")
    posicao = 1
    for nome, total in ranking:
        print(f"  {posicao}º  {nome:<25} : {total} unidades usadas")
        posicao += 1
    print("========================================\n")