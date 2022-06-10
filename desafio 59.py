from time import sleep
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
        total = valor1 + valor2
        print('A soma de {} + {} é {}'.format(valor1, valor2, total))
    elif opção == 2:
        total = valor1 * valor2
        print( 'A multiplicação de {} x {} é {}'.format(valor1, valor2, total))
    elif opção == 3:
        if valor1 < valor2:
            print('O {} é maior que {}'.foemat(valor2, valor1))
        elif valor1 > valor2:
            print('O {} é maior que {}'.format(valor1, valor2))
        elif valor1 == valor2:
            print('Ambos tem o mesmo valor')
    elif opção == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
    sleep(1)
print('Fim do programa! Volte sempre!')

