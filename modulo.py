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
            
class User:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        self.inventario = []
    def __str__(self):
        return f"Nombre: {self.nombre}\nContraseña: {self.contraseña}\nInventario: {self.inventario}"
