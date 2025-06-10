class productDao:
    def __init__(self):
        self.productos = []  # Se crea una lista vacía para guardar los productos.

    def add(self, producto):  # Se agrega un producto a la lista.
        self.productos.append(producto)
        print("Producto agregado.")

    def show(self):  # Muestra todos los productos registrados.
        if not self.productos:
            print("No hay productos registrados.")
        else:
            for i, producto in enumerate(self.productos, 1):
                print(f"{i}. {producto}")

    def distribuir(self, nombre, cantidad, destinatario):  # Distribuye una cantidad de un producto a un destinatario.
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a cero.")
                    return
                if producto.existencia < cantidad:
                    print("No hay suficiente cantidad en el inventario.")
                    return
                producto.existencia -= cantidad
                print(f"Se distribuyeron {cantidad} unidades de '{nombre}' a {destinatario}.")
                return
        print("Ese producto no está en el inventario.")
