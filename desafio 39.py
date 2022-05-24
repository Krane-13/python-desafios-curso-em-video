from datetime import date #importação da condição de tempo
nasc = int(input('Ano de nascimento:')) #ler o ano de nascimento
atual = date.today().year #ler ano atual
idade = atual - nasc #calcular a idadde
print('quem nasceu em {} tem {} em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade #tempo que falta para o alistamento
    alistamento = nasc + 18 #quando foi o alistamento
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(alistamento))
elif idade > 18:
    saldo = idade - 18
    alistamento = nasc + 18
    print('você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Você deveri ter se alistado em {}.'.format(alistamento))

          
