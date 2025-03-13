while True:
    p = int(input("Digite el numero al cual se le buscara el primo mas cercano (tenga en cuenta que debe ser mayor de 2): ")) #Se le pide al usuario que digite el valor hasta el cual se evaluara
    if p > 2:
        break #Si el numero es mayor que 2 se rompe el bucle y pasa a evaluar
    else:
        print("El numero no es mayor que 2") #Si el numero es menor que 2 el bucle continua y se le pide un nuevo numero al usuario
for n in range(2 , p + 1): #Se iteran los numeros de 2 hasta p
    d = 0
    m = 1
    while m <= n: #en el bucle se evalua si n es divisible entre m  y se repite hasta que m=n
        if n % m == 0: 
            d += 1
        m += 1
    if d == 2 : #Se evalua si el numero n tiene igual a 2 divisores, si es asi significa que es primo
        a = n
print(f"El primo menor o igual mas cercano a {p} es: {a}") #Se imprime el numero primo menor o igual mas cercano
