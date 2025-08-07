def mostrar_menu():
    print("===== menu =====")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Opcion 3")
    print("4. salir")


    def main():
        opcion = 0
        while opcion != 4:
            mostrar_menu()
            try:
                opcion = int(input("Selecione una opcion:"))
            except ValueError:
                print("Entrada invalida. Por favor, ingrese un numero.") 
                continue


            if opcion == 1:
                print("Ha elegidola opcion 1.")
            elif opcion == 2:
                print("Ha elegido la opcion 2.")
            elif opcion == 3:
                print("Ha elegido la opcion 3.")
            elif opcion == 4:
                print("Saliendo del programa...")
            else:
                print("Opcion invalida. Por Favor, seleccione una opcion valida.")

                if_name_ == "_main_":
                  main()