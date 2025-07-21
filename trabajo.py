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
    #Actualizar el nombre de un producto
    def actualizar_nombre(self, id_producto, nuevo_nombre):
    if id_producto in self.productos:
        self.productos[id_producto].nombre = nuevo_nombre
        print(f"El nombre del producto ha sido actualizado a {nuevo_nombre}.")
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

if __name__ == "__main__":
    sistema = SistemaTienda()
    sistema.menu_principal()
