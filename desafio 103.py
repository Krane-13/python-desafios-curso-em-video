def jog(nome = '<desconhecido> ', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

n = str(input('nome do jogador:'))
g = str(input('número de gols:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jog(gol=g)
else:
    jog(n,g)
