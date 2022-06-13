num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    escolha = str(input('Quer continuar? [S/N]')).strip().upper()
    if escolha not in 'SN':
        print('Opção inválida')
    elif escolha == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {num}')
print(f'a lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
                     
