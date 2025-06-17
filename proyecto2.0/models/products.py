class product:
    def __init__(self, nombre, cantidad, precio):
        self.producto = nombre
        self.cantidad = cantidad
        self.precio = precio
    def __str__(self):
        return f"Producto: {self.producto}, Cantidad: {self.cantidad}, Precio: {self.precio}"