'''
A continuación, debe solicitar por pantalla el departamento al que debe
pertenecer el nuevo usuario. Elige 5 departamentos diferentes para elegir.
(por ejemplo, Compras, Ventas, Marketing...).
'''
usuarios = []
DEPARTAMENTOS = ['Compras', 'Ventas', 'Marketing', "Sistemas", "Desarrollo"]

def escoger_departamento():
    print("Escoge un número de departamento: ")
    for numero in range(len(DEPARTAMENTOS)):
        print((str(numero + 1) + " .- " + DEPARTAMENTOS[numero]))
    departamento_escogido = int(input())-1

    if departamento_escogido < len(DEPARTAMENTOS):
        return DEPARTAMENTOS[departamento_escogido]
    else:
        print("Has introducido mal el numero de departamento, vuélvelo a introducir:")
        escoger_departamento()


def crear_usuario():

    nombre = input("Escibe el nombre: ")
    edad = input("Escibe la edad: ")
    departamento = escoger_departamento()


    usuario = {
        'nombre': nombre,
        'edad': edad,
        'departamento': departamento
    }

    usuarios.append(usuario)

def listar_usuarios():
    for usuario in usuarios:
        texto = ""
        texto = texto + "Nombre: " + usuario['nombre'] + " - "
        texto = texto + "Edad: " + usuario['edad'] + " - "
        texto = texto + "Departamento: " + usuario['departamento']
        print(texto)

repetir = True
while repetir:
    print("**************************")
    opcion = input("""
    1.- Crea un nuevo usuario
    2.- Muestra todos los usuarios y sus respectivos datos
    3.- Salir
    """)

    print("**************************")
    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        listar_usuarios()
    elif opcion == "3":
        repetir = False
    else:
        print("Has introducido un número incorrecto, vuelve a intentarlo: ")

