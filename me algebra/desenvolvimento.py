import math

TOL = 1e-5
MAX_ITER = 1000


def f(x):
    return 4 + x * math.cos(x)


def df(x):
    return math.cos(x) - x * math.sin(x)


def bisseccao(a, b):
    if f(a) * f(b) > 0:
        raise ValueError("O intervalo precisa conter uma mudança de sinal.")

    for iteracao in range(1, MAX_ITER + 1):
        meio = (a + b) / 2

        if (b - a) / 2 < TOL:
            return meio, iteracao

        if f(a) * f(meio) <= 0:
            b = meio
        else:
            a = meio

    raise RuntimeError("Bissecção não convergiu.")


def newton(x):
    for iteracao in range(1, MAX_ITER + 1):
        derivada = df(x)
        if derivada == 0:
            raise ZeroDivisionError("A derivada se anulou durante o método.")

        proximo = x - f(x) / derivada

        if abs(proximo - x) < TOL:
            return proximo, iteracao

        x = proximo

    raise RuntimeError("Newton não convergiu.")


def secantes(x0, x1):
    for iteracao in range(1, MAX_ITER + 1):
        denominador = f(x1) - f(x0)
        if denominador == 0:
            raise ZeroDivisionError("Não foi possível calcular a próxima secante.")

        proximo = x1 - f(x1) * (x1 - x0) / denominador

        if abs(proximo - x1) < TOL:
            return proximo, iteracao

        x0, x1 = x1, proximo

    raise RuntimeError("Secantes não convergiu.")


intervalos = [(8.3, 8.4), (10.6, 10.7)]

for indice, (a, b) in enumerate(intervalos, start=1):
    chute = (a + b) / 2

    raiz_bis, iter_bis = bisseccao(a, b)
    raiz_newton, iter_newton = newton(chute)
    raiz_sec, iter_sec = secantes(a, b)

    print(f"\nRaiz positiva {indice}:")
    print(f"Bissecção: {raiz_bis:.5f} ({iter_bis} iterações)")
    print(f"Newton:    {raiz_newton:.5f} ({iter_newton} iterações)")
    print(f"Secantes:  {raiz_sec:.5f} ({iter_sec} iterações)")