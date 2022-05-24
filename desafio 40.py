nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segundo nota:'))
média = (nota1 + nota2) / 2
print('tirando {:.1f} e {:.1f}, a média do aluno será {:.1f}'.format(nota1,nota2,média))
if média >= 7:
    print('O aluno está APROVADO.')
elif média >= 5:
    print('O aluno está de RECUPERAÇÂO.')
elif média < 5:
    print('O aluno está REPROVADO.')
    
 
