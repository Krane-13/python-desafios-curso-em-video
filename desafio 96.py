def area (larg,comp):
    a = larg * comp
    print(f'A área de um terreno {larg} X {comp} é de {a}m².')
def msg (txt):
    print(txt)
    print('-'*30)

#Programa principal    
msg('Controle de Terrenos')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
