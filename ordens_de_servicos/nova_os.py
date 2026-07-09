import os
import csv
import datetime
from utils import verificar_arquivo_os


def abrir_os():
    verificar_arquivo_os()
    
    arquivo = "ordens_servico.csv"
    
    id_os = 1
    id_cliente   = input("Digite o ID do cliente: ")
    nome_cliente = input("Digite o nome do cliente: ")
    descricao    = input("Descreva o serviço a ser realizado: ")
    status       = "Aberta"
    data_abertura = datetime.date.today().strftime("%d/%m/%Y")
    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = list(csv.reader(f))
        if len(linhas) > 1:
            id_os = int(linhas[-1][0]) + 1
    with open(arquivo, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([id_os, id_cliente, nome_cliente, descricao, status, data_abertura])
    print(f"OS Nº {id_os} aberta com sucesso para o cliente '{nome_cliente}'!")