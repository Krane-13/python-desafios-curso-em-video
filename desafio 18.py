import math
angulo = float(input('Coloque o ângulo desejado:'))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO valendo {:.2f}'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO valendo {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE valendo {:.2f}'.format(angulo, tangente))
