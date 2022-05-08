nome = str(input('Qual o seu nome?')).strip().title()#lendo o nome
if nome == 'Matheus': #colocando uma condição
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': #outras condições
    print('Seu nome é bem popular no Brasil.')
else: #finalização
    print('Seu nome é bem comum')
print('tenha um bom dia, {}!'.format(nome))
