from defs115 import *
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu (['Cadastrar Pessoa', 'Lista pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        print('opção 2')
    elif resposta == 3:
        print('Saindo do sistema... Até logo')
        break
    else:
        print('ERRO! Digite uma opção válida!')
