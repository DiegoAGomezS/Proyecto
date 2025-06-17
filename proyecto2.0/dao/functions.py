##Data Acces Object (DAO)
class productDao:
    def __init__(self):
        self.productos = []
        
    def add(self, producto):
        self.productos.append(producto)
        
    def show(self):
        for producto in self.productos:
            print(f"producto: {producto.producto} || cantidad: {producto.cantidad} || precio: {producto.precio}$")
    def distribute(self, producto, cantidad):
        for p in self.productos:
            if p.producto == producto:
                if p.cantidad >= cantidad:
                    p.cantidad -= cantidad
                    print(f"Distribuido {cantidad} de {producto}. Cantidad restante: {p.cantidad}")
                else:
                    print(f"No hay suficiente cantidad de {producto} para distribuir. Cantidad disponible: {p.cantidad}")
                return
        print(f"Producto {producto} no encontrado.")
        
        