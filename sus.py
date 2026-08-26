import time
pacientes={}
medicos={}

while True:
    print('ola seja bem vindo ao hospital regional de catende')
    time.sleep(1)
    print('digite 1 para adicionar, 2 para consultar,3 para atender, 4 para remover')
    op=int(input('digite a opção que deseja fazer:'))
    if op==1:
        adicionador=int(input('quem voçe deseja adicionar? medico ou paciente?[1/2]: '))
        if adicionador==1:
            add1=input('digite o nome do medico:')
            add2=input('digite sua area de especialização:')
            medicos[add1]=add2

        elif adicionador==2:
            add3=input('digite o nome do nova paciente: ')
            add4=input('digite o que esse paciente tem: ')
            pacientes[add3]=add4

    elif op==2:
        busca=input('digite o nome do paciente ou medico que deseja consultar: ')
        print('consultado...')
        time.sleep(10)
        if busca in pacientes:
            print(f'o paciente {busca} possui {pacientes[busca]}')
        elif busca in medicos:
            print(f'o medico {busca} é especializado em {medicos[busca]}')   

    elif op==3:
        atendimento=input('digite o paciente que vai ser atendido:')
        if atendimento in pacientes:
            print(f'o paciente {atendimento} possui {pacientes[atendimento]}')
            atendi2=input('quem sera o medico responsavel pelo paciente? ')
            if atendi2 in medicos:
                print('tratamento em andamento...')
                time.sleep(200)

    elif op==4:
        remocao=input('digite o nome de quem deseja remover: ')
        if remocao in pacientes:
            del pacientes[remocao]
        elif remocao in medicos:
            del medicos[remocao]

    elif op==5:
        print('sindo')
        break