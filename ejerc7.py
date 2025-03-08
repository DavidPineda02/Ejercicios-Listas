#  De las listas trabajadas en el ejercicio #2, ingresar nuevos elementos a estas listas en  diferentes posiciones y mostrar al final la nueva lista modificada 

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
    else:
        print("\nEl Numero de Cantidad en la Lista es Impar.")
    
    print("Lista Original:", listNum)
    listNum.reverse()
    print("Lista Invertida:", listNum)
    print("\n======================================")

    while True:
        newNum = input("\nDesea agregar un nuevo Numero a la Lista? (si/no): ")
        if newNum.lower() == 'si':
            num = int(input("\nDigite el nuevo Numero: "))
            posicion = int(input("Digite la Posición donde desea Agregarlo (0 para inicio, -1 para final): "))
            if posicion == -1:
                listNum.append(num)
            else:
                listNum.insert(posicion, num)
            print("\nLista Modificada:", listNum)
        else:
            print("\n======================================")
            break
else: 
    print("\nNumero Negativo o Igual a 0")
    print("\n======================================")