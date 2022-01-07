''''
Una vez creada la contraseña, debe determinar su fortaleza y mostrar por pantalla si esta
es débil, media o fuerte (debes especificar los criterios para clasificarla en una categoría o en otra).
'''

import random

LISTA_MINUSCULAS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
LISTA_MAYUSCULAS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
LISTA_SIMBOLOS = ["!","#","$","%","&","/","(",")","=","?","¿","¡","*","+","-",",",".",":",";","_","|","{","}","[","]","^","~","@","<",">","¬","`","´","¨","ª","º","µ","·","¿","¡"]

def si_no_pantalla(texto):
    opcion = input(f"¿Quieres incluir {texto} en la contraseña? Escribe 's' o 'n': ").lower()

    if opcion == "s" or opcion == "n":
        return opcion
    else:
        print("Opcion mal escogida.")
        si_no_pantalla(texto)


def longitud_password():
    longitud = input("Escribe el número de caracteres que quieres que contenga la contraseña: ")
    return int(longitud)


def generar_password():

    longitud = longitud_password()
    minusculas = si_no_pantalla("minusculas")
    mayusculas = si_no_pantalla("mayusculas")
    simbolos = si_no_pantalla("simbolos")

    todas = []
    if minusculas == "s":
        todas.extend(LISTA_MINUSCULAS)
    if mayusculas == "s":
        todas.extend(LISTA_MAYUSCULAS)
    if simbolos == "s":
        todas.extend(LISTA_SIMBOLOS)
    ''' Vamos a mezclar el array '''
    random.shuffle(todas)

    password = ""

    for x in range(longitud):
        password = password +  str(random.choice(todas))
    print("***************************")
    print(f"La contraseña generada es: {password}")
    print("***************************")


    return {
        'longitud' : longitud,
        'minusculas' : minusculas,
        'mayusculas' : mayusculas,
        'simbolos' : simbolos,
        'password' : password
    }


data = generar_password()


print("""
Citerios para la contraseña:
- Débil: Si solo dispone de una de las tres opciones es débil (mayusculas o minusculas o simbolos) y longitud < 5
- Media: Si dispone de una dos de las opciones es media (ma-min o ma-sim o min-may o min-sim o sim-ma o sim-min) y longitud = > 5 y longitud = < 7
- Fuerte: Si dispone de tres de las opciones es fuerte (mayusculas y minusculas y simbolos) y longitud > 7
""")


if data['minusculas'] == "s" and data['mayusculas'] == "s" and data['simbolos'] == "s" and data['longitud'] > 7 :
    print("FORTALEZA FUERTE")
elif ((data['mayusculas'] == "s" and data['minusculas'] == "s") or (data['mayusculas'] == "s" and data['simbolos'] == "s" == "s") or (data['minusculas'] == "s" and data['mayusculas'] == "s") or (data['minusculas'] == "s" and data['simbolos'] == "s")) and data['longitud'] >= 5 :
        print("FORTALEZA MEDIA")
else:
        print("FORTALEZA DÉBIL")









