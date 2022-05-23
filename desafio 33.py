a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('terceiro valor:'))
#vendo menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#vendo maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número é o {}'.format(menor))
print('O maior número é o {}'.format(maior))
    
