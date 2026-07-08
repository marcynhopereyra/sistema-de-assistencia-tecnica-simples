import os
from utils import limpar_tela, pausar
from clientes import main_cliente
from estoque import main_estoque
from financeiro import main_financeiro
from ordens_de_servicos import main_os
from relatorios import main_relatorios


def menu_principal():
    while True:
        limpar_tela()
        print("""
===========================================
      Sistema de Assistência Técnica
===========================================
    1 - Clientes
    2 - Ordens De Serviços
    3 - Estoque / Peças
    4 - Financeiro
    5 - Relatórios
    0 - Sair
===========================================
    """)
        try:
            opcao = int(input(" Opção Desejada: "))
                
            if opcao == 1:
                main_cliente.menu_cliente()
            elif opcao == 2:
                main_os.menu_os()
            elif opcao == 3:
                main_estoque.menu_estoque()
            elif opcao == 4:
                main_financeiro.menu_financeiro()
            elif opcao == 5:
                main_relatorios.menu_Relatorios()
            elif opcao == 0:
                print(" Encerrando... ")
                break
            else:
                print("Opção Invalida: ")
                pausar()
        except ValueError:
            print("Digite uma Opção valida: ")
            pausar()

if __name__ == "__main__":
 menu_principal()
