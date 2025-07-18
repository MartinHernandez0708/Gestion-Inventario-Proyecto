import modulo = mo

correct_pass = False
usuarios_registrados = [mo.User("Default", "0123")]
usuario_act:mo.User

#Mientras no se ponge la contraseña correcta o se cree una cuenta esto se repite
while correct_pass == False:
  eleccion:int = int(input("1_ Iniciar sesion\n2_ Crear cuenta\n"))

  enter_name = input("Ingrese su nombre: ")
  enter_password = input("Ingrese su contraseña: ")
  if eleccion == 1:
    for usuario in usuarios_registrados:
      if enter_name == usuario.nombre and enter_password == usuario.contraseña:
        print("Entro con exito\n")
        usuario_act = usuario
        correct_pass = True
      else:
        print("Contraseña o nombre incorrectos\n")
  else:
    usuarios_registrados.append(mo.User(enter_name, enter_password))
    #Le resto 1 al largo de la lista para que no se salga de rango
    usuario_act = usuarios_registrados[len(usuarios_registrados)-1]
    print("Registrado correctamente")
    print(usuario_act)
    correct_pass = True

while True:
  eleccion = mo.menu()
  if eleccion == 1:
    pass
  elif eleccion == 2:
    pass
  elif eleccion == 3:
    pass
  elif eleccion == 4:
    pass
  else:
    break
