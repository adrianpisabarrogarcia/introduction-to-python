'''
Debe pedir por pantalla un nombre de usuario.
En el código creado debe existir una lista, tupla,
diccionario u otra estructura de datos* de usuarios
existentes.
Si el nombre existe, no debe dejar crearlo.
'''

lista_de_usuarios = ['juan', 'pedro', 'maria', 'jose']

def pedir_usuario():
    nombre_usuario = input('Ingrese su nombre de usuario: ').lower()
    crearlo = True

    for usuario in lista_de_usuarios:
        if usuario == nombre_usuario:
            crearlo = False
            break

    if crearlo:
        lista_de_usuarios.append(nombre_usuario)
        print(f"Añadido el usuario {nombre_usuario} a la lista de usuarios.")
    else:
        print(f"El nombre de usuario: {nombre_usuario} ya esta creado. Prueba con otro diferente")

def imprimir_lista_usuarios():
    texto = "los usuarios son: "

    for usuario in lista_de_usuarios:
        texto = texto + usuario + " "

    print(texto)


salir = False
while not salir:
    opcion = input('''
    1.- Añadir un nombre de usuario nuevo
    2.- Imprimir lista de usuarios
    3.- Salir del programa
    ''')
    '''print(f"opcion ,{opcion}")'''
    if opcion == "1":
        pedir_usuario()
    elif opcion == "2":
        imprimir_lista_usuarios()
    elif opcion == "3":
        salir = True
    else:
        print("Introduce un número válido")






