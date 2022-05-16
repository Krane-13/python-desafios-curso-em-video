'''def lin():
    print('-'*30)
lin()
print('APRENDA PYTHON')
lin()
print('CURSO EM VÍDEO')
lin()
print('MATHEUS')
lin()'''


'''def msg(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
msg('oi')'''


'''def soma(a,b):
    s = a + b
    print(f'A = {a} e B = {b}')
    print(f'A soma de A + B ={s} ')
#Programa principal
soma(4,5)
soma(8,9)
soma(2,1)'''


'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são {tam} números')
contador(2, 1, 7)
contador(8, 0)
contador(4,4,7,6)'''


def dobra(lst):
    pos = 0
    while pos<len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3, 9, 0, 2]
dobra(valores)
print(valores)
