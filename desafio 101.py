def voto():
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        #print(f'Com {idade} anos: NÃO VOTA')
         return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65 :
        #print(f'Com {idade} anos: VOTO OPICIONAL')
        return f'Com {idade} anos: VOTO OPICIONAL'
    else:
        #print(f'Com {idade} anos: VOTO OBRIGADORIO')
        return f'Com {idade} anos: VOTO OBRIGADORIO'
            
#Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto())
