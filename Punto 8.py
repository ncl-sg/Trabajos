n = int(input("Ingrese un número entero positivo: "))
nuevo_n = ""
while n > 0:
    c = (n % 10) + 1
    if c == 10:
        c = 0
    nuevo_n= str(c) + nuevo_n
    n //= 10
print("Nuevo número:", nuevo_n)