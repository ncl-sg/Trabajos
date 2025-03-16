def convertir_base(n, b):
    resultado = ""
    while n > 0:
        r = n % b
        if r >= 10:
            resultado = chr(55 + r) + resultado  # Convierte 10-15 en A-F para base 16
        else:
            resultado = str(r) + resultado
        n //= b
    return resultado if resultado else "0"
n = int(input("Ingrese un número entero: "))
print("Base 2:", convertir_base(n, 2))
print("Base 4:", convertir_base(n, 4))
print("Base 8:", convertir_base(n, 8))
print("Base 16:", convertir_base(n, 16))