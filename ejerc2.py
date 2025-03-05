# Almacenar una lista de números, identificar la longitud de la lista si es par: Los elementos
# invertir los elementos de la lista. Imprimir la lista original y lista invertida.

print("========== Listas Invertidas =========")

cantNum = int(input("\nCantidad de Numeros que desea tener en la Lista: "))
listNum = []

if cantNum >= 1:
    print(" ")
    for i in range(cantNum):
        num = int(input(f"Digite el Numero {i+1}: "))
        listNum.append(num)
    
    cantNumList = len(listNum)
    if cantNumList % 2 == 0:
        print("\nEl Numero de Cantidad en la Lista es Par.")
        print(listNum)
        listNum.reverse()
        print(listNum)
        print("\n======================================")
    else:
        print("\nEl Numero de Cantidad en la Lista es Impar.")
        print(listNum)
        listNum.reverse()
        print(listNum)
        print("\n======================================")
else: 
    print("\nNumero Negativo o Igual a 0")
    print("\n======================================")
