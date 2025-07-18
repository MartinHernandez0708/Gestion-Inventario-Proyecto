#Proyecto gestion de inventario
#Github tiene un Codespace / espacio de codigo

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
    
class Gestor_Inventario:
    def __init__(self):
        self.productos = {}
class User:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        self.inventario = []
    def __str__(self):
        return f"Nombre: {self.nombre}\nContraseña: {self.contraseña}\nInventario: {self.inventario}"
    def agregar_producto(self, nombre_producto, cantidad_producto, precio_producto=0):
        for producto in self.inventario:
            if nombre_producto == producto.nombre:
                producto.cantidad += cantidad_producto
                return
        self.inventario.append(Producto(nombre_producto, cantidad_producto, precio_producto))
