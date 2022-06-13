from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados {cont} valores')
    print(f'O maior valor foi {maior}')

#PROGRAMA
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
