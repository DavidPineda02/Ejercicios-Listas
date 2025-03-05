# calcular la nota máxima y nota mínima de cada estudiante del curso de programación.  Recordar que por cada estudiante al almacena 5 notas, las dos primeras son evaluaciones  que equivalen al 30% de la nota final, la tercera y cuarta nota es de trabajos y equivale el 10%  y la última nota es examen final que equivale al 60%. Al final por cada estudiante se debe  mostrar su nombre, sus notas y su nota máxima y mínima. el curso está conformado por un  total de 20 aprendices en total y con rango de notas que van de 1 al 10 en su escala. 

print("========== Aprendices de Programacion ==========")

contador = 0
listaEst = []

while contador <= 20:
    listaNotas = []

    print(" ")
    nomb = input(f"Digite el Nombre del Aprendiz {contador + 1}: ")
    print(" ")

    for i in range(5):
        nots = float(input(f"Digite la Nota {i + 1} (1 - 10): "))
        listaNotas.append(nots)

    notMin = min(listaNotas)
    notMax = max(listaNotas)
    listaEst.append([nomb, listaNotas, notMax, notMin])

    contador += 1

print("\n========== Datos Aprendices ==========")
for nomb, listaNotas, notMax, notMin in listaEst:
    print(f"\nNombre: {nomb} \nNotas: {listaNotas} \nNota Maxima: {notMax} \nNota Minima: {notMin}")
print("\n======================================")