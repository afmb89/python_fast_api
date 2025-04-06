def user_information(name:str = "", surname:str = "", email:str = ""):
  if (len(name) == 0):
    print('No se ingresó ningún "nombre".')
    return

  if (len(surname) == 0):
    print('No se ingresó ningún "apellido".')
    return

  if (len(email) == 0):
    print('No se ingresó ningún "email".')
    return

  if (email.find("@") == -1):
    print("El email ingresado no tiene el formato debido.")
    return

  user = {'name': name, 'apellido': surname, 'email': email}
  print(user)

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
email = str(input("Ingrese su email: "))

user_information(nombre, apellido, email)