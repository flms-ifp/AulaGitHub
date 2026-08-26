numeros = []
numeros2 = []

while True:
    num=int(input('Digite um número: '))
    qtd=len(numeros)
    if qtd<30:
        numeros.append(num)
    else:
        print('numero maximo atingido (30)')

    if num%2 == 0: 
        multi=num*2
        numeros2.append(multi)
    else: 
        multi2=num*3
        numeros2.append(multi2)

    print(numeros)
    print(numeros2)