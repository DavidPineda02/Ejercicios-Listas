# Crear un programa que añada números a una lista hasta que introducimos u número negativo.  A continuación, debe crear una nueva lista igual que la anterior, pero eliminando los números  duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados. 

print("========== Lista Sin Duplicados ==========\n")

listNum = []

while True:
    num = int(input("Digite un Numero (Numero Negativo para Terminar): "))
    if num < 0:
        break
    listNum.append(num)

listSinDup = []
for num in listNum:
    if num not in listSinDup:
        listSinDup.append(num)

print("\nLista original:", listNum)
print("Lista sin duplicados:", listSinDup)
print("\n==========================================")