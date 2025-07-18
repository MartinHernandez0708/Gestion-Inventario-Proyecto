import modulo = mo

correct_pass = False
#Si ya ingresaron con la contraseña correcta o no
usuarios_registrados = [mo.User("Default", "0123")]
#Todos los usuarios registrados
usuario_act:mo.User
#Usuario de la sesion actual

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
    correct_pass = True

while True:
  eleccion = mo.eleccion_menu()
  if eleccion == 1:
    usuario_act.agregar_producto(input("ID producto: "), input("Nombre producto: "), input("Cantidad: "), input("Precio: "))
  elif eleccion == 2:
    usuario_act.mostrar_productos()
    usuario_act.eliminar_producto(input("ID producto a eliminar: "))
  elif eleccion == 3:
    eleccion = int(input("1_ Actualizar cantidad\n2_ Actualizar precio\n3_ Actualizar nombre"))
    if eleccion == 1:
      usuario_act.mostrar_productos()
      usuario_act.actualizar_cantidad(input("ID producto: "))
  elif eleccion == 4:
    pass
  else:
    break
