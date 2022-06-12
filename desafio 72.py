cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito','nove',
        'dez','onze','doze','treze','catorze',
        'quize','dezesseis','dezesete','dezoito',
        'dezenove','vinte')
while True:
    resp = ' ' 
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print('Tente novamente.',end=' ')
    print(f'Você digitou o número {cont[n]}')
    while resp not in 'SN':
        resp = str(input('Continuar?')).strip().upper()[0]
    if resp == 'N':
        print('fim')
        break
    
