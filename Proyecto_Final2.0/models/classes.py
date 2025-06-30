class Producto:
    def __init__(self, id, nombre, precio, cantidad, fecha_registro, ultima_fecha_retiro=None):
        # self se refiere al objeto actual que se está creando
        # Guardamos todos los datos como atributos del objeto
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_registro = fecha_registro
        self.ultima_fecha_retiro = ultima_fecha_retiro

# Clase que representa una distribución o retiro de producto
class Distribucion:
    def __init__(self, id_producto, nombre_producto, cantidad, fecha_retiro):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.cantidad = cantidad
        self.fecha_retiro = fecha_retiro