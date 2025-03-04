n = int(input("Introduzca n: "))
nbak = n
m = 0
while n > 0 :
    r = n % 10
    n = n // 10
    m = m * 10 + r 
print(str(m) + " -> " + str(nbak))
print(f"{nbak} -> {m}")
print("{} -> {}".format(m, nbak))