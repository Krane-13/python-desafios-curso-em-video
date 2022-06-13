bon = '-'*40
listagem = ('Lápis',1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)
print(bon)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(bon)
for pos in range(len(listagem)):
    if pos % 2 == 0 :
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print(bon)
