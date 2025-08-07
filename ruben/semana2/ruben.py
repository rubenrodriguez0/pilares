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