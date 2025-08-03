# Proyecto gestión de inventario

import csv
import os
import hashlib
import re

# Clase que define cada producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio, categoria="Sin categoría"):
        if not nombre:
            raise ValueError("El nombre del producto no puede estar vacío")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
            
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria

    # Método para mostrar el producto
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}, Categoría: {self.categoria}"
    
    def to_dict(self):
        # Convierte el producto a un diccionario para exportación CSV
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": str(self.cantidad),
            "precio": str(self.precio),
            "categoria": self.categoria
        }

class GestorInventario:
    def __init__(self):
        self.productos = {}
        self.proximo_id = 1  # Contador para IDs automáticos
        self.categorias = ["Tecnologia", "Hogar", "Alimentos"]  # Categorías disponibles

    def _generar_id_unico(self):
        # Genera un ID único con formato 001, 002, etc.
        while True:
            id_str = f"{self.proximo_id:03d}"
            if id_str not in self.productos:
                return id_str
            self.proximo_id += 1

    # Método para mostrar todos los productos
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        print("\n--- Productos en Inventario ---")
        for producto in self.productos.values():
            print(producto)

    # Método para agregar producto
    def agregar_producto(self):
        try:
            print("\n--- Agregar Producto ---")
            id_producto = input("ID del producto (dejar en blanco para auto-generar): ").strip()
            if not id_producto:
                id_producto = self._generar_id_unico()
                
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("El nombre del producto no puede estar vacío.")
                return
                
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            
            # Mostrar categorías disponibles
            self.mostrar_categorias()
            opcion_categoria = input("Seleccione una categoría (número) o deje en blanco para 'Sin categoría': ").strip()
            
            categoria = "Sin categoría"
            if opcion_categoria:
                try:
                    indice = int(opcion_categoria)
                    categoria_seleccionada = self.obtener_categoria_por_indice(indice)
                    if categoria_seleccionada is not None:
                        categoria = categoria_seleccionada
                    else:
                        print("Categoría no válida. Se usará 'Sin categoría'.")
                except ValueError:
                    print("Entrada no válida. Se usará 'Sin categoría'.")
            
            producto = Producto(id_producto, nombre, cantidad, precio, categoria)
            self.productos[id_producto] = producto
            print(f"Producto agregado exitosamente con ID: {id_producto}")
        except ValueError as e:
            print(f"Error al agregar producto: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    # Importar productos desde archivo CSV
    def importar_productos(self):
        try:
            nombre_archivo = input("Nombre del archivo CSV (dejar en blanco para 'sample_products.csv'): ").strip()
            if not nombre_archivo:
                nombre_archivo = "sample_products.csv"
                
            if not os.path.exists(nombre_archivo):
                print(f"El archivo {nombre_archivo} no existe.")
                return
                
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    # Crear producto desde los datos del CSV
                    id_producto = fila["id"]
                    nombre = fila["nombre"]
                    cantidad = int(fila["cantidad"])
                    precio = float(fila["precio"])
                    categoria = fila.get("categoria", "Sin categoría")
                    
                    producto = Producto(id_producto, nombre, cantidad, precio, categoria)
                    self.productos[id_producto] = producto
                    
            print(f"Productos importados exitosamente desde {nombre_archivo}")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no fue encontrado.")
        except Exception as e:
            print(f"Error al importar productos: {e}")

    # Eliminar producto del inventario
    def eliminar_producto(self):
        try:
            print("\n--- Eliminar Producto ---")
            id_producto = input("ID del producto a eliminar: ").strip()
            if not id_producto:
                print("El ID del producto no puede estar vacío.")
                return
                
            if id_producto in self.productos:
                del self.productos[id_producto]
                print("Producto eliminado exitosamente.")
            else:
                print("No se encontró un producto con ese ID.")
        except Exception as e:
            print(f"Error al eliminar producto: {e}")

    # Modificar nombre de producto
    def modificar_nombre_producto(self):
        try:
            print("\n--- Modificar Nombre de Producto ---")
            id_producto = input("ID del producto a modificar: ").strip()
            if not id_producto:
                print("El ID del producto no puede estar vacío.")
                return
                
            producto = self.productos.get(id_producto)
            if not producto:
                print("No se encontró un producto con ese ID.")
                return
                
            print(f"Nombre actual: {producto.nombre}")
            nuevo_nombre = input("Nuevo nombre: ").strip()
            if not nuevo_nombre:
                print("El nombre no puede estar vacío.")
                return
                
            producto.nombre = nuevo_nombre
            print("Nombre actualizado exitosamente.")
        except ValueError as e:
            print(f"Error al modificar nombre: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    # Modificar cantidad de producto
    def modificar_cantidad_producto(self):
        try:
            print("\n--- Modificar Cantidad de Producto ---")
            id_producto = input("ID del producto a modificar: ").strip()
            if not id_producto:
                print("El ID del producto no puede estar vacío.")
                return
                
            producto = self.productos.get(id_producto)
            if not producto:
                print("No se encontró un producto con ese ID.")
                return
                
            print(f"Cantidad actual: {producto.cantidad}")
            nueva_cantidad = int(input("Nueva cantidad: "))
            
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                return
            
            producto.cantidad = nueva_cantidad
            print("Cantidad actualizada exitosamente.")
        except ValueError as e:
            print(f"Error al modificar cantidad: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    # Modificar precio de producto
    def modificar_precio_producto(self):
        try:
            print("\n--- Modificar Precio de Producto ---")
            id_producto = input("ID del producto a modificar: ").strip()
            if not id_producto:
                print("El ID del producto no puede estar vacío.")
                return
                
            producto = self.productos.get(id_producto)
            if not producto:
                print("No se encontró un producto con ese ID.")
                return
                
            print(f"Precio actual: ${producto.precio:.2f}")
            nuevo_precio = float(input("Nuevo precio: "))
            
            if nuevo_precio < 0:
                print("El precio no puede ser negativo.")
                return
            
            producto.precio = nuevo_precio
            print("Precio actualizado exitosamente.")
        except ValueError as e:
            print(f"Error al modificar precio: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    # Exportar productos a archivo CSV
    def exportar_productos(self):
        try:
            nombre_archivo = input("Nombre del archivo de exportación (dejar en blanco para 'productos_exportados.csv'): ").strip()
            if not nombre_archivo:
                nombre_archivo = "productos_exportados.csv"
                
            with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
                # Escribir encabezado
                archivo.write("id,nombre,cantidad,precio,categoria\n")
                # Escribir productos
                for producto in self.productos.values():
                    archivo.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio:.2f},{producto.categoria}\n")
                    
            print(f"Productos exportados exitosamente a {nombre_archivo}")
        except Exception as e:
            print(f"Error al exportar productos: {e}")

    # Mostrar productos por categoría
    def mostrar_productos_por_categoria(self):
        try:
            print("\n--- Mostrar Productos por Categoría ---")
            self.mostrar_categorias()
            opcion_categoria = input("Seleccione una categoría (número): ").strip()
            
            try:
                indice = int(opcion_categoria)
                categoria = self.obtener_categoria_por_indice(indice)
                if categoria is not None:
                    print(f"Productos en la categoría '{categoria}':")
                    encontrados = False
                    for producto in self.productos.values():
                        if producto.categoria == categoria:
                            print(producto)
                            encontrados = True
                    if not encontrados:
                        print("No hay productos en esta categoría.")
                else:
                    print("Categoría no válida.")
            except ValueError:
                print("Entrada no válida.")
        except Exception as e:
            print(f"Error al mostrar productos por categoría: {e}")

    # Mostrar productos de la categoría "Tecnologia"
    def mostrar_productos_tecnologia(self):
        """Muestra todos los productos que pertenecen a la categoría 'Tecnologia'"""
        print("\n--- Productos de Tecnologia ---")
        encontrados = False
        for producto in self.productos.values():
            if producto.categoria == "Tecnologia":
                print(producto)
                encontrados = True
        if not encontrados:
            print("No hay productos en la categoría 'Tecnologia'.")

    # Comprar producto (para clientes)
    def comprar_producto(self):
        try:
            print("\n--- Comprar Producto ---")
            id_producto = input("ID del producto a comprar: ").strip()
            if not id_producto:
                print("El ID del producto no puede estar vacío.")
                return
                
            producto = self.productos.get(id_producto)
            if not producto:
                print("No se encontró un producto con ese ID.")
                return
                
            print(f"Producto seleccionado: {producto}")
            cantidad = int(input("Cantidad a comprar: "))
            
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                return
                
            if cantidad > producto.cantidad:
                print(f"No hay suficiente stock. Disponible: {producto.cantidad}")
                return
                
            # Actualizar la cantidad del producto
            producto.cantidad -= cantidad
            print(f"Compra realizada exitosamente. Total: ${producto.precio * cantidad:.2f}")
            print(f"Productos restantes en inventario: {producto.cantidad}")
        except ValueError as e:
            print(f"Error al comprar producto: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def mostrar_categorias(self):
        print("\nCategorías disponibles:")
        for i, categoria in enumerate(self.categorias):
            print(f"{i + 1}. {categoria}")

    def obtener_categoria_por_indice(self, indice):
        if 0 < indice <= len(self.categorias):
            return self.categorias[indice - 1]
        return None


class Usuario:
    def __init__(self, nombre, contraseña, tipo, hash_password=None):
        if not nombre or not contraseña:
            raise ValueError("Nombre y contraseña son requeridos")
        if tipo not in ['vendedor', 'cliente']:
            raise ValueError("Tipo de usuario debe ser 'vendedor' o 'cliente'")
            
        self.nombre = nombre
        self.tipo = tipo  # 'vendedor' o 'cliente'
        
        # Determinar si debemos hashear la contraseña
        if hash_password is None:
            # Auto-detect: si la contraseña parece hasheada (hex de cierta longitud), no hashear
            # De lo contrario, hashear si cumple con los requisitos
            if self._parece_hasheada(contraseña):
                self.contraseña = contraseña
                self._contraseña_hasheada = True
            elif self._validar_contraseña(contraseña):
                self.contraseña = self._hash_contraseña(contraseña)
                self._contraseña_hasheada = True
            else:
                # Contraseña débil, almacenar en texto plano por compatibilidad
                self.contraseña = contraseña
                self._contraseña_hasheada = False
        elif hash_password:
            if not self._validar_contraseña(contraseña):
                raise ValueError("La contraseña no cumple con los requisitos de seguridad")
            self.contraseña = self._hash_contraseña(contraseña)
            self._contraseña_hasheada = True
        else:
            # Para compatibilidad con contraseñas existentes en texto plano
            self.contraseña = contraseña
            self._contraseña_hasheada = False

    @property
    def contraseña_hasheada(self):
        return self._contraseña_hasheada

    @contraseña_hasheada.setter
    def contraseña_hasheada(self, value):
        self._contraseña_hasheada = value

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}"
        
    def _hash_contraseña(self, contraseña):
        """Genera un hash SHA-256 de la contraseña con salto"""
        salt = "salt_unico_para_inventario"
        return hashlib.sha256((contraseña + salt).encode()).hexdigest()

    def _validar_contraseña(self, contraseña):
        """Valida que la contraseña cumpla con ciertos requisitos de seguridad"""
        errores = []
        if len(contraseña) < 6:
            errores.append("debe tener al menos 6 caracteres")
        # Al menos una mayúscula, una minúscula y un número
        if not re.search(r"[A-Z]", contraseña):
            errores.append("debe incluir al menos una letra mayúscula")
        if not re.search(r"[a-z]", contraseña):
            errores.append("debe incluir al menos una letra minúscula")
        if not re.search(r"[0-9]", contraseña):
            errores.append("debe incluir al menos un número")
        return len(errores) == 0, errores
    
    def _parece_hasheada(self, contraseña):
        """Determina si una contraseña parece estar hasheada (hex de 64 caracteres)"""
        return len(contraseña) == 64 and re.match(r"^[a-fA-F0-9]+$", contraseña)
    
    def verificar_contraseña(self, contraseña):
        """Verificar si la contraseña proporcionada es correcta"""
        if self.contraseña_hasheada:
            # Si la contraseña almacenada parece hasheada, comparar hashes
            if self._parece_hasheada(self.contraseña):
                return self.contraseña == self._hash_contraseña(contraseña)
            else:
                # Si no parece hasheada pero se marcó como hasheada, comparar directamente
                return self.contraseña == contraseña
        else:
            # Compatibilidad con contraseñas en texto plano
            return self.contraseña == contraseña
    
    def actualizar_contraseña(self, nueva_contraseña):
        """Actualiza la contraseña del usuario con una nueva contraseña hasheada"""
        es_valida, errores = self._validar_contraseña(nueva_contraseña)
        if not es_valida:
            mensaje_error = "La nueva contraseña no cumple con los requisitos de seguridad: " + ", ".join(errores) + "."
            raise ValueError(mensaje_error)
        self.contraseña = self._hash_contraseña(nueva_contraseña)
        self.contraseña_hasheada = True
