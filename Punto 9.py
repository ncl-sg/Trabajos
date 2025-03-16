lim = int(input("Ingrese un número entero: "))
a, b = 0, 1
while a <= lim:
    print(a)
    a, b = b, a + b