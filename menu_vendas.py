from menu_cadastro import lista_cadastrados
import Tela

carrinho = []

def menu_vendas():
    while True:
        Tela.LimpaTela()
        print('Olá! Agora que estamos no menu de Vendas, digite o número de uma das opções abaixo para ser redirecionado novamente: ')
        print('1. Listar produtos no carrinho;')
        print('2. Adicionar produtos no carrinho;')
        print('3. Excluir produtos do carrinho;')
        print('4. Finalizar compra;')
        print('5. Voltar Para o Menu de Navegação;')

        while True:
            print('')
            opc = input("Digite o que deseja: ")
            if opc not in '12345' or len(opc) > 1: 
                print('Código inválido!')
            else:
                break

        if opc == '1':
            ### erro no cadastro
            Tela.LimpaTela()
            print('Carrinho')
            print('Veja os itens dentro do carrinhos: ')
            while True:
                if len(carrinho) > 0:
                    cont_01 = 0
                    print('=+' * 19)
                    print(f'{"Código":<7}{"Nome do Produto":<20}{"Preço":>10}')
                    print('=+' * 19)
                    while cont_01 < len(carrinho):
                        print(f'{cont_01:^7}{carrinho[cont_01][0]:.<20}R${carrinho[cont_01][1]}')
                        cont_01 += 1  

                else:
                    print()
                    print('Carrinho está vázio, adicione um produto para seguir com a finalização da compra')
                pergunta = input('Mostrar novamente? [S/N]')   
                if pergunta in 'Nn':
                    break


        elif opc == '2':
            while True:
                Tela.LimpaTela()
                print('Veja a lista de produtos cadastrados: ')
                print()
                if len(lista_cadastrados) > 0:
                    cont_02 = 0
                    print('=+' * 19)
                    print(f'{"Código":<7}{"Nome do Produto":<20}{"Preço":>10}')
                    print('=+' * 19)
                    while cont_02 < len(lista_cadastrados):
                        print(f'{cont_02:^7}{lista_cadastrados[cont_02][0]:.<20}R${lista_cadastrados[cont_02][1]}')
                        cont_02 += 1
                    print('')
                    cod_produto = int(input('Digite o código do produto a ser adicionado ao carrinho: '))
                    while True:
                        if 0 <= cod_produto <= len(lista_cadastrados) - 1:
                            print(f'O Produto {lista_cadastrados[cod_produto][0]} adicionado com sucesso!')
                            carrinho.append(lista_cadastrados[cod_produto][:])
                            print(carrinho)
                            break
                        else:
                            print('Código de produto inválido!')
                            cod_produto = int(input('Digite o código do produto a ser adicionado ao carrinho: '))
                else:
                    print('Nenhum produto cadastrado!')

                print('O que deseja fazer agora?')
                print('1. Adicionar outro produto ao carrinho.')
                print('2. Voltar.')

                num = input('Digite a opção: ')

                while num not in "12":
                    print('Código inválido!')

                    num = input('Digite a opção: ')

                if num == '1':
                    print()

                elif num == '2':
                    break

                

        elif opc == '3':
            cont_01 = 0
            while True:
                Tela.LimpaTela()
                print('[ATENÇÃO! ÁREA DE DELEÇÃO] ')
                print('Veja a lista de produtos cadastrados no carrinho: ')
                if len(carrinho) > 0:
                    cont_01 = 0
                    print('=+' * 19)
                    print(f'{"Código":<7}{"Nome do Produto":<20}{"Preço":>10}')
                    print('=+' * 19)
                    while cont_01 < len(carrinho):
                        print(f'{cont_01:^7}{carrinho[cont_01][0]:.<20}R${carrinho[cont_01][1]:}')
                        cont_01 += 1
                    deletar = str(input('Quer deletar algum produto? [S/N] ')).strip()[0]
                    while deletar not in "SsNn":
                        print('Código inválido!')
                        deletar = str(input('Digite [S] p/ sim ou [N] p/ não: '))
                    if deletar in "Ss:":
                        num_del = int(input('Digite o código do produto a ser deletado: '))
                        while True:
                            if 0 <= num_del <= len(carrinho) - 1:
                                print(f'O Produto {carrinho[num_del][0]} foi deletado com sucesso!')
                                del carrinho[num_del]
                                break
                            else:
                                print('Código de produto inválido!')
                                num_del = int(input('Digite o código do produto a ser deletado: '))
                    else:
                        break   
                    
        elif opc == '4':
            while True:
                Tela.LimpaTela
                print('Finalização de compras')
                if len(carrinho) > 0:
                    soma = 0
                    for c in range (0, len(carrinho)):
                        soma = soma + carrinho[c][1]
                    print(f'A soma dos produtos do carrinho deu R${soma}')
                else:
                    print('Carrinho vazio')

                pergunta = input('Deseja mostrar novamente? [S/N]')   
                if pergunta in 'Nn':
                    break

        elif opc == '5':
            carrinho.clear()
            print()
            break

