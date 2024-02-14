class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Args:
            id (int): ID único del producto.
            nombre (str): Nombre del producto.
            cantidad (int): Cantidad disponible del producto.
            precio (float): Precio del producto.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario.

        Args:
            producto (Producto): Producto a añadir.

        Returns:
            bool: True si el producto fue añadido con éxito, False si no.
        """
        if not self.buscar_producto_por_id(producto.get_id()):
            self.productos.append(producto)
            return True
        else:
            return False

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.

        Args:
            id (int): ID del producto a eliminar.

        Returns:
            bool: True si el producto fue eliminado con éxito, False si no.
        """
        producto = self.buscar_producto_por_id(id)
        if producto:
            self.productos.remove(producto)
            return True
        else:
            return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID.

        Args:
            id (int): ID del producto a actualizar.
            cantidad (int, optional): Nueva cantidad del producto. Default is None.
            precio (float, optional): Nuevo precio del producto. Default is None.

        Returns:
            bool: True si el producto fue actualizado con éxito, False si no.
        """
        producto = self.buscar_producto_por_id(id)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            return True
        else:
            return False

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca productos por su nombre.

        Args:
            nombre (str): Nombre (o parte del nombre) del producto a buscar.

        Returns:
            list: Lista de productos que coinciden con el nombre buscado.
        """
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados
    # Agregar una pausa para esperar la entrada del usuario antes de volver al menú
    def buscar_producto_por_id(self, id):
        """
        Busca un producto por su ID.

        Args:
            id (int): ID del producto a buscar.
        Returns:
            Producto: Producto con el ID especificado, o None si no se encuentra.
        """
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        """
        for producto in self.productos:
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

        # Agregar una pausa para esperar la entrada del usuario antes de volver al menú
        input("\nPresione Enter para volver al menú...")


def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\nAlmacén de Pinturas FullColor - Menú:")
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos en el inventario")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("Ingrese ID del producto: "))
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            if inventario.agregar_producto(producto):
                print("Producto agregado exitosamente.")
            else:
                print("Ya existe un producto con ese ID.")
        elif opcion == "2":
            id = int(input("Ingrese ID del producto a eliminar: "))
            if inventario.eliminar_producto(id):
                print("Producto eliminado exitosamente.")
            else:
                print("Producto no encontrado.")
        elif opcion == "3":
            id = int(input("Ingrese ID del producto a actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no actualizar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no actualizar): ")
            if cantidad:
                cantidad = int(cantidad)
            if precio:
                precio = float(precio)
            if inventario.actualizar_producto(id, cantidad=cantidad, precio=precio):
                print("Producto actualizado exitosamente.")
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre o parte del nombre del producto: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                print("Resultados de la búsqueda:")
                for producto in resultados:
                    print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
                    input("\nPresione Enter para volver al menú...")
            else:
                print("Producto no encontrado.")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()

