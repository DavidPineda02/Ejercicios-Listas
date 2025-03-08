# Generar una lista de nombres de libros del autor Gabriel García Márquez mínimo 10 obras  del autor, al final mostrar el nombre del libro, la cantidad de caracteres del título y remplazar  cada letra A con la letra X mayúscula. y mostrar el resultado de las modificaciones de la lista  original. 

print("========== Libros Gabriel García Márquez ==========\n")

libros = [
    "Cien años de soledad",
    "El amor en los tiempos del cólera",
    "Crónica de una muerte anunciada",
    "El otoño del patriarca",
    "Los funerales de la Mamá Grande",
    "El general en su laberinto",
    "Del amor y otros demonios",
    "El siglo de las luces",
    "La mala hora",
    "El rastro de tu padre"
]

titulsModf = []
for libro in libros:
    newTitul = libro.replace('A', 'X').replace('a', 'X')
    cantCarct = len(libro)
    titulsModf.append((newTitul, cantCarct))

for titulModf, cant in titulsModf:
    print(f"{titulModf} - {cant} caracteres")

print("\n===================================================")