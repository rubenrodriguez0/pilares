def calcular_interes_o _ total():
"""calcula el interes si es mayor al 30% e informa el importe total."""  
try:
    cantidad = float(input("ingrese la cantidad"))
    porsentaje_interes=float(input("ingrese el porsentaje" de interes(sin el simbolo%):))
    if porsentaje_interes >30:
        interes = (cantidad* porcentaje_interes)/100
        total = cantidad + interes
        print =(f"El interes es: {interes:.2f}")
        print =(f"El importe total es:{total:.2f}")

    else:
        print =(f"El importe total es:{cantidad:.2f}")
except ValueError:
    print("Error: Ingrese valores numericos validos.")    
#llamada ala funcion para ejecutar el programa
calcular_interes_o_total()