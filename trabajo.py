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
