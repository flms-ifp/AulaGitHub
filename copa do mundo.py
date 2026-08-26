copa2026=[
    {
    'selecao':'brazil',
    'tecnico':'acelote',
    'goleiro':'alisson',
    'titulos':5
    },

    {
    'selecao':'franca',
    'tecnico':'didier',
    'goleiro':'magnam',
    'titulos': 2
    },

    {
    'selecao':'espanha',
    'tecnico':'Luis de la fourte',
    'goleiro':'Unai',
    'titulos':1
    }
]

print('seja bem vindo a seleção da copa do mundo')
for time in copa2026:
    print(f'seleção: {time['selecao']}')
    print('tecnico: ', time['tecnico'])
    print('goleiro principa: ', time['goleiro'])
    print('quantidade de titulos: ', time['titulos'])
    print()
