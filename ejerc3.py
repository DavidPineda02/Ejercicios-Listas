# Almacenar dos listos de números enteros, lista1 y lista2, y generar la tercera lista con los
# siguientes criterios: Sumar el primer elemento de la lista1 con el último elemento de la lista2 y
# guardar el resultado en la lista3, luego el segundo elemento de la lista1 sumarlo con el noveno
# elemento de la lista2. Al final imprimir las tres listas.

print("========== Creacion de Tercera Lista ==========")

lista1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista2 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
lista3 = []

for i in range(len(lista1)):
    lista3.append(lista1[i] + lista2[-(i + 1)])

print("\nLista 1:", lista1)
print("Lista 2:", lista2)
print("\nLista 3:", lista3)
print("\n===============================================")
