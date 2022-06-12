preço = total = totalmil = menor = cont = 0
barato = ' '
while True:
    resp = ' '
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('preço: R$'))
    cont += 1
    total += preço
    if total >= 1000:
        totalmil += 1
    if cont == 1 or preço < menor: #assim que faz o menor
        menor = preço
        barato = produto
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total  da compra foi R${total:.2f}')
print(f'Temos {totalmil} produto custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
    
