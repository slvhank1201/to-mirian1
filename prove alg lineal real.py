import numpy as np

# Coeficientes de los vectores u1, u2, u3 y v
A = np.array([[1, 2, 1], [-3, -4, -5], [2, -1, 7]])
v = np.array([1, -2, 5])

# Resolver el sistema de ecuaciones lineales
c = np.linalg.solve(A, v)

# Mostrar los coeficientes c1, c2 y c3
print("c1 =", c[0])
print("c2 =", c[1])
print("c3 =", c[2])