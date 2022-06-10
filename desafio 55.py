maior = 0
menor = 0 
for pess in range(1, 6):
    peso = float(input('Pesso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg \ne o menor peso foi {}Kg'.format(maior, menor), end='')
