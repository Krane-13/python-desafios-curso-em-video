'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''


n = int(input('Digite um número para calacular seu fatoria: '))# recebe o valor
c = n
f = 1 # para ter multiplicação limpa tem que ser 1
print('Calculando {}! = '.format(n), end= '')
while c > 0: # se valor maneor que 0
    print('{} '.format(c),end='') # mostra o valor
    print(' x ' if c > 1 else ' = ', end='') #mostra os sinais de x e =
    f *= c # calcula o fatorial
    c -= 1 #vai diminuar o valor de n
print('{}'.format(f))# mostra o fatorial
