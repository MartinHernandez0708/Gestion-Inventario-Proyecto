import trabajo as tr
class SistemaTienda:
    def __init__(self):
        self.usuarios = []
        self.inventario = tr.Gestor_Inventario()
        # Por defecto, agregar dos vendedores solicitados
        self.usuarios.append(tr.Usuario("Martin", "Martin", "vendedor"))
        self.usuarios.append(tr.Usuario("Jilson", "Jilson", "vendedor"))
        self.usuario_actual = None

    def registrar_cliente(self):
        nombre = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        self.usuarios.append(Usuario(nombre, contraseña, "cliente"))
        print("Cuenta de cliente creada exitosamente.")

    def iniciar_sesion(self):
        nombre = input("Usuario: ")
        contraseña = input("Contraseña: ")
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.contraseña == contraseña:
                self.usuario_actual = usuario
                print(f"Bienvenido {usuario.nombre} ({usuario.tipo})")
                return True
        print("Usuario o contraseña incorrectos.")
        return False

    def cerrar_sesion(self):
        print(f"Saliendo de la cuenta de {self.usuario_actual.nombre}")
        self.usuario_actual = None

    def menu_principal(self):
        while True:
            if not self.usuario_actual:
                print("\n--- Sistema de Tienda ---")
                print("1. Iniciar sesión")
                print("2. Registrarse como cliente")
                print("3. Salir")
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    if self.iniciar_sesion():
                        self.menu_usuario()
                elif opcion == "2":
                    self.registrar_cliente()
                elif opcion == "3":
                    print("Hasta luego.")
                    break
                else:
                    print("Opción no válida.")
            else:
                self.menu_usuario()

    def menu_usuario(self):
        usuario = self.usuario_actual
        while True:
            print(f"\n--- Menú ({usuario.tipo}) ---")
            if usuario.tipo == "vendedor":
                print("1. Agregar producto")
                print("2. Eliminar producto")
                print("3. Modificar nombre de producto")
                print("4. Modificar cantidad de producto")
                print("5. Modificar precio de producto")
                print("6. Mostrar productos actuales")
                print("7. Salir de la cuenta")
            elif usuario.tipo == "cliente":
                print("1. Ver productos")
                print("2. Comprar producto")
                print("3. Cambiar de cuenta")
                print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if usuario.tipo == "vendedor":
                if opcion == "1":
                    idp = input("ID producto: ")
                    nombre = input("Nombre: ")
                    cantidad = int(input("Cantidad: "))
                    precio = float(input("Precio: "))
                    producto = Producto(idp, nombre, cantidad, precio)
                    self.inventario.agregar_producto(producto)
                elif opcion == "2":
                    idp = input("ID producto a eliminar: ")
                    self.inventario.eliminar_producto(idp)
                elif opcion == "3":
                    idp = input("ID producto a modificar nombre: ")
                    nombre = input("Nuevo nombre: ")
                    self.inventario.actualizar_nombre(idp, nombre)
                elif opcion == "4":
                    idp = input("ID producto a modificar cantidad: ")
                    cantidad = int(input("Nueva cantidad: "))
                    self.inventario.actualizar_cantidad(idp, cantidad)
                elif opcion == "5":
                    idp = input("ID producto a modificar precio: ")
                    precio = float(input("Nuevo precio: "))
                    self.inventario.actualizar_precio(idp, precio)
                elif opcion == "6":
                    self.inventario.mostrar_productos()
                elif opcion == "7":
                    self.cerrar_sesion()
                    break
                else:
                    print("Opción no válida.")
            elif usuario.tipo == "cliente":
                if opcion == "1":
                    self.inventario.mostrar_productos()
                elif opcion == "2":
                    self.comprar_producto()
                elif opcion == "3":
                    self.cerrar_sesion()
                    break
                elif opcion == "4":
                    print("Hasta luego.")
                    exit()
                else:
                    print("Opción no válida.")

    def comprar_producto(self):
        self.inventario.mostrar_productos()
        idp = input("Ingrese el ID del producto que desea comprar: ")
        if idp in self.inventario.productos:
            producto = self.inventario.productos[idp]
            cantidad = int(input(f"Ingrese la cantidad a comprar (disponible: {producto.cantidad}): "))
            if cantidad > 0 and cantidad <= producto.cantidad:
                producto.cantidad -= cantidad
                print(f"Compra realizada. Usted compró {cantidad} unidades de {producto.nombre}.")
            else:
                print("Cantidad no válida.")
        else:
            print("Producto no encontrado.")
