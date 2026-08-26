produtos = [
    {'sabor': 'chocolate', 'preco': 3.00, 'estoque': 20},
    {'sabor': 'morango', 'preco': 2.50, 'estoque': 50},
    {'sabor': 'baunilha', 'preco': 4.00, 'estoque': 10}
]

while True:
    print('Olá, seja bem-vinda à minha loja!')

    for item in produtos:
        print(f"Sabor: {item['sabor']} Valor: R${item['preco']}")

    loja = input('Deseja comprar alguma coisa? ').lower()
    if loja == 'sim' or loja == 's':

        op = input('Digite o sabor: ').lower()

        if op == 'chocolate':
            print(f"Estoque disponível: {produtos[0]['estoque']}")
            quanti = int(input('Digite quantos você deseja comprar: '))
            if quanti > produtos[0]['estoque']:
                print(f"Não temos essa quantidade, temos apenas {produtos[0]['estoque']}")
            else:
                produtos[0]['estoque'] -= quanti
                print("Compra realizada!")

        elif op == 'morango':
            print(f"Estoque disponível: {produtos[1]['estoque']}")
            quanti = int(input('Digite quantos você deseja comprar: '))
            if quanti > produtos[1]['estoque']:
                print(f"Não temos essa quantidade, temos apenas {produtos[1]['estoque']}")
            else:
                produtos[1]['estoque'] -= quanti
                print("Compra realizada!")

        elif op == 'baunilha':
            print(f"Estoque disponível: {produtos[2]['estoque']}")
            quanti = int(input('Digite quantos você deseja comprar: '))
            if quanti > produtos[2]['estoque']:
                print(f"Não temos essa quantidade, temos apenas {produtos[2]['estoque']}")
            else:
                produtos[2]['estoque'] -= quanti
                print("Compra realizada!")

        else:
            print("Sabor não encontrado!")

    else:
        print('Ok, encerrando atendimento.')
        break