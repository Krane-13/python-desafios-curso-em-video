galera = list()
dados = dict()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip()
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas com M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    galera.append(dados.copy())
    while True:
        esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if esc in 'SN':
            break
        print('ERRO! REsponda apenas com S ou N.')
    if esc == 'N':
        break
print('-=' *30)
print(f'A)Ao todo temos {len(galera)} pessoas cadastradas.') 
media = soma/ len(galera)
print(f'B)A média de idade é de {media:5.2f} anos')
print('C)As mulheres cadastradas foram' , end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}' , end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v} ' , end='')
        print()
print('<< ENCERRADO >>')
