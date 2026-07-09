from . import registrar_pagamento
from . import listar_pendentes
from . import relatorio_faturamento

def menu_financeiro():
    while True:
        print("""
=======================================
            Menu Financeiro
 ======================================       
 1 - Registrar Pagamento de OS
 2 - Listar OS Pendentes de Pagamento
 3 - Relatório de Faturamento (dia/mês)
 0 - Voltar
=======================================
""")
        try:
            opcao = int(input(" Opção Desejada: "))
            
            if opcao == 1:
                registrar_pagamento.registrar_pagamento()
            elif opcao == 2:
                listar_pendentes.listar_pendentes()
            elif opcao == 3:
                relatorio_faturamento.relatorio_faturamento()
            elif opcao == 0:
                return
            else:
                print("Opção Invalida; ")
        except ValueError:
            print(" Digite uma opção Valida: ")