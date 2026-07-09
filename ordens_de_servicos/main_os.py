from . import nova_os
from . import buscar_os
from . import cancelar_os
from . import atualizar_os
from . import listar_os_abertas
from . import listar_os_concluidas

def menu_os():
    while True:
        print("""
=============================
    Menu Ordens De Serviço
 ============================       
 1 - Abrir Nova OS
 2 - Buscar OS
 3 - Atualizar Status da OS
 4 - Listar OS em Aberto
 5 - Listar OS Concluídas
 6 - Cancelar OS
 0 - Voltar
=============================
""")
        try:
            opcao = int(input(" Opção Desejada: "))
            
            if opcao == 1:
                nova_os.abrir_os()
            elif opcao == 2:
                buscar_os.buscar_os()
            elif opcao == 3:
                atualizar_os.atualizar_status_os()
            elif opcao == 4:
                listar_os_abertas.listar_os_abertas()
            elif opcao == 5:
                listar_os_concluidas.listar_os_concluidas()
            elif opcao == 6:
                cancelar_os.cancelar_os()
            elif opcao == 0:
                return
            else:
                print("Opção Invalida; ")
        except ValueError:
            print(" Digite uma opção Valida: ")