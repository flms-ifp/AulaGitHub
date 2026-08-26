import random
estoque = [
    {'quantidade_pacotes': 40, 'preco_pacote': 7.00},
    {'capa_mole': 15.00, 'capa_dura': 20.00,'premiun':30.00}
]
album=[]
grupo={}

def comprar_pacote():
    print(f'a quantidade de pacotes é de {estoque[0]['quantidade_pacotes']}')
    quanti = int(input('Quantos pacotes você deseja comprar? '))
    if quanti <= estoque[0]['quantidade_pacotes']:
        total = quanti * estoque[0]['preco_pacote']
        estoque[0]['quantidade_pacotes'] -= quanti
        print(f'Valor da compra: R${total}')
        print(f"Restam {estoque[0]['quantidade_pacotes']} pacotes")
        print()
    else:
        print(f"Temos apenas {estoque[0]['quantidade_pacotes']} pacotes")
        print()


def comprar_album():
    print('temos 3 tipos de album')
    print(f'1- capa mole R${estoque[1]['capa_mole']}')
    print(f'2- capa dura R${estoque[1]['capa_dura']}')
    print(f'3- ptremiun R${estoque[1]['premiun']}')
    tipo = int(input('Qual álbum deseja? 1, 2 ou 3? '))
    if tipo == 1:
        print(f"Preço do álbum: R${estoque[1]['capa_mole']}")
        print('Compra realizada')
        print()

    elif tipo == 2:
        print(f"Preço do álbum: R${estoque[1]['capa_dura']}")
        print('Compra realizada')
        print()
    
    elif tipo == 3:
        print(f"Preço do álbum: R${estoque[1]['premiun']}")
        print('Compra realizada')
        print()

    else:
        print('Tipo inválido')
        print()


def inscrever_grupo():
    inscri = input('Deseja se inscrever no grupo? ').lower()
    if inscri=='sim' or inscri== 's':
        info_nome=input('digite seu nome: ')
        grupo['nome']=info_nome

        info_numero=input('digite seu numero de telefone: ')
        grupo['numero de telefone']=info_numero

        info_email=input('digite seu email: ')
        grupo['email']=info_email
    else:
        print('Inscrição cancelada')
    print()

def pacotes():
    abrir=input('deseja abrir um pacote?')
    if abrir=='sim':
        
        print('abrindo')
        fig_aleatorias1=random.randint(1,980)
        fig_aleatorias2=random.randint(1,980)
        fig_aleatorias3=random.randint(1,980)
        fig_aleatorias4=random.randint(1,980)
        fig_aleatorias5=random.randint(1,980)
        fig_aleatorias6=random.randint(1,980)
        fig_aleatorias7=random.randint(1,980)
        print(f'suas figurinhas são: {fig_aleatorias1},{fig_aleatorias2},{fig_aleatorias3},{fig_aleatorias4},{fig_aleatorias5},{fig_aleatorias6},{fig_aleatorias7}')
        print()


def menu():
    while True:
        print('Ola seja bme vindo a Loja de figurinhas, o que deseja fazer?')
        print('1 Comprar pacote')
        print('2 Comprar álbum')
        print('3 Entrar no grupo')
        print('4 Sair')
        print('5 abrir pacotes')

        op = int(input('Digite a opção: '))
        if op == 1:
            comprar_pacote()

        elif op == 2:
            comprar_album()

        elif op == 3:
            inscrever_grupo()

        elif op == 4:
            print('Saindo da loja...')
            break

        elif op == 5:
            pacotes()

        else:
            print('Opção inválida')
            print()
menu()