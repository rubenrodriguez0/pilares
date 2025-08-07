def menu():
    while True:
        print("\n--- menu ---")
        print("1. opcion 1")
        print("2. opcion 2")
        print("3. salir 3")
    

        opcion = input("Seleccine una opcion:")

        if opcion == '1':
            print("Ha seleccinado la opcion 1")
        elif opcion =='2':
            print("Ha seleccionado la opcion 2")
        elif opcion =='3':
            print("saliendo")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")