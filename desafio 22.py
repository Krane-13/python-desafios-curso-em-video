nome = str(input('Qual o seu nome completo:')).strip()
print('analisando seu nome...')
print('O nome em maiusculo é: {}'.format(nome.upper()))
print('O nome em minusculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letra'.format(nome.find(' ')))
