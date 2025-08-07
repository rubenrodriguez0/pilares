numero= input("ingresa un numero",)
if not numero:
    print("no ingresate un numero,")
    if numero > 0:
        print("El numero positivo.")
    elif numero < 0:
        print("El numero es negativo.")    
    else:
        print("El numero es cero.")