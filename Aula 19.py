'''pessoas = {'nome' : 'Matheus', 'sexo': 'M', 'idade': 16}
print(pessoas)'''

'''pessoas = {'nome': 'Matheus','sexo': 'M', 'idade': 16}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')'''

'''pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 16}
print(pessoas.keys())'''

'''pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 16 }
print(pessoas.values())'''

'''pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 16}
print(pessoas.items())'''

'''pessoas ={ 'nome': 'Matheus', 'sexo': 'M','Idade': 16}
pessoas['Peso'] = 68.7
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
#Usando dicionario com lista
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['Sigla'])'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v)
