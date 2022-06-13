num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não atribuido')
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r not in 'SN':
        print('Opção inválida')
    if r == 'N':
        break
    num.sort()
print(f'Você digitou os valores {num}')
