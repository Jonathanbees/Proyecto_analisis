import numpy as np


def SOR(x0, A, b, Tol, niter, w):
    c = 0
    error = Tol + 1
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    E = []

    while error > Tol and c < niter:
        T = np.linalg.inv(D - w * L) @ ((1 - w) * D + w * U)
        C = w * np.linalg.inv(D - w * L) @ b
        x1 = T @ x0 + C
        E.append(np.linalg.norm(x1 - x0, np.inf))
        error = E[-1]
        x0 = x1
        c += 1

    if error < Tol:
        s = x0
        print(f'es una aproximación de la solución del sistema con una tolerancia= {Tol}')
    else:
        s = x0
        print(f'Fracasó en {niter} iteraciones')

    return E, s


# Ejemplo de uso
x0 = np.array([0, 0, 0])  # Ejemplo de vector inicial
A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])  # Ejemplo de matriz A
b = np.array([1, 2, 3])  # Ejemplo de vector b
Tol = 1e-5
niter = 100
w = 1.25

E, s = SOR(x0, A, b, Tol, niter, w)
print("Errores:", E)
print("Solución:", s)
