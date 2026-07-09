from . import editar
from . import cadastrar
from . import buscar
from . import listar
from . import deletar

def menu_cliente():
    while True:
        print("""
=============================
        Menu Cliente
 ============================       
 1 - Cadastrar Cliente
 2 - Buscar Cliente
 3 - Editar Cliente
 4 - Listar Clientes
 5 - Excluir Cliente
 0 - Voltar
=============================
""")
        try:
            opcao = int(input(" Opção Desejada: "))
            
            if opcao == 1:
                cadastrar.cadastrar_cliente()
            elif opcao == 2:
                buscar.buscar_cliente()
            elif opcao == 3:
                editar.editar_cliente()
            elif opcao == 4:
                listar.listar_clientes()
            elif opcao == 5:
                deletar.deletar_cliente()
            elif opcao == 0:
                return
            else:
                print("Opção Invalida; ")
        except ValueError:
            print(" Digite uma opção Valida: ")