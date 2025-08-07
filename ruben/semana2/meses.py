meses = ("Enero","Febrero","marzo","Abril","Mayo","junio","julio","agosto""septiembre","octubre","noviembre","diciembre")
salir = False

while not salir:
    numero  = int(input("Dame un numero (0 para salir): " ))

    if numero == 0:
        salir =True
    elif 1 <= numero <= len(meses):
         print("mes:", meses[numero - 1])
    else:
        print("por favor, inserta un numero entre 1 y , 1en(meses)")
      