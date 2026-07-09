from . import faturamento_por_periodo
from . import os_por_status
from . import pecas_mais_usadas
from . import registrar_uso_pecas

def menu_Relatorios():
    while True:
        print("""
=============================
        Menu Relatórios
 ============================       
 1 - OS por Status
 2 - Faturamento por Período
 3 - Registrar uso de Peças 
 4 - Peças mais Usadas
 0 - Voltar
=============================
""")
        try:
            opcao = int(input(" Opção Desejada: "))
            
            if opcao == 1:
                os_por_status.relatorio_os_por_status()
            elif opcao == 2:
                faturamento_por_periodo.relatorio_faturamento_periodo()
            elif opcao == 3:
                registrar_uso_pecas.registrar_uso_peca()
            elif opcao == 4:
                pecas_mais_usadas.relatorio_pecas_mais_usadas()
            elif opcao == 0:
                return
            else:
                print("Opção Invalida; ")
        except ValueError:
            print(" Digite uma opção Valida: ")