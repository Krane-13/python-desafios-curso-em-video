print('==' * 10)
print('GERADOR DE PA')
print('==' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
c = 1
total= 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} - '.format(termo), end = '')
        termo += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('A progração foi finalizadda com {} termos mostrados'.format(total))

