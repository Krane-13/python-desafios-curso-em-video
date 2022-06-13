lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        print('opção inválida')
    if escolha == 'N':
        break
print('-='*30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse = True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 NÃO faz parte da lista')
   
