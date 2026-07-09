from . import cadastrar_pecas
from . import excluir_peca
from . import atualizar_quantidade
from . import buscar_peca
from . import listar_pecas


def menu_estoque():
    while True:
        print("""
=============================
        Menu Estoque
 ============================       
 1 - Cadastrar Peças
 2 - Excluir Peça
 3 - Buscar Peça
 4 - Listar Peças
 5 - Atualizar Quantidade de Peças
 0 - Voltar
=============================
""")
        try:
            opcao = int(input(" Opção Desejada: "))
            
            if opcao == 1:
                cadastrar_pecas.cadastrar_peca()
            elif opcao == 2:
                excluir_peca.excluir_peca()
            elif opcao == 3:
                buscar_peca.buscar_peca()
            elif opcao == 4:
                listar_pecas.listar_pecas()
            elif opcao == 5:
                atualizar_quantidade.atualizar_quantidade()
            elif opcao == 0:
                return
            else:
                print("Opção Invalida; ")
        except ValueError:
            print(" Digite uma opção Valida: ")