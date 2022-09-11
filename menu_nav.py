import os
import boas_vindas
def nav( ):

    os.system("cls")
    red2 = int(input('Digite o número de uma das opções abaixo: \n 1 - Menu de Cadastro; \n 2 - Menu de Vendas; \n 3 - Voltar.\n'))
    if red2 == 1:
        print()
    elif red2 == 2:
        print()
    elif red2 == 3:
        boas_vindas.vindas()
