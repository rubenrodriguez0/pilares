fahrenheit = float(input("Dame el número de grados Fahrenheit que quieres convertir: "))
centigrados = (fahrenheit - 32) * (5 / 9)
print("Los grados centígrados son:", centigrados)

print("\nSelecciona la operación")
print("1. Suma")      
print("2. Resta")
print("3. Multiplicación")
print("4. División")  # Se corrigió el error en "divicion"
opcion = input("Ingresa la opción (1/2/3/4): ")  # Corregida la sintaxis en el input

# Se deben guardar los números en variables antes de operar con ellos
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion in ("1", "2", "3", "4"):
    if opcion == "1":
        resultado = num1 + num2  # Se corrigió la falta de definición de la función suma
    elif opcion == "2":
        resultado = num1 - num2  # Lo mismo con resta
    elif opcion == "3":
        resultado = num1 * num2  # Multiplicación
    elif opcion == "4":    
        resultado = num1 / num2 if num2 != 0 else "Error: división por cero"  # Se corrigió la división

    print("El resultado es:", resultado)  

print("\nEste programa calcula el perímetro y área de un rectángulo")  
base = float(input("Dame la base del rectángulo: "))  
altura = float(input("Dame la altura del rectángulo: "))  
perimetro = 2 * (base + altura)  
area = base * altura  
print("El perímetro del rectángulo es:", perimetro)  
print("El área del rectángulo es:", area)  

print("\nEste programa calcula la media de 3 números")  
n1 = float(input("Dame el primer número: "))  
n2 = float(input("Dame el segundo número: "))  
n3 = float(input("Dame el tercer número: "))  
media = (n1 + n2 + n3) / 3  
print("La media es:", media)