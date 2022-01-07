'''
Debe ofrecer por pantalla un generador de contraseñas.
Se deberá mostrar por pantalla las siguientes opciones que podemos elegir para crearla:

a. Longitud(int)
b. Minúsculas (si queremos que incluya o no)
c. Mayúsculas (si queremos que incluya o no)
d. Símbolos (si queremos que incluya o no)
'''
import random


def longitud():
    longitud = input("Escribe el número de caracteres que quieres que contenga la contraseña: ")
    return int(longitud)

def si_no_pantalla(texto):
    opcion = input(f"¿Quieres incluir {texto} en la contraseña? Escribe 's' o 'n': ").lower()

    if opcion == "s" or opcion == "n":
        return opcion
    else:
        print("Opcion mal escogida.")
        si_no_pantalla(texto)




longitud = longitud()
minusculas = si_no_pantalla("minusculas")
mayusculas = si_no_pantalla("mayusculas")
simbolos = si_no_pantalla("simbolos")



lista_minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
lista_mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lista_simbolos = ["!","#","$","%","&","/","(",")","=","?","¿","¡","*","+","-",",",".",":",";","_","|","{","}","[","]","^","~","@","<",">","¬","`","´","¨","ª","º","µ","·","¿","¡"]
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
    password = password +  str(random.choice(todas))
print("***************************")
print(f"La contraseña generada es: {password}")
print("***************************")







