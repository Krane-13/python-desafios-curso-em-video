velocidade = float(input('qual a velocidade atual de um carro?'))
if velocidade <= 80 :
                 print('Tenha um bom dia! Digija com segurança!')
else:
    pagar = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(pagar))
    print('Tenha um bom dia! Dirija com segurança!')
                 
