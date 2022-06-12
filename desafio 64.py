n = c = total = 0 # colocar n dentro e fora tira a soma de 999 pelo n indicado
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c +=1
    total += n
    n = int(input('Digite um número [999 para parar]: ')) 
print('Você digitou {} números e a soma entre eles foi {}'.format(c , total))
 
