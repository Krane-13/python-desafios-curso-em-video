'''num = [2, 5, 9, 1]
print(num)'''

'''num = [2, 5, 9, 1]
num [2] = 3
print(num)'''

'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,0)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')'''


'''num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.insert(2,0)
num.sort(reverse=True)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Chaguei ao final da lista.')'''


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
    if v == 13: # curiosidade
        print('Você digitou um valor surpresa')
print('Cheguei ao final da lista')


'''a = [2, 3, 4, 7] # isso está aginto como uma ligação
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Liast B: {b}')'''


'''a = [2, 3, 4, 7] # isso está funcionando como uma copia sem alterar o original
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''


