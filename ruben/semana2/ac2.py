numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")



numero = int(input("Ingresa un número: "))

if 1 <= numero <= 7:
    print("El número está en el rango de 1 a 7.")
else:
    print("El número NO está en el rango de 1 a 7.")


cantidad = float(input("Ingresa una cantidad: "))
interes = float(input("Ingresa el porcentaje de interés (sin %): "))

# Convertimos el porcentaje a decimal
tasa = interes / 100

if tasa > 0.30:
    monto_interes = cantidad * tasa
    print(f"El interés es: ${monto_interes:.2f}")
else:
    print(f"El importe total es: ${cantidad:.2f}")