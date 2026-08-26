num_pessoas=[]
while True:
    print('ola')
    print('seja bem vindo, o que deseja fazer?')
    print('a) cadastrar o nome do usuario')
    print('b) deletar quem saiu da sala')
    print('c) exibir quantas pessoas estão na sala e quem são')
    print('d) sair da sala')
    op=input('digite a opcao desejada: ')
    if op=='a':
        nome=input('digite o nome do usuario: ')
        if num_pessoas<20:
            num_pessoas.append(nome)
        elif num_pessoas==20:
            print('limite maximo de pessoas atingido (20)')
        print()
        continue
    elif op=='b':
        delete=input('digite o nome do usuario que deseja remover: ')
        num_pessoas.remove(delete)
        print()
        continue
    elif op=='c':
        quant=len(num_pessoas)
        print(f'a quantidade de pessoas é {quant} e as pessoas são {num_pessoas}')
        print()
        continue
    elif op=='d':
        print('ok, tchau')
        break