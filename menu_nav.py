import menu_cadastro
import menu_vendas
import Tela

def nav():
    executar = True
    while executar:
        Tela.LimpaTela()
        print('Que bom que está continuando com a gente! Você está sendo redirecionada (o) para o nosso menu de navegação!')
        print()
        red2 = str(input('Digite o número de uma das opções abaixo: \n 1 - Menu de Cadastro; \n 2 - Menu de Vendas; \n 3 - Voltar. \n Digite o que deseja: '))
        while red2 not in '123':
            print('Por favor, digite o valor 1, 2 ou 3. \n Digite o que deseja: ')
            red2 = str(input())
        if red2 == '1':
            menu_cadastro.MenuCadastro()
        elif red2 == '2':
            menu_vendas.menu_vendas()
        elif red2 == '3':
           executar = False
        
