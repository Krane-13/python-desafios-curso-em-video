cont = contM = contF =  0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        contM += 1
    if sexo == 'F' and idade < 20:
        contF += 1
    print('-'*30)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao total temos {contM} homens cadastredos')
print(f'eE temos {contF} mulheres com menos de 20 anos')
                                                                 
    
        
