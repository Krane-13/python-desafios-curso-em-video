from random import randint
from time import sleep
computador = randint(0,5)#O computador está sorteando um número 
print('-=-' *20) #Criar linhas para deixar bonito
print('vou pensa em um número entre 0 e 5. Tente adivinhar')
print('-=-' *20)
jogador = int(input('Em qual número eu pensei?'))
print('Pocessando...')
sleep(2)#Faz o computadoe esperar para mostrar o resultado
if computador == jogador:
    print('Você acertou, PARABENS!!!')
else:
    print('Que pena você errou, eu pensei no número {} e não no número {}'.format(computador,jogador))
