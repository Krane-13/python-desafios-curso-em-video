salário = float(input('Qual o salário do funcionário?'))
if salário > 1250:
    ganho = salário + (salário * 0.10)
else:
    ganho = salário + (salário * 0.15)
print('Quem ganhava {} passa a ganhar R${:.2f} agora.'.format(salário, ganho))
