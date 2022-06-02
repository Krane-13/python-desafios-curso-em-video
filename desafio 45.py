from random import randint # para poder ser gerar um negocio aleatorio
from time import  sleep
itens = ('Pedra', 'Papel', 'Tesoura', 'JOGADA INVÁLIDA') # as opções
computador = randint(0, 2)
print('''Suas opções;
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?')) # a escolha do jogador
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=' * 10)#deixa bonito
print('O computador escolheu {}'.format(itens[computador])) #jogada do computador
print('Jogador jogou {}'.format(itens[jogador])) #jogada do user
print('-=' * 10) #deixar bonito
if computador == 0: #jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    else :
        print('JOGADA INVÁLIDA')         
elif computador == 1:#jogou PAPEL
    if jogador == 0:
        print('JOGADOR PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else :
        print('JOGADA INVÁLIDA')
elif computador == 2: #jogou TESOURA
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('JOGADOR PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else :
        print('JOGADA INVÁLIDA')
