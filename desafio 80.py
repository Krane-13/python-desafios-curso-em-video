lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:#se ele é o primeiro ou se é maior que o último
        lista.append(n)
        print('Adicionado ao final da lista!')
    else:
        pos = 0
        while pos  < len(lista):
            if n <= lista[pos]:#se não é nenhum dos outros ele é adicionado em outra posição
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
