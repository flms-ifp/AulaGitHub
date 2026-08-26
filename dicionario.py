nomes={ 'joel':'artista',
        'aldmir':'cantor',
        'luis':'genio'}
while True:
    aluno=input('digite o nome do aluno desejado: ').lower()
    if aluno in nomes:
        print(f'o aluno {aluno} é um {nomes[aluno]}')
    elif aluno not in nomes:
        add=input('digite o nome de quem deseja adicionar: ')
        add2=input('digite o que ele é: ')
        nomes[add]=add2
        print(nomes.keys())
        print(nomes.values())