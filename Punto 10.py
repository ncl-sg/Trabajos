x = int(input("Ingrese un número entero: "))
a, b = 0, 1
while a <= x:
    a, b = b, a + b
print("Siguiente número de Fibonacci:", a)