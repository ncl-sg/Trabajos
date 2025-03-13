while True:
    n = int(input("Digite el valor que desea evaluar:")) #se le pide al usuario el numero que desea evaluar
    if n >= 0: #si el numero es mayor o igual a 0 se rompe el bucle y continua evaluando
        break
    else : #si el numero es menor que 0 (negativo) entonces el bucle continua y solicita un nuevo numero
        print("El numero no es positivo")
if n ** 0.5 % 1 == 0: #evalua si el numero tiene raiz cuadrada entera
    print(f"El numero {n} SI tiene raiz cuadrada entera") #imprime si tiene raiz cuadrada entera
else :
    print(f"El numero {n} NO tiene raiz cuadrada entera")  #imprime si no tiene raiz cuadrada entera