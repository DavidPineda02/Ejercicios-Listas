# Crear dos listas la primera contendrá el nombre del usuario y la segunda lista contendrá el  password de cada usuario. Genere una rutina de código que permita validar que los usuarios  y password, guardados coincidan con los datos ingresados por el usuario y si es correcto  arrojar el mensaje de usuario registrado y de lo contrario arrojar el mensaje de usuario no  valido. 

users = []
password = []

print("========== Inicio de Seccion ==========")

while True:
    print("\n1. Registrarse. \n2. Inicio de Sesion.")
    opc = int(input("\nCual es la Opcion que Deseas? (1 - 2): "))
    if opc == 1:
        nomUser = input("\nDigite su Nombre de Usuario: ")
        pswUser = input("Digite su Contraseña: ")

        users.append(nomUser)
        password.append(pswUser)
        continue
    if opc == 2:
        nomUser = input("\nDigite su Nombre de Usuario: ")
        pswUser = input("Digite su Contraseña: ")

        if nomUser in users:
            valid = users.index(nomUser)
            if password[valid] == pswUser:
                print("\nUsuario Registrado.")
                print("\n=======================================")
                break
            else:
                print("\nContraseña Incorrecta.")
        else:
            print("\nUsuario no Valido.")