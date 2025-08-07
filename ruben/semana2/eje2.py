def verificar_rango(numero)
    """veriffica si un numero esta en el rango de 1 al 7 (incluyendo el 1 el 7)."""
    if 1 <= numero <= 7:
        return True
    else:
        return False
#obtenr la entrada del usuario
numero_ingresado = in(input("ingrese un numero: "))

#verificar el rango y mostrar el resultado
if verificar_rango(numero_ingresado):
    print(f"El numero{numero_ingresado} esta dentro del rango de 1 a 7.")