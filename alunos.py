alunos=[{'nome':'fabio',
                'data_de_nascimento':'32/08/2009',
                'cpf':'112.937.000-00',
                'rg': '1111111',
                'telefone':'40228922'}
]
print(alunos[0]['nome'])

while True:
    add=input('deseja add alunos? ')
    if add=='sim' or 's':
        nome=input('digite seu nome:')
        alunos['nome']=nome

        nascimento=input('digite sua data de nascimento: ')
        if nascimento < 11111111 or nascimento > 31129999:
            print('data de nascimento invalida')
        alunos['data_de_nascimento']=nascimento

        cpf=input('digite seu cpf:')
        alunos['cpf']=cpf

        rg=input('digite seu rg: ')
        alunos['rg']=rg

        telefone=input('digite seu numero de telefone:')
        alunos['telefone']=telefone

        print(alunos)
    elif add=='não' or 'n':
        print('ok')
        print(alunos[0][nome])
        break