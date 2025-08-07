import random  

# Generación de variables aleatorias
variable1 = random.randint(1, 10)
variable2 = random.randint(1, 10)
variable3 = random.randint(1, 10)
variable4 = random.randint(1, 10)
variable5 = random.randint(1, 10)
variable6 = random.randint(1, 10)
variable7 = random.randint(1, 10)
variable8 = random.randint(1, 10)
variable9 = random.randint(1, 10)
variable10 = random.randint(1, 10)

# Lista con variables multiplicadas por 2
lista1 = [
    variable1 * 2, variable2 * 2, variable3 * 2, variable4 * 2, variable5 * 2,
    variable6 * 2, variable7 * 2, variable8 * 2, variable9 * 2, variable10 * 2
]

# Lista con variables multiplicadas por 3 (nombres corregidos y errores de sintaxis arreglados)
lista2 = [
    variable1 * 3, variable2 * 3, variable3 * 3, variable4 * 3, variable5 * 3,
    variable6 * 3, variable7 * 3, variable8 * 3, variable9 * 3, variable10 * 3
]





# Crear la lista con 5 cadenas ingresadas por teclado
lista_original = []
for i in range(5):
    cadena = input(f"Ingrese la cadena {i + 1}: ")
    lista_original.append(cadena)

# Copiar la lista en orden inverso
lista_invertida = lista_original[::-1]

# Mostrar los elementos de la lista invertida
print("Lista invertida:")
for cadena in lista_invertida:
    print(cadena)




# Leer 5 notas entre 0 y 10
notas = []
for i in range(5):
    nota = float(input(f"Ingrese la nota {i + 1} (de 0 a 10): "))
    while nota < 0 or nota > 10:
        print("⚠️ Nota no válida. Debe estar entre 0 y 10.")
        nota = float(input(f"Ingrese nuevamente la nota {i + 1}: "))
    notas.append(nota)

# Mostrar todas las notas
print("\nNotas ingresadas:")
for nota in notas:
    print(nota)

# Calcular y mostrar promedio, nota más alta y nota más baja
media = sum(notas) / len(notas)
nota_max = max(notas)
nota_min = min(notas)

print(f"\n📊 Nota media: {media:.2f}")
print(f"🔝 Nota más alta: {nota_max}")
print(f"🔻 Nota más baja: {nota_min}")


alumnos = {}
cantidad = int(input("¿Cuántos alumnos deseas guardar? "))

for _ in range(cantidad):
    alumno = input("Nombre del alumno: ")
    # Verifica que el nombre no esté repetido
    while alumno in alumnos:
        print("Ese alumno ya fue registrado.")
        alumno = input("Nombre del alumno: ")

    notas = []
    while True:
        nota = int(input("Dame una nota del alumno (número negativo para terminar):"))
        if nota < 0:
            break
        notas.append(nota)

    alumnos[alumno] = notas

# Mostrar promedio de cada alumno
print("\nPromedios:")
for alumno, notas in alumnos.items():
    if notas:  # Verifica que tenga al menos una nota
        promedio = sum(notas) / len(notas)
        print(f"{alumno} tiene una nota media de {promedio:.2f}")
    else:
        print(f"{alumno} no tiene notas registradas.")




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
      




