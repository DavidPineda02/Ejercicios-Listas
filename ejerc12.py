# Escriba un programa que permita crear una lista de palabras y que, a continuación de tres  opciones: 
# • Contar: Me pide una cadena, y me dice cuántas veces aparece en la lista 
# • Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones  de la primera por la segunda en la lista. 
# • Eliminar: Me pide una cadena, y la elimina de la lista. 
# • Mostrar: Muestra la lista de cadenas 
# • Terminar 

print("========== Menu de Listas ==========")

listPalbrs = []

while True:
    print("\n0. Agregar \n1. Contar \n2. Modificar \n3. Eliminar \n4. Mostrar \n5. Terminar")
    opc = int(input("\nDigita una Opcion (0-5): "))

    if opc == 0:
        cadena = input("\nDigite la Cadena a Ingresar: ")
        listPalbrs.append(cadena.upper())

    elif opc == 1:
        cadena = input("\nDigite la Cadena a Contar: ")
        conteo = listPalbrs.count(cadena.upper())
        print(f"\nLa Cadena '{cadena}' Aparece {conteo} Veces en la Lista.")

    elif opc == 2:
        cadenaModf = input("\nDigite la Cadena a Modificar: ")
        if cadenaModf.upper() in listPalbrs:
            newCadena = input("Digite la Nueva Cadena: ")
            for i in range(len(listPalbrs)):
                if listPalbrs[i] == cadenaModf.upper():
                    listPalbrs[i] = newCadena.upper()
            print(f"\nSe han Modificado todas las ocurrencias de '{cadenaModf}' por '{newCadena}'.")
        else:
            print(f"\nLa Cadena '{cadenaModf}' no se encuentra en la lista.")

    elif opc == 3:
        cadenaDelt = input("\nDigite la Cadena a Eliminar: ")
        while cadenaDelt.upper() in listPalbrs:
            listPalbrs.remove(cadenaDelt.upper())
        print(f"\nLa Cadena '{cadenaDelt}' ha sido eliminada de la lista.")

    elif opc == 4:
        print("\nLista de Palabras:", listPalbrs)

    elif opc == 5:
        print("\nTerminando el Programa.")
        print("\n====================================")
        break

    else:
        print("\nNúmero Inválido, Digita del (0 al 5)")
