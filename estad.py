import random as rnd

def media(lA):
    maxA = len(lA)
    suma = 0
    for i in range(maxA):
        suma += lA[i]
       
    if maxA > 0 :
        return suma / maxA
    else :
        return float("nan")
    
def var(lA, muestral = True):
    maxA = len(lA)
    suma = 0
    promedio = media(lA)
    for i in range(maxA):
        suma += (A[i] - promedio) ** 2
    if maxA > 0 and muestral == False :
        return suma / maxA
    elif maxA > 2 :
        return suma / (maxA - 1)
    else :
        return float("nan")
    

n = int(input("n: "))
A = []

for i in range(n):
    A.append(rnd.randint(1, 100))
    
print(A)
print(f"El promedio es {media(A)}, la varianza es {var(A, False)} ")


