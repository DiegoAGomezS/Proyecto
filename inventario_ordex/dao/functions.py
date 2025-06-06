class productDao:
    def __init__(self):
        self.productos = [] # Se crea una lista vacía para guardar los productos.

    def add(self, producto): # Se agrega un producto a la lista.
        self.productos.append(producto)
        print("Producto agregado.")

    def show(self): # Muestra todos los productos registrados.
        if not self.productos:
            print("No hay productos registrados.")
        else:
            for i, producto in enumerate(self.productos, 1):
                print(f"{i}. {producto}")
