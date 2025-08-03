import trabajo as tr
import os
import csv

class SistemaTienda:
    def __init__(self):        
        # Por defecto, agregar dos vendedores solicitados
        self.usuarios = [
            tr.Usuario("Martin", "Martin", "vendedor"),
            tr.Usuario("Jilson", "Jilson", "vendedor")
        ]
        self.inventario = tr.GestorInventario()  # Corregido el nombre de la clase
        # Importar productos desde el archivo CSV
        self.inventario.importar_productos()
        self.usuario_actual = None
        # Cargar usuarios desde archivo si existe
        self.cargar_usuarios()

    # Registrar un nuevo cliente con validación mejorada
    def registrar_cliente(self):
        try:
            nombre = input("Ingrese su nombre de usuario: ").strip()
            if not nombre:
                print("El nombre de usuario no puede estar vacío.")
                return
                
            # Verificar si el usuario ya existe
            if any(usuario.nombre == nombre for usuario in self.usuarios):
                print("Ya existe un usuario con ese nombre.")
                return
                
            contraseña = input("Ingrese su contraseña: ").strip()
            if not contraseña:
                print("La contraseña no puede estar vacía.")
                return
                
            nuevo_usuario = tr.Usuario(nombre, contraseña, "cliente")
            self.usuarios.append(nuevo_usuario)
            print("Cuenta de cliente creada exitosamente.")
            # Mostrar si la contraseña fue hasheada
            if nuevo_usuario.contraseña_hasheada:
                print("La contraseña ha sido hasheada para mayor seguridad.")
            else:
                print("La contraseña no cumple con los requisitos de seguridad y se almacenará sin hash.")
            # Guardar usuarios en archivo
            self.guardar_usuarios()
        except ValueError as e:
            print(f"Error al crear la cuenta: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    # Iniciar sesión comprobando usuario y contraseña con mejor manejo de errores
    def iniciar_sesion(self):
        try:
            nombre = input("Usuario: ").strip()
            contraseña = input("Contraseña: ").strip()
            
            if not nombre or not contraseña:
                print("Usuario y contraseña son requeridos.")
                return False
                
            for usuario in self.usuarios:
                if usuario.nombre == nombre and usuario.verificar_contraseña(contraseña):
                    self.usuario_actual = usuario
                    print(f"Bienvenido {usuario.nombre} ({usuario.tipo})")
                    # Mostrar si la contraseña del usuario está hasheada
                    if usuario.contraseña_hasheada:
                        print("Tu contraseña está hasheada para mayor seguridad.")
                    else:
                        print("Tu contraseña no está hasheada.")
                    return True
            print("Usuario o contraseña incorrectos.")
            return False
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return False

    # Salir de la cuenta actual
    def cerrar_sesion(self):
        if self.usuario_actual:
            print(f"Saliendo de la cuenta de {self.usuario_actual.nombre}")
        self.usuario_actual = None

    # Guardar usuarios en archivo
    def guardar_usuarios(self):
        try:
            with open("usuarios.csv", "w", newline="", encoding="utf-8") as archivo:
                archivo.write("nombre,contraseña,tipo,contraseña_hasheada\n")
                for usuario in self.usuarios:
                    # Convertir booleano a string en minúsculas para consistencia
                    hasheada_str = "true" if usuario.contraseña_hasheada else "false"
                    archivo.write(f"{usuario.nombre},{usuario.contraseña},{usuario.tipo},{hasheada_str}\n")
        except Exception as e:
            print(f"Error al guardar usuarios: {e}")

    # Cargar usuarios desde archivo
    def cargar_usuarios(self):
        try:
            if os.path.exists("usuarios.csv"):
                with open("usuarios.csv", "r", encoding="utf-8") as archivo:
                    next(archivo)  # Saltar encabezado
                    for linea in archivo:
                        datos = linea.strip().split(",")
                        if len(datos) >= 3:
                            nombre, contraseña, tipo = datos[0], datos[1], datos[2]
                            # Verificar que el usuario no exista ya en la lista
                            if not any(u.nombre == nombre for u in self.usuarios):
                                # Si hay información sobre si la contraseña está hasheada
                                if len(datos) >= 4:
                                    contraseña_hasheada = datos[3].lower() == 'true'
                                    # Crear usuario con la información de hash
                                    self.usuarios.append(tr.Usuario(nombre, contraseña, tipo, hash_password=contraseña_hasheada))
                                else:
                                    # Crear usuario con valores por defecto
                                    self.usuarios.append(tr.Usuario(nombre, contraseña, tipo))
        except Exception as e:
            print(f"Error al cargar usuarios: {e}")

    # Métodos delegados al inventario
    def agregar_producto(self):
        self.inventario.agregar_producto()

    def eliminar_producto(self):
        self.inventario.eliminar_producto()

    def modificar_nombre_producto(self):
        self.inventario.modificar_nombre_producto()

    def modificar_cantidad_producto(self):
        self.inventario.modificar_cantidad_producto()

    def modificar_precio_producto(self):
        self.inventario.modificar_precio_producto()

    def exportar_productos(self):
        self.inventario.exportar_productos()

    def mostrar_productos_por_categoria(self):
        self.inventario.mostrar_productos_por_categoria()

    def comprar_producto(self):
        self.inventario.comprar_producto()

    # Actualizar contraseña del usuario actual
    def actualizar_contraseña_usuario(self):
        if not self.usuario_actual:
            print("Debes iniciar sesión primero.")
            return
            
        try:
            print("\n--- Actualizar Contraseña ---")
            contraseña_actual = input("Contraseña actual: ").strip()
            if not contraseña_actual:
                print("La contraseña actual no puede estar vacía.")
                return
                
            # Verificar que la contraseña actual sea correcta
            if not self.usuario_actual.verificar_contraseña(contraseña_actual):
                print("La contraseña actual es incorrecta.")
                return
                
            nueva_contraseña = input("Nueva contraseña: ").strip()
            if not nueva_contraseña:
                print("La nueva contraseña no puede estar vacía.")
                return
                
            # Intentar actualizar la contraseña
            self.usuario_actual.actualizar_contraseña(nueva_contraseña)
            print("Contraseña actualizada exitosamente.")
            # Mostrar si la nueva contraseña fue hasheada
            if self.usuario_actual.contraseña_hasheada:
                print("La nueva contraseña ha sido hasheada para mayor seguridad.")
            else:
                print("La nueva contraseña no cumple con los requisitos de seguridad.")
            # Guardar usuarios en archivo
            self.guardar_usuarios()
        except ValueError as e:
            print(f"Error al actualizar la contraseña: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    # Eliminar cuenta de cliente (solo para clientes)
    def eliminar_cuenta_cliente(self):
        if not self.usuario_actual:
            print("Debes iniciar sesión primero.")
            return
            
        # Verificar que el usuario sea un cliente
        if self.usuario_actual.tipo != "cliente":
            print("Solo los clientes pueden eliminar su cuenta.")
            return
            
        try:
            print("\n--- Eliminar Cuenta de Cliente ---")
            confirmacion = input("¿Estás seguro de que quieres eliminar tu cuenta? Esta acción no se puede deshacer. (sí/no): ").strip().lower()
            if confirmacion != "sí" and confirmacion != "si":
                print("Eliminación de cuenta cancelada.")
                return
                
            contraseña = input("Ingresa tu contraseña para confirmar: ").strip()
            if not contraseña:
                print("La contraseña no puede estar vacía.")
                return
                
            # Verificar que la contraseña sea correcta
            if not self.usuario_actual.verificar_contraseña(contraseña):
                print("Contraseña incorrecta. Eliminación de cuenta cancelada.")
                return
                
            # Eliminar al usuario de la lista de usuarios
            self.usuarios = [u for u in self.usuarios if u.nombre != self.usuario_actual.nombre]
            print("Cuenta eliminada exitosamente.")
            # Guardar usuarios en archivo
            self.guardar_usuarios()
            # Cerrar sesión
            self.cerrar_sesion()
        except Exception as e:
            print(f"Error al eliminar la cuenta: {e}")

    # Solicitar recuperación de contraseña
    def solicitar_recuperacion_contraseña(self):
        try:
            print("\n--- Solicitar Recuperación de Contraseña ---")
            nombre_usuario = input("Ingrese su nombre de usuario: ").strip()
            
            if not nombre_usuario:
                print("El nombre de usuario no puede estar vacío.")
                return
                
            # Verificar si el usuario existe
            usuario_encontrado = None
            for usuario in self.usuarios:
                if usuario.nombre == nombre_usuario and usuario.tipo == "cliente":
                    usuario_encontrado = usuario
                    break
                    
            if not usuario_encontrado:
                print("No se encontró un cliente con ese nombre de usuario.")
                return
                
            # Verificar si ya hay una solicitud pendiente
            if os.path.exists("solicitudes_recuperacion.csv"):
                with open("solicitudes_recuperacion.csv", "r", encoding="utf-8") as archivo:
                    for linea in archivo:
                        datos = linea.strip().split(",")
                        if len(datos) >= 2 and datos[0] == nombre_usuario:
                            print("Ya existe una solicitud de recuperación pendiente para este usuario.")
                            return
            
            # Guardar la solicitud en un archivo
            with open("solicitudes_recuperacion.csv", "a", newline="", encoding="utf-8") as archivo:
                # Si el archivo está vacío, escribir encabezado
                if archivo.tell() == 0:
                    archivo.write("usuario,estado\n")
                archivo.write(f"{nombre_usuario},pendiente\n")
                
            print("Solicitud de recuperación enviada. Un vendedor debe aprobarla.")
        except Exception as e:
            print(f"Error al solicitar recuperación de contraseña: {e}")

    # Aprobar solicitud de recuperación de contraseña (solo para vendedores)
    def aprobar_solicitud_recuperacion(self):
        try:
            print("\n--- Aprobar Solicitud de Recuperación de Contraseña ---")
            
            # Verificar si hay solicitudes pendientes
            if not os.path.exists("solicitudes_recuperacion.csv"):
                print("No hay solicitudes de recuperación pendientes.")
                return
                
            solicitudes_pendientes = []
            with open("solicitudes_recuperacion.csv", "r", encoding="utf-8") as archivo:
                next(archivo)  # Saltar encabezado
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) >= 2 and datos[1] == "pendiente":
                        solicitudes_pendientes.append(datos[0])
                        
            if not solicitudes_pendientes:
                print("No hay solicitudes de recuperación pendientes.")
                return
                
            print("Solicitudes pendientes:")
            for i, usuario in enumerate(solicitudes_pendientes, 1):
                print(f"{i}. {usuario}")
                
            seleccion = input("Seleccione una solicitud para aprobar (número) o 0 para cancelar: ").strip()
            
            if seleccion == "0":
                print("Operación cancelada.")
                return
                
            try:
                indice = int(seleccion) - 1
                if 0 <= indice < len(solicitudes_pendientes):
                    usuario_seleccionado = solicitudes_pendientes[indice]
                    
                    # Actualizar el estado de la solicitud a "aprobada"
                    lineas = []
                    with open("solicitudes_recuperacion.csv", "r", encoding="utf-8") as archivo:
                        lineas = archivo.readlines()
                        
                    with open("solicitudes_recuperacion.csv", "w", newline="", encoding="utf-8") as archivo:
                        for linea in lineas:
                            datos = linea.strip().split(",")
                            if len(datos) >= 2 and datos[0] == usuario_seleccionado and datos[1] == "pendiente":
                                archivo.write(f"{datos[0]},aprobada\n")
                            else:
                                archivo.write(linea)
                                
                    print(f"Solicitud de {usuario_seleccionado} aprobada. El usuario puede ahora establecer una nueva contraseña.")
                else:
                    print("Selección no válida.")
            except ValueError:
                print("Entrada no válida.")
        except Exception as e:
            print(f"Error al aprobar solicitud de recuperación: {e}")

    # Establecer nueva contraseña después de aprobación
    def establecer_nueva_contraseña(self):
        try:
            print("\n--- Establecer Nueva Contraseña ---")
            nombre_usuario = input("Ingrese su nombre de usuario: ").strip()
            
            if not nombre_usuario:
                print("El nombre de usuario no puede estar vacío.")
                return
                
            # Verificar si hay una solicitud aprobada para este usuario
            if not os.path.exists("solicitudes_recuperacion.csv"):
                print("No hay solicitudes de recuperación.")
                return
                
            solicitud_aprobada = False
            with open("solicitudes_recuperacion.csv", "r", encoding="utf-8") as archivo:
                next(archivo)  # Saltar encabezado
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) >= 2 and datos[0] == nombre_usuario and datos[1] == "aprobada":
                        solicitud_aprobada = True
                        break
                        
            if not solicitud_aprobada:
                print("No hay una solicitud aprobada para este usuario.")
                return
                
            # Encontrar al usuario
            usuario_encontrado = None
            for usuario in self.usuarios:
                if usuario.nombre == nombre_usuario:
                    usuario_encontrado = usuario
                    break
                    
            if not usuario_encontrado:
                print("Usuario no encontrado.")
                return
                
            nueva_contraseña = input("Ingrese su nueva contraseña: ").strip()
            if not nueva_contraseña:
                print("La nueva contraseña no puede estar vacía.")
                return
                
            # Actualizar la contraseña del usuario
            usuario_encontrado.actualizar_contraseña(nueva_contraseña)
            print("Contraseña actualizada exitosamente.")
            
            # Eliminar la solicitud de recuperación
            lineas = []
            with open("solicitudes_recuperacion.csv", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                
            with open("solicitudes_recuperacion.csv", "w", newline="", encoding="utf-8") as archivo:
                for linea in lineas:
                    datos = linea.strip().split(",")
                    if len(datos) >= 2 and datos[0] != nombre_usuario:
                        archivo.write(linea)
                        
            # Guardar usuarios actualizados
            self.guardar_usuarios()
        except ValueError as e:
            print(f"Error al establecer nueva contraseña: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    # Menú para iniciar sesión o registrar una cuenta
    def menu_principal(self):
        while True:
            if not self.usuario_actual:
                print("\n--- Sistema de Tienda ---")
                print("1. Iniciar sesión")
                print("2. Registrarse como cliente")
                print("3. Solicitar recuperación de contraseña")
                print("4. Establecer nueva contraseña (después de aprobación)")
                print("5. Salir")
                opcion = input("Seleccione una opción: ").strip()
                
                if opcion == "1":
                    if self.iniciar_sesion():
                        self.menu_usuario()
                elif opcion == "2":
                    self.registrar_cliente()
                elif opcion == "3":
                    self.solicitar_recuperacion_contraseña()
                elif opcion == "4":
                    self.establecer_nueva_contraseña()
                elif opcion == "5":
                    print("Hasta luego.")
                    break
                else:
                    print("Opción no válida.")
            else:
                self.menu_usuario()

    # Menú del usuario que cambia dependiendo de si es cliente o vendedor
    def menu_usuario(self):
        usuario = self.usuario_actual
        while True:
            print(f"\n--- Menú ({usuario.tipo}) ---")
            if usuario.tipo == "vendedor":
                print("1. Agregar producto")
                print("2. Importar productos desde archivo CSV")
                print("3. Eliminar producto")
                print("4. Modificar nombre de producto")
                print("5. Modificar cantidad de producto")
                print("6. Modificar precio de producto")
                print("7. Mostrar productos actuales")
                print("8. Exportar productos a archivo CSV")
                print("9. Aprobar solicitud de recuperación de contraseña")
                print("10. Actualizar contraseña")
                print("11. Salir de la cuenta")
            elif usuario.tipo == "cliente":
                print("1. Ver todos los productos")
                print("2. Ver productos por categoría")
                print("3. Comprar producto")
                print("4. Actualizar contraseña")
                print("5. Eliminar cuenta")
                print("6. Cambiar de cuenta")
                print("7. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if usuario.tipo == "vendedor":
                if opcion == "1":
                    self.agregar_producto()
                elif opcion == "2":
                    self.inventario.importar_productos()
                elif opcion == "3":
                    self.eliminar_producto()
                elif opcion == "4":
                    self.modificar_nombre_producto()
                elif opcion == "5":
                    self.modificar_cantidad_producto()
                elif opcion == "6":
                    self.modificar_precio_producto()
                elif opcion == "7":
                    self.inventario.mostrar_productos()
                elif opcion == "8":
                    self.exportar_productos()
                elif opcion == "9":
                    self.aprobar_solicitud_recuperacion()
                elif opcion == "10":
                    self.actualizar_contraseña_usuario()
                elif opcion == "11":
                    self.cerrar_sesion()
                    break
                else:
                    print("Opción no válida.")
            elif usuario.tipo == "cliente":
                if opcion == "1":
                    self.inventario.mostrar_productos()
                elif opcion == "2":
                    self.mostrar_productos_por_categoria()
                elif opcion == "3":
                    self.comprar_producto()
                elif opcion == "4":
                    self.actualizar_contraseña_usuario()
                elif opcion == "5":
                    self.eliminar_cuenta_cliente()
                elif opcion == "6":
                    self.cerrar_sesion()
                    break
                elif opcion == "7":
                    print("Hasta luego.")
                    exit()
                else:
                    print("Opción no válida.")

# Crear instancia del sistema y ejecutar el menú principal
if __name__ == "__main__":
    sistema = SistemaTienda()
    sistema.menu_principal()
