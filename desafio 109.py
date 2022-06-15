import moeda

p= float(input('Digite p preço R$'))
print(f'A metade de {moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumento 10%, temos {moeda.aumento(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13)}')
