import numpy as np
import time

def ajuste_quadratico(points: list[tuple[float, float]]):
    n = len(points)
    sum_x = float(0)
    sum_y = float(0)
    sum_xy = float(0)
    sum_x2 = float(0)
    sum_x3 = float(0)
    sum_x4 = float(0)
    sum_x2y = float(0)

    for x, y in points:
        sum_x += x
        sum_y += y
        sum_xy += x*y
        sum_x2 += x*x
        sum_x3 += x*x*x
        sum_x4 += x*x*x*x
        sum_x2y += (x*x)*y

    A = np.array([
        [sum_x4, sum_x3, sum_x2],
        [sum_x3, sum_x2, sum_x],
        [sum_x2, sum_x,  n]
    ], dtype=float)

    b = np.array([
        [sum_x2y],
        [sum_xy],
        [sum_y]
    ], dtype=float)

    solucao, residuo, erro, tempo = elim_gauss(A, b)
    a = solucao[0][0]
    b = solucao[1][0]
    c = solucao[2][0]

    return a, b, c

def resolve_superior(A, b):
    n, _ = np.shape(A)
    x = np.zeros((n, 1), dtype=float)
    for i in range(n-1, -1, -1):
        x[i,0] = (b[i,0] - A[i,i:n]@x[i:n, 0])/ A[i,i]
    return x

def elim_gauss(A, b):
    inicio = time.perf_counter()
    n, _ = np.shape(A)
    aumentada = np.concatenate((A, b), axis=1)

    for i in range(n-1):
        linha_pivo_atual = i
        for j in range(i+1, n):
            if(abs(aumentada[j, i]) > abs(aumentada[linha_pivo_atual, i])):
                linha_pivo_atual = j

        if linha_pivo_atual != i:
            temp = np.copy(aumentada[i, :])
            aumentada[i, :]= aumentada[linha_pivo_atual, :]
            aumentada[linha_pivo_atual, :] = temp

        pivo = aumentada[i,i]

        if pivo == 0.0:
            raise ValueError("Erro: Pivô é 0 mesmo após pivotiamento")


        for j in range(i+1, n):
            fator = aumentada[j, i] / pivo
            aumentada[j, :] = aumentada[j, :] - fator*aumentada[i, :]

        
    U = aumentada[:, 0:n]
    y = aumentada[:, n:]
    x = resolve_superior(U, y)
    residuo = b - (A @ x)
    fim = time.perf_counter()
    tempo = fim - inicio
    return x, residuo, 0, tempo