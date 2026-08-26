pacientes={}
medicos={}

print('ola seja bem vindo ao hospital regional de catende')
print('digite 1 para adicionar, 2 para consultar,3 para atender, 4 para remover')
op=input('digite a opção que deseja fazer:')

if op==1:
    tipo=input('quem voçe deseja adicionar? medico ou paciente? ')    
    if tipo=='medico':
        add1=('digite o nome do medico:')
        add2=('digite sua area de especialização:')
        medicos[add1]=add2

    elif tipo=='paciente':
        add3=('digite o nome do nova paciente: ')
        add4=('digite o que esse paciente tem: ')
        pacientes[add3]=add4

elif op==2:
    busca=input('digite o nome do paciente ou medico que deseja consultar: ')
    print('consultado...')
    if busca in pacientes:
        print(f'o paciente {busca} possui {pacientes[busca]}')

    elif busca in medicos:
        print(f'o medico {busca} é especializado em {medicos[busca]}')
            
elif op==3:
    atendimento=('digite o paciente que vai ser atendido:')

    if atendimento in pacientes:
        print(f'o paciente {atendimento} possui {pacientes[atendimento]}')

        atendi2=input('quem sera o medico responsavel pelo paciente? ')
        if atendi2 in medicos:
                print('tratamento em andamento...')