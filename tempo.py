import time
def calculadora():
    num1=int(input('digite o primeiro numero: '))
    num2=int(input('digite o segndo numero: '))
    op=input('qual a operação a ser efetuada? ')
    
    if op=='soma':
        mais=num1+num2
        print('calculando...')
        time.sleep(5)
        print(mais)

    elif op=='subtração':
        menos=num1-num2
        print('calculando...')
        time.sleep(5)
        print(menos)

    elif op=='divisão':
        divi=num1/num2
        print('calculando...')
        time.sleep(5)
        print(divi)

    elif op=='multiplicação':
        multi=num1*num2
        print('calculando...')
        time.sleep(5)
        print(multi)

    else:
        print('opção não encontrada')
while True:
    time.sleep(2)
    print('ola') 
    time.sleep(5)
    calculadora()