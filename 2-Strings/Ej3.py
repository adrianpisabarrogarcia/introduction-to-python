string = "su clave es: 1540"
print("antes de cifrar: ", string)

'''change space of the string to the character that you want'''
input_text = input("Ingrese el caracter que desea cambiar: ")
string = string.replace('\d', input_text)
print("despues de cifrar: ", string)