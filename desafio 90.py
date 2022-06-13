aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-=' * 30)
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'  -{k} é igual a {v}')
