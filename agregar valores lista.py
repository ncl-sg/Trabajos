a = int(input("Cuanto valores desea agregar a la lista: "))
b = 1
l = []
for i in range(a) :
    n = int(input(f"Digite el valor {b}:"))
    l.append(n)
    b += 1
max = l[0]
print(l)
for i in range(len(l)):
    if max < l[i]:
        max = l[i]
        posmax = i + 1
print(max)
print(posmax)