
'''lista de usuarios'''
import email
import random
import re
import smtplib
from email.mime.text import MIMEText

usuarios = []


'''ejercicio 1'''
def comprobar_usuario_existente(nombre):
    for usuario in usuarios:
        if usuario['nombre'] == nombre:
            return True

    return False

'''ejercicio 2'''
def longitud_password():
    longitud = input("Escribe el número de caracteres que quieres que contenga la contraseña: ")
    return int(longitud)


def si_no_pantalla(texto):
    opcion = input(f"¿Quieres incluir {texto} en la contraseña? Escribe 's' o 'n': ").lower()

    if opcion == "s" or opcion == "n":
        return opcion
    else:
        print("Opcion mal escogida.")
        si_no_pantalla(texto)

''' ejercicio 3 '''
def fortaleza_password(data):
    print("""
    Criterios para la contraseña:
    - Débil: Si solo dispone de una de las tres opciones es débil (mayusculas o minusculas o simbolos) y longitud < 5
    - Media: Si dispone de una dos de las opciones es media (ma-min o ma-sim o min-may o min-sim o sim-ma o sim-min) y longitud = > 5 y longitud = < 7
    - Fuerte: Si dispone de tres de las opciones es fuerte (mayusculas y minusculas y simbolos) y longitud > 7
    """)

    if data['minusculas'] == "s" and data['mayusculas'] == "s" and data['simbolos'] == "s" and data['longitud'] > 7:
        print("FORTALEZA FUERTE")
    elif ((data['mayusculas'] == "s" and data['minusculas'] == "s") or (
            data['mayusculas'] == "s" and data['simbolos'] == "s" == "s") or (
                  data['minusculas'] == "s" and data['mayusculas'] == "s") or (
                  data['minusculas'] == "s" and data['simbolos'] == "s")) and data['longitud'] >= 5:
        print("FORTALEZA MEDIA")
    else:
        print("FORTALEZA DÉBIL")

''' ejercicio 2 '''
def generar_password():
    longitud = longitud_password()
    minusculas = si_no_pantalla("minusculas")
    mayusculas = si_no_pantalla("mayusculas")
    simbolos = si_no_pantalla("simbolos")

    lista_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r",
                        "s",
                        "t", "u", "v", "w", "x", "y", "z"]
    lista_mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R",
                        "S",
                        "T", "U", "V", "W", "X", "Y", "Z"]
    lista_simbolos = ["!", "#", "$", "%", "&", "/", "(", ")", "=", "?", "¿", "¡", "*", "+", "-", ",", ".", ":", ";",
                      "_",
                      "|", "{", "}", "[", "]", "^", "~", "@", "<", ">", "¬", "`", "´", "¨", "ª", "º", "µ", "·", "¿",
                      "¡"]
    todas = []
    if minusculas == "s":
        todas.extend(lista_minusculas)
    if mayusculas == "s":
        todas.extend(lista_mayusculas)
    if simbolos == "s":
        todas.extend(lista_simbolos)
    ''' Vamos a mezclar el array '''
    random.shuffle(todas)

    password = ""

    for x in range(longitud):
        password = password + str(random.choice(todas))

    print(f"La contraseña generada es: {password}")

    data = {
        'longitud': longitud,
        'minusculas': minusculas,
        'mayusculas': mayusculas,
        'simbolos': simbolos,
        'password': password
    }

    '''Ejercicio 3: Muestra la fortaleza de la contraseña'''
    fortaleza_password(data)

    return password

'''ejercicio 4'''
def escoger_departamento():
    '''lista de departamentos'''
    DEPARTAMENTOS = ['Compras', 'Ventas', 'Marketing', "Sistemas", "Desarrollo"]

    print("Escoge un número de departamento: ")
    for numero in range(len(DEPARTAMENTOS)):
        print((str(numero + 1) + " .- " + DEPARTAMENTOS[numero]))
    departamento_escogido = int(input())-1

    if departamento_escogido < len(DEPARTAMENTOS):
        return str(DEPARTAMENTOS[departamento_escogido])
    else:
        print("Has introducido mal el numero de departamento, vuélvelo a introducir:")
        escoger_departamento()


'''ejercicio 5'''
def introducir_email_valido():
    email = input("Introduce un mail válido: ")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if (re.fullmatch(regex, email)):
        return email
    else:
        print("Email invalido, vuelve a introducir un mail valido.")
        introducir_email_valido()


'''ejercicio 6'''
def imprimir_usuario_concreto(usuario):
    texto = ""
    texto = texto + "Nombre: " + usuario['nombre'] + " - "
    texto = texto + "Edad: " + usuario['edad'] + " - "
    """ He eliminado la password para no mostrarla"""
    texto = texto + "Email: " + usuario['email'] + " - "
    texto = texto + "Departamento: " + usuario['departamento']
    return texto

'''ejercicio 7'''
def envio_email_registro(usuario):
    from_addr = 'developersweapp@gmail.com'
    to = str(usuario['email'])
    message = str(imprimir_usuario_concreto(usuario))

    # credenciales de Gmail
    username = 'developersweapp@gmail.com'
    password = '12345Abcde'

    """
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to, message)
    server.quit()
    """

    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP()
    server.connect(smtp_host, smtp_port)
    server.ehlo()
    server.starttls()
    server.login(username, password)

    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = email.Utils.COMMASPACE.join(to)
    msg['Subject'] = "Usuario registrado"
    msg.attach(MIMEText(message))
    server.sendmail(from_addr, to, msg.as_string())

def crear_usuario():

    nombre = input("Escibe el nombre: ")
    '''ejercicio 1: Compruebo si el usuario esta creado o no:'''
    if comprobar_usuario_existente(nombre):
        print("El usuario ya existe, crea otro usuario")
        crear_usuario()
    edad = input("Escibe la edad: ")
    '''ejericio 2: generador de contraseñas'''
    password = generar_password()

    '''ejercicio 4: escoger departamento'''
    departamento = escoger_departamento()

    '''ejercicio 5: introducir un mail válido'''
    email = introducir_email_valido()


    usuario = {
        'nombre': nombre,
        'edad': edad,
        'password': password,
        'email': email,
        'departamento': departamento
    }

    '''ejercicio 6'''
    print(imprimir_usuario_concreto(usuario))
    usuarios.append(usuario)
    print(f"Ahora mismo hay {len(usuarios)} usuarios creados")

    '''ejercicio 7'''
    envio_email_registro(usuario)

'''ejercicio 6'''
def listar_usuarios():
    print("**********************************")
    for usuario in usuarios:
        texto = ""
        texto = texto + "Nombre: " + usuario['nombre'] + " - "
        texto = texto + "Edad: " + usuario['edad'] + " - "
        """ Se puede eliminar la password para no mostrarla"""
        texto = texto + "Password: " + usuario['password'] + " - "
        texto = texto + "Email: " + usuario['email'] + " - "
        texto = texto + "Departamento: " + usuario['departamento']
        print(texto)

    print("**********************************")




''' Main '''

repetir = True
while repetir:
    print("**************************")
    opcion = input("""
    1.- Crea un nuevo usuario
    2.- Muestra todos los usuarios y sus respectivos datos, junto con el número de usuarios que existen.
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
