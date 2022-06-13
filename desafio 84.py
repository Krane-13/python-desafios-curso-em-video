lista = []
princ = []
maior = menor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista [1] < menor:
            menor = lista[1]
    princ.append(lista[:])
    lista.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp not in 'SN':
        print('opção invalida')
    elif resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior pesso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1]== maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')

for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
