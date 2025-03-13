n1 = int(input("Digite el primer valor a evaluar:")) #solicita al usuario el primer valor a evaluar
n2 = int(input("Digite el segundo valor a evaluar:")) #solicita al usuario el segundo valor a evaluar
if (n1 % 2 == 0 and n2 % 2 == 0) or (n1 % 2 == 1 and n2 % 2 == 1): #si ambos valores son pares o impares, halla el mcd
    if n1 < n2:
        for i in range(1, n1 + 1, 1):
            if n1 % i == 0 and n2 % i == 0:
                mcd = i
    else :
        if n1 > n2:
            i = 1
            while i <= n2:
                if n1 % i == 0 and n2 % i == 0:
                    mcd = i
                i = i + 1
        else:
            mcd = n1
    print(f"El maximo comun divisor es: {mcd}") #imprime el mcd de ambos numeros
else : #sino quiere decir que uno es par y el otro impar, por lo que halla el mcm
    if n1 != n2:
        if n1 > n2:
            max = n1
        else:
            max = n2
        for i in range(n1 * n2, max - 1, -1) :
            if i % n1 == 0 and i % n2 == 0:
                mcm = i
    else:
        mcm = n1
    print(f"El minimo comun multiplo es: {mcm}") #imprime el mcm de ambos numeros