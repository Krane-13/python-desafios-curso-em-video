from defs115 import *

while True:
    resposta = menu(['Cadastrar Pessoa', 'Lista Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print('opção 1')
    elif resposta == 2:
        print('opção 2')
    elif resposta == 3:
        print('saindo do sistema... Até logo')
        break
    else:
        print('ERRO! Digite uma opção válida!')
            
        
