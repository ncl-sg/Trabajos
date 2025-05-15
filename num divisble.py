n = int(input("Ingrese un número entero: "))
c = 1
while c <= n:
    m = str(c)
    if c % 2 == 0 and c % 3 == 0:
        m += ". Divisible por 2 y 3"
    elif c % 2 == 0 and c % 5 == 0:
        m += ". Divisible por 2 y 5"
    elif c % 3 == 0 and c % 5 == 0:
        m += ". Divisible por 3 y 5"
    elif c % 2 == 0:
        m += ". Divisible por 2"
    elif c % 3 == 0:
        m += ". Divisible por 3"
    elif c % 5 == 0:
        m += ". Divisible por 5"
    print(m)
    c += 1
