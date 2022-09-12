produtos = {}

while True:
    print('=' * 30)
    print('=' * 30)
    print(f'{"MENU DE CADASTRO":^30}')
    print('=' * 30)
    print('=' * 30)
    print('O que deseja fazer?')
    print('1. Cadastrar produto.')
    print('2. Listar produtos cadastrados.')
    print('3. Deleção de produtos')
    print('4. Voltar/Sair')
    num = int(input("Digite o que deseja: "))
    if num == 1:
        while True:
            print('=' * 30)
            print('=' * 30)
            nome = str(input('Digite o nome do produto: '))
            preco = float(input('Qual o preço: R$ '))
            produtos[nome] = preco
            print(nome,' ===> ', produtos[nome])
            print('=' * 30)
            novo = str(input('Cadastrar novo produto? [S/N]'))
            if novo in 'Nn':
                print('.\n.\n.\n')
                break
    elif num == 2:
        print('.\n.\n.\n')
        print('Lista de produtos cadastrados: ')
        print(produtos)
    elif num == 3:
        print('Em construção...')
    elif num == 4:
        print('.\n.\n.\n')
        break