"""
Después,debe pedir por pantalla un email para poder mandar los datos
(nombre de usuario, departamento y contraseña).
El programa debe validar el email (que esté bien escrito).
"""
import re
import smtplib, ssl

#pido datos
nombre_usuario = input("Introduce un nombre de usuario:")
departamento_usuario = input("Introduce el departamento correspondiente:")
password_usuario = input("Introduce una password del usuario:")
email_usuario = input("Introduce un email del usuario:")

#validar email
email = email_usuario
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

if not re.fullmatch(regex, email):
    print("Email invalido, vuelve a ejecutar la aplicación.")
else:
    mensaje = '''
    Hay registrado un nuevo usuario!
    Nombre: ''' + nombre_usuario + '''
    Departamento: ''' + departamento_usuario + '''
    Email: ''' + email_usuario + '''
    '''

    #envio mail
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    print("¡Un momento! Vamos a configurar el mail, para enviar un correo:")
    sender_email = input("Type your gmail email account and press enter: ")
    password = input("Type your gmail password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context) # Secure the connection
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, email_usuario, mensaje)
        print("Correo enviado! :)")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()