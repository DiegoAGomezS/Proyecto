class productDao:
    def __init__(self):
        self.productos = []  # Se crea una lista vacía para guardar los productos.

    def add(self, producto):  # Se agrega un producto a la lista.
        self.productos.append(producto)
        print("Producto agregado.")

    def show(self):  # Muestra todos los productos registrados.
        if not self.productos: # Si la lista está vacía, se informa al usuario.
            print("No hay productos registrados.")
        else:  # Si hay productos, se enumeran y muestran uno por uno.
            for i, producto in enumerate(self.productos, 1):
                print(f"{i}. {producto}")
        
    def distribuir(self, nombre, cantidad, destinatario):  # Distribuye una cantidad de un producto a un destinatario.
        for producto in self.productos: # Busca el producto por nombre 
            if producto.nombre.lower() == nombre.lower():
                if cantidad <= 0:  # No se puede distribuir una cantidad nula o negativa.
                    print("La cantidad debe ser mayor a cero.")
                    return
                if producto.existencia < cantidad:  # Verifica que haya suficiente inventario disponible.
                    print("No hay suficiente cantidad en el inventario.")
                    return
                # Se descuenta la cantidad distribuida del inventario.
                producto.existencia -= cantidad
                print(f"Se distribuyeron {cantidad} unidades de '{nombre}' a {destinatario}.")
                return
        # Si no se encuentra el producto, se muestra un mensaje.
        print("Ese producto no está en el inventario.")
