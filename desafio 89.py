ficha = list()
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota1: ')) #todas essas valiaveis estão indo para a lista
    nota2 = float(input('Nota2: ')) #ficha, no casa da última onde temos ([,[],])
    media = (nota1 + nota2) / 2     #assim só mostra as notas se pedimos
    ficha.append([nome,[nota1,nota2], media])
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        print('Opção invalida')
    elif escolha == 'N':
        break
print('-=' * 30) #deixando centralizado com :< num em baixo vai os valores dai
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno?{999 interrompe}: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< Volte Sempre >>>')
