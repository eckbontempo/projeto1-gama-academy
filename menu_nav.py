import menu_cadastro
import menu_vendas
import Tela


def nav():
    Tela.LimpaTela()
    print('Que bom que está continuando com a gente! Você está sendo redirecionada (o) para o nosso menu de navegação!')
    print()
    red2 = int(input(
        'Digite o número de uma das opções abaixo: \n 1 - Menu de Cadastro; \n 2 - Menu de Vendas; \n 3 - Voltar.\n'))
    if red2 == 1:
        menu_cadastro.MenuCadastro()
    elif red2 == 2:
        menu_vendas.menu_vendas()
    elif red2 == 3:
        return
