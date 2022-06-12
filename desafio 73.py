times = ('Flamengo','Internacional','Atletico-MG','São Paulo',
         'Fluminense','Grêmio','Palmeiras','Santos',
         'Athleticos-PR','Bragantino','Ceará SC','Corinthians',
         'Atletico-GO','Bahia','Sport Recife','Fortaleza',
         'Vasco da Grama','Goiás','Coritiba','Botafogo')#31/03/2021
bon = '-='*30
print(bon)
print(f'Lista de times do Brasileirão: {times}')
print(bon)
print(f'Os 5 primeiros são {times[0:5]}')
print(bon) 
print(f'Os 4 últimos são {times[-4:]}')
print(bon)
print('Times em ordem alfabetica',sorted(times))
print(bon)
print(times.index('Atletico-MG')+1)
