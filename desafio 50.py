num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        tot +=1
        print(' ESSE' )
    else:
        print(' NÃO')
    print('{}'.format(c))
print('O número {} foi dvidível {} vezes'.format(num, tot))
if tot ==2:
    print('É por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')
