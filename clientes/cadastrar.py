import csv
import os
from utils import verificar_arquivo

verificar_arquivo()

def cadastrar_cliente():

    arquivo = "clientes.csv"
    
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    
    id_cliente = 1
    
    with open(arquivo, "r") as f:
        linhas = list(csv.reader(f))
        if len(linhas) > 1:
            id_cliente = int(linhas[-1][0]) + 1

    with open(arquivo, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([id_cliente, nome, telefone, email])

    print(f"Cliente '{nome}' cadastrado com ID {id_cliente}!")
