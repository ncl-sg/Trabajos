import numpy as np

filas = int(input("introduzca el número de filas y columnas, o de ecuaciones: "))
cols = filas + 1

matriz = np.zeros((filas, cols))

for i in range(filas):
    for j in range(cols):
        matriz[i, j] = float(input(f"Introduzca el elemento para la posición {i + 1}, {j + 1} de la matriz: "))

print("La matriz es:")
print(matriz) 

matriz_coef = matriz[:, :-1]

matriz2 = np.zeros((filas, filas))

for i in range(filas):

    for j in range(filas):
        matriz2[j, i] = matriz_coef[i, j]
        
print(matriz2)