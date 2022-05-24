casa = float(input('Valor da casa: R$')) #valor casa
salário = float(input('Salário do comprador: R$')) #salário do comprador
ano = int(input('Quantos anos para pagar:')) # quantos anos para pagar
prestação = casa / (ano * 12) #multiplicando o ano pelos total de meses e
#dividindo pelo valor da casa para saber a prestação por mês
pagar = salário * 0.30 #os 30% do salário do comprador
print('Para uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa,ano,prestação))
if prestação <= pagar:
    print('Emprêstimo APROVADO!')
else:
    print('Empêstimo NEGADO')

#print(casa)
#print(salário)
#print(ano)
#print(prestação)
 
