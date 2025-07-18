#Proyecto gestion de inventario
#Github tiene un Codespace / espacio de codigo

#Creando una clase de productos en donde se define cada producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    #Mostran el procuto
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
    
class Gestor_Inventario:
    def __init__(self):
        self.productos = {}

    #Funcion para agregar procutos.
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print(f"El producto con ID {producto.id_producto} es existente.")
        else:
            self.productos[producto.id_producto] = producto

    #Funcion para eliminar poductos
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con el ID {id_producto} fue eliminado.")
        else:
            print(f"Producto con el ID {id_producto} no ha sido encontrado.")
    #Actualizar la cantidad de un producto
    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].cantidad = nueva_cantidad
            print(f"La cantidad del producto ha sido actualizada a {nueva_cantidad}.")
        else:
            print(f"El producto con el ID {id_producto} no ha sido encontrado.")

    #Mostrar todos los productos en el inventario
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos.values():
                print(producto) 
    
    #Cambriar el precio de un producto
    def actualizar_precio(self, id_producto, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].precio = nuevo_precio
            print(f"El precio del producto ha sido actualizado a {nuevo_precio}")
            
class Usuario:
    def __init__(self, nombre, contraseña, tipo):
        self.nombre = nombre
        self.contraseña = contraseña
        self.tipo = tipo  # 'vendedor' o 'cliente'

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}"

class SistemaTienda:
    def __init__(self):
        self.usuarios = []
        self.inventario = Gestor_Inventario()
        # Por defecto, agregar dos vendedores solicitados
        self.usuarios.append(Usuario("Martin", "Martin", "vendedor"))
        self.usuarios.append(Usuario("Jilson", "Jilsont", "vendedor"))
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
                print("3. Modificar cantidad de producto")
                print("4. Modificar precio de producto")
                print("5. Mostrar productos actuales")
                print("6. Salir de la cuenta")
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
                    idp = input("ID producto a modificar cantidad: ")
                    cantidad = int(input("Nueva cantidad: "))
                    self.inventario.actualizar_cantidad(idp, cantidad)
                elif opcion == "4":
                    idp = input("ID producto a modificar precio: ")
                    precio = float(input("Nuevo precio: "))
                    self.inventario.actualizar_precio(idp, precio)
                elif opcion == "5":
                    self.inventario.mostrar_productos()
                elif opcion == "6":
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
                print(f"Compra realizada. Usted compró {cantidad} unidad(es) de {producto.nombre}.")
            else:
                print("Cantidad no válida.")
        else:
            print("Producto no encontrado.")

if __name__ == "__main__":
    sistema = SistemaTienda()
    sistema.menu_principal()
