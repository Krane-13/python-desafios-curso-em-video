'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

'''n = 0
while n != 999:
    n =int(input('Digite um número: '))'''

'''cont = n = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1'''

n = s = 0
while True:
    n = int(input('digite um número: [parar 999] '))
    if n == 999:
        break
    s +=n
print('A soma dos valores é {}'.format(s))
