class Producto:
    def __init__(self, id, nombre, precio, cantidad, fecha_registro=None, ultima_fecha_retiro=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_registro = fecha_registro
        self.ultima_fecha_retiro = ultima_fecha_retiro

    def __str__(self):
        return (f"ID: {self.id} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | "
                f"Cantidad: {self.cantidad} | Fecha registro: {self.fecha_registro} | "
                f"Último retiro: {self.ultima_fecha_retiro}")


class Distribucion:
    def __init__(self, id_producto, nombre_producto, cantidad, fecha_retiro):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.fecha_retiro = fecha_retiro

    def __str__(self):
        return (f"ID Producto: {self.id_producto} | Nombre: {self.nombre_producto} | "
                f"Cantidad: {self.cantidad} | Fecha retiro: {self.fecha_retiro}")