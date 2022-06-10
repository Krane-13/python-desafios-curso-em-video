from random import randint
computador = randint(0,10)#escolhe um número
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')
acertou = False
palpites = 0
while  not acertou:
   jogador = int(input('Qual é seu palpite? ')) # le o valor atribuido
   palpites += 1 # vai somar os palpites necessarios
   if jogador == computador: # se for igual 
       acertou = True
   else:
        if jogador < computador: # se for menor vai dizer mais
            print('Mais...')
        elif jogador > computador:# se for menor vai dizer menos
            print('Menos...')
print('Acertou com {} palpites!tentativas. Parabéns!'.format(palpites))
