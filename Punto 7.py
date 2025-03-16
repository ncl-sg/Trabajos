pos = 0
neg = 0
suma_pos = 0
suma_neg = 0
while True:
    n = int(input("Ingrese un número entero (0 para terminar): "))
    if n == 0:
        break
    elif n > 0:
        pos += 1
        suma_pos += n
    else:
        neg += 1
        suma_neg += n
print("Cantidad de positivos:", pos)
print("Promedio de positivos:", suma_pos / pos if pos > 0 else 0)
print("Cantidad de negativos:", neg)
print("Promedio de negativos:", suma_neg / neg if neg > 0 else 0)