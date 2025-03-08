# Convertir cada elemento guardado en la lista del ejercicio #6, en mayúsculas y minúsculas,  Al final mostrar en pantalla el listado original y luego los dos nuevos listados respectivamente.

print("========== Libros Gabriel García Márquez ==========\n")

libros = [
    "Cien Años De Soledad",
    "El Amor En Los Tiempos del cólera",
    "Crónica De Una Muerte Anunciada",
    "El Otoño Del Patriarca",
    "Los Funerales De La Mamá Grande",
    "El General En Su Laberinto",
    "Del Amor y Otros Demonios",
    "El Siglo De Las Luces",
    "La Mala Hora",
    "El Rastro De Tu Padre"
]

listMay = []
listMin = []

for libro in libros:
    listMay.append(libro.upper())
    listMin.append(libro.lower())

print("Lista Original:", libros)
print("\nLista en Mayusculas:", listMay)
print("\nLista en Minusculas:", listMin)

print("\n===================================================")