
import Tela


produto = []
lista_cadastrados = []

def MenuCadastro():
    while True:
        Tela.LimpaTela()
        print('Olá! Agora que estamos no menu de cadastro, digite o número de uma das opções abaixo para ser redirecionado novamente: ')
        print('1. Cadastrar produto;')
        print('2. Listar produtos cadastrados;')
        print('3. Deleção de produtos;')
        print('4. Voltar Para o Menu de Navegação;')
        while True:
            num = input("Digite o que deseja: ")
            if num not in '1234':
                print('Código inválido!')
            else:
                break
        if num == '1':
            while True:
                Tela.LimpaTela()
                while True:
                    nome = input('Digite o nome do produto: ')
                    if nome.isalpha() == True:
                        break
                    else:
                        print('Nome inválido! O nome pode conter apenas letras.')
                while True:
                    preco = input('Qual o preço: R$ ').replace(',','.')
                    validador = 0
                    for i, v in enumerate(preco):
                        if preco[i] in "0123456789.":
                            validador += 1
                    if validador == len(preco):
                        preco = float(preco)
                        break
                    else:
                        print('Preço inválido! Digite apenas números.')
                       
                produto.append(nome)
                produto.append(preco)
                print(f'Nome do produto: {nome} \nPreço: R$ {preco:.2f}')
                print('Parabéns! Seu produto foi cadastrado com sucesso!')
                lista_cadastrados.append(produto[:])
                novo = str(input('Cadastrar novo produto? [S/N] '))[0]
                while novo not in "SsNn":
                    print('Código inválido!')
                    novo = str(input('Digite [S] p/ sim ou [N] p/ não: '))[0]
                produto.clear()
                if novo in 'Nn':
                    break
        elif num == '2':
            while True:
                Tela.LimpaTela()
                print('Lista de produtos cadastrados: ')
                if len(lista_cadastrados) > 0:
                    cont_01 = 0
                    print('=+' * 19)
                    print(f'{"Código":<7}{"Nome do Produto":<20}{"Preço":>10}')
                    print('=+' * 19)
                    while cont_01 < len(lista_cadastrados):
                        print(f'{cont_01:^7}{lista_cadastrados[cont_01][0]:.<20}R${lista_cadastrados[cont_01][1]:.>8.2f}')
                        cont_01 += 1
                else:
                    print('=+' * 19)
                    print('Nenhum produto cadastrado!')
                    print('=+' * 19)
                pergunta = str(input('Mostrar lista novamente? [S/N] '))
                while pergunta not in "SsNn":
                    print('Código inválido!')
                    pergunta = str(input('Digite [S] p/ sim ou [N] p/ não: '))
                if pergunta in 'Ss':
                    print()
                elif pergunta in 'Nn':
                    break
        elif num == '3':
            while True:
                Tela.LimpaTela()
                print('[ATENÇÃO! ÁREA DE DELEÇÃO] ')
                print('Veja a lista de produtos cadastrados: ')
                if len(lista_cadastrados) > 0:
                    cont_01 = 0
                    print('=+' * 19)
                    print(f'{"Código":<7}{"Nome do Produto":<20}{"Preço":>10}')
                    print('=+' * 19)
                    while cont_01 < len(lista_cadastrados):
                        print(f'{cont_01:^7}{lista_cadastrados[cont_01][0]:.<20}R${lista_cadastrados[cont_01][1]:.>8.2f}')
                        cont_01 += 1
                    deletar = str(input('Quer deletar algum produto? [S/N] ')).strip()[0]
                    while deletar not in "SsNn":
                        print('Código inválido!')
                        deletar = str(input('Digite [S] p/ sim ou [N] p/ não: '))
                    if deletar in "Ss:":
                        num_del = int(input('Digite o código do produto a ser deletado: '))
                        while True:
                            if 0 <= num_del <= len(lista_cadastrados) - 1:
                                print(f'O Produto {lista_cadastrados[num_del][0]} foi deletado com sucesso!')
                                del lista_cadastrados[num_del]
                                break
                            else:
                                print('Código de produto inválido!')
                                num_del = int(input('Digite o código do produto a ser deletado: '))
                    else:
                        break
                else:
                    print('Nenhum produto cadastrado!')
                print('O que deseja fazer agora?')
                print('1. Deletar outro produto.')
                print('2. Voltar.')
                num = input('Digite a opção: ')
                while num not in "12":
                    print('Código inválido!')
                    num = input('Digite a opção: ')

                if num == '1':
                    print()
                elif num == '2':
                    break
        elif num == '4':
            break
#MenuCadastro()