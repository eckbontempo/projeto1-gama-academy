import Tela


produto = []
lista_cadastrados = []

def MenuCadastro():
    while True:
        Tela.LimpaTela()
        print('Olá! Estamos agora que estamos no menu de cadastro, digite o número de uma das opções abaixo para ser redirecionado novamente: ')
        print('1. Cadastrar produto;')
        print('2. Listar produtos cadastrados;')
        print('3. Deleção de produtos;')
        print('4. Voltar Para o Menu de Navegação;')
        num = int(input("Digite o que deseja: "))
        if num == 1:
            while True:
                Tela.LimpaTela()
                nome = str(input('Digite o nome do produto: '))
                preco = float(input('Qual o preço: R$ '))
                produto.append(nome)
                produto.append(preco)
                print(f'Nome do produto: {nome} ===> Preço: R$ {preco:.2f}')
                print('Parabéns, seu produto foi cadastrado com sucesso!')
                lista_cadastrados.append(produto[:])
                novo = str(input('Cadastrar novo produto? [S/N]'))
                while novo not in "SsNn":
                    print('Código inválido!')
                    novo = str(input('Digite [S] p/ sim ou [N] p/ não: '))
                produto.clear()
                if novo in 'Nn':
                    break
        elif num == 2:
            print('Lista de produtos cadastrados: ')
            cont_01 = 0
            print('=+' * 30)
            print(f'{"Código":<7}{"Nome do Produto":<20}{"Preço":>10}')
            print('=+' * 30)
            while cont_01 < len(lista_cadastrados):
                print(f'{cont_01:^7}{lista_cadastrados[cont_01][0]:.<20}R${lista_cadastrados[cont_01][1]:.>8.2f}')
                cont_01 += 1
        elif num == 3:
            while True:
                print('[ÁREA DE DELEÇÃO] Lista de produtos cadastrados [ÁREA DE DELEÇÃO] ')
                cont_01 = 0
                print('=+' * 30)
                print(f'{"Código":<7}{"Nome do Produto":<20}{"Preço":>10}')
                print('=+' * 30)
                while cont_01 < len(lista_cadastrados):
                    print(f'{cont_01:^7}{lista_cadastrados[cont_01][0]:.<20}R${lista_cadastrados[cont_01][1]:.>8.2f}')
                    cont_01 += 1
                deletar = str(input('Quer deletar algum produto? [S/N]')).strip()[0]
                while deletar not in "SsNn":
                    print('Código inválido!')
                    deletar = str(input('Digite [S] p/ sim ou [N] p/ não: '))
                while True:
                    if deletar in "Ss:":
                        while True:
                            num_del = int(input('Digite o código do produto a ser deletado: '))
                            if 0 <= num_del <= len(lista_cadastrados) - 1:
                                del lista_cadastrados[num_del]
                                print('Produto deletado com sucesso!')
                                break
                            else:
                                print('Código de produto inválido!')
                        print('O que deseja fazer agora?')
                        print('1. Deletar outro produto.')
                        print('2. Voltar.')
                        num = int(input('Digite a opção: '))
                        if num == 1:
                            print()
                        elif num == 2:
                            break
                    else:
                        break
        elif num == 4:
            break
MenuCadastro()