# Crear una lista de palabras ingresadas por teclado, e identificar si alguna de ellas es  palíndroma o no, al final arrojar cuantas, y cuales palabras son palíndromas, y mostrar la lista  original. 

print("========== Palabras Palindromas =========")

listPalb = []

cant = int(input("\nCuantas palabras deseas digitar?: "))
print("")
for i in range(cant):
    palbr = input(f"Digita la palabra {i + 1}: ")
    listPalb.append(palbr)

palindromas = []

for palabra in listPalb:
    if palabra == palabra[::-1]:
        palindromas.append(palabra)

print("\nLista Original:", listPalb)
print("Palabras Palindromas:", palindromas)
print("Cantidad de Palabras Palindromas:", len(palindromas))
print("\n=========================================")