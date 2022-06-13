lista = [[],[]]
valor = 0
for v in range(1,8):
    valor = int(input(f'Digite o {v}º. Valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-=' * 30)
lista[0].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
lista[1].sort()
print(f'Os valores ímpares digitados foram: {lista[1]}')
    
