class Product:
    def __init__(self, nombre, precio, existencia):  # Esta parte se ejecuta cuando se crea un nuevo producto
        self.nombre = nombre  # Guarda el nombre del producto
        self.precio = precio   # Guarda el precio del producto
        self.existencia = existencia  # Guarda cuántas unidades hay disponibles

    def __str__(self):  # Define cómo se mostrará el producto cuando lo imprimimos
        return f"{self.nombre} | Precio: ${self.precio:.2f} | Existencia: {self.existencia}"
