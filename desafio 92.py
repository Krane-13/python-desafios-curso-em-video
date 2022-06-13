from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Data de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = int(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35 - datetime.now().year) 
print('-='*30)
for k,v in dados.items():
    print(f'{k} tem o valor {v}')

