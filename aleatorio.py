import random
mega=[]
respostas=[]
acertos=0
print('ola, seja bem vindo a megacena da virada')
for i in range(7):
    dig=int(input('digite um numero de 1 a 60: '))
    if dig<60:
        respostas.append(dig)

    elif dig>60:
        print('numero não aceito')

    num=random.randint(1, 60)
    mega.append(num)
    for m,r in zip(mega, respostas):
        if m == r:
            acertos+=1
            print(acertos)

