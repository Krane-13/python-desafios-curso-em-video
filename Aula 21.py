'''print(input.__doc__) 
print('-='*30)
help(print)''' #Formas de descobrir o funcionamento de um comando


'''def contador(i,f,p):
    c=i
    while c <=f:
        print(f'{c}', end='..')
        c+=p
    print('FIM!')

contador(2,10,2)''' #Analisando code


'''def soma(a=0,b=0,c=0): 
    s = a + b + c
    print(f'A soma vale {s}')
soma(2,4,6)
soma(2,2)
soma(1)
soma()'''  #Parametros opicionais 


'''def teste():
    x=8 # x está servindo como uma variavel local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

    
#Program principal
n = 2 # n está servindo como uma variavel global
print(f'No progrema principal, n vale {n}')
teste()''' # escopo


'''def funcao():
    n1=4 # variavel local
    print(f'N1 dentro vale {n1}')

    
n1=2 # variavel global
funcao()
print(f'N1 fora vale {n1}')''' #escopo de variavei globais e locais



'''def soma(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = soma(3,2,5)
r2 = soma(2,2)
r3 = soma(6)

print(f'Os resultados foram {r1}, {r2}, {r3}')''' # uso de return



'''def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

n= int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''# usando return para mostrar o valor fatorial



def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um valor: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')
