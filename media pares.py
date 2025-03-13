x = int(input("Digite la cantidad de valores que desea tener en cuenta: ")) #Se le pide al usuario la cantidad de valores que tendra en cuenta el programa
n = 0
c = 0
for i in range(x + 1):  #se generan los numeros desde 0 hasta la variable dada por el usuario
    if i % 2 == 0 : #se evalua si el numero generado es par
        n = n + i
        c = c + 1
b = n // c
print(f"La media de los numeros pares que hay hasta el valor {x} es: {b}") #se imprime la media de los numeros pares que hay hasta la variable dada por el usuario