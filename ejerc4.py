# generar dos listas de longitudes n y m, la primera lista ordenarla de manera ascendente y la  segunda de manera descendente. 

print("========== Listas Ascendentes y Descendentes ==========")

listaN = []
listaM = []

cant1 = int(input("\nCantidad de Numeros de la Primer Lista: "))

print("\n----- Primer Lista -----\n")
for i in range(cant1):
    listaN.append(int(input(f"Digite el numero {i + 1}: ")))
print("\n------------------------")

cant2 = int(input("\nCantidad de Numeros de la Segunda Lista: "))

print("\n----- Segunda Lista -----\n")
for i in range(cant2):
    listaM.append(int(input(f"Digite el numero {i + 1}: ")))
print("\n-------------------------")

listaN.sort()
listaM.sort(reverse=True)
print(f"\n{listaN}")
print(listaM)
print("\n=======================================================")