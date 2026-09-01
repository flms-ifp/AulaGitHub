import random
mega=[]
print('ola, seja bem vindo a megacena da virada')
for i in range (7):
    dig=int(input('digite um numero de 1 a 20: '))
    num=random.randint(1, 20)
    mega.append(num)
megacena=mega
print (megacena)