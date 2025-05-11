import numpy as np
import math as m

def ReduccionGaussJordan(A):
    # proceso para fijar la fila de referencia y hallar el factor que anula el elemento correspondiente en la fila que se quiere reducir
    for i in range(filas):
        # i representa la fila que está siendo fijada
        for j in range(filas):
            # j representa la fila a comparar
            if i != j:
                if A[j, i] != 0:
                    factor = (-1) * (A[i, i] / A[j, i])
                    # multiplicar fila completa en j por factor y sumar fila en i
                    filatemp = A[i, :] + (factor) * A[j, :]
                    A[j, :] = filatemp
        
    # dividir la fila completa de referencia por el valor en la diagonal para convertir en 1
    for i in range(filas):
        A[i, :] /= (A[i, i])
    
    return A
    #fin del def de gauss jordan

# Crear una matriz identidad del mismo tamaño
def MatrizIdentidad(filas):
    I = np.zeros((filas, filas))
    for i in range(filas):
        I[i, i] = 1  # Crear la matriz identidad
    return I

filas = int(input("introduzca el número de filas y columnas, o de ecuaciones: "))
cols = filas + 1

matriz = np.zeros((filas, cols))

for i in range(filas):
    for j in range(cols):
        matriz[i, j] = float(input(f"Introduzca el elemento para la posición {i + 1}, {j + 1} de la matriz: "))

print("La matriz es:")
print(matriz) 

matriz_2 = np.copy(matriz)

# invocar la función gauss jordan
matriz_r = ReduccionGaussJordan(matriz)

print("Después de la reducción de gauss jordan:")
print(matriz_r)

# Crear la matriz identidad
matriz_iden = MatrizIdentidad(filas)

# Obtener la matriz solo con los coeficientes, sin las igualdades
matriz_coef = matriz_2[:, :-1]

# Juntar la matriz de coeficientes con la matriz identidad
matriz_ampliada = np.hstack((matriz_coef, matriz_iden))

# invocar la funcion gauss jordan para hallar la inversa
matriz_inv = ReduccionGaussJordan(matriz_ampliada)

# Extraer la matriz inversa de la parte derecha de la matriz ampliada
matriz_inv = matriz_inv[:, filas:]

print("Matriz inversa:")
print(matriz_inv)