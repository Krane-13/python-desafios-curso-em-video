def fatorial(n):
    f=1
    for c in range(1,n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triblo (n):
    return n*3


def imc(m,a):
    mc = m / a ** 2
    return mc