numero= int(input("introduce un numero entero positivo:"))

if numero < 0:
    print("El numero debe ser positivo.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    print("El factorial de !",numero, "es", factorial)
    