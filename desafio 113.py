def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO com o tipo de dado digitado, digite um valor inteiro')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não informar esse valor')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO, por favor digite um número REAL válido')
            continue
        except(KeyboardInterrupt):
            print('Ussuário preferiu não informar esse valor')
            return 0
        else:
            return n

num1 = leiaint('Digite um número Inteiro: ')
num2 = leiafloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {num1} ')
print(f'O valor real digitado foi {num2}')
