from datetime import datetime

class InventarioMinimoDao:
    def __init__(self, productos, distribuciones):
        self.productos = productos
        self.distribuciones = distribuciones

    def calcular_inventario_minimo(self, id_producto):
        producto = next((p for p in self.productos if p.id == id_producto), None)
        if not producto:
            return "Producto no encontrado."

        distribuciones_producto = [d for d in self.distribuciones if d.id_producto == id_producto]
        total_dist = len(distribuciones_producto)
        if total_dist == 0:
            return "No hay distribuciones registradas para este producto."

        formato = "%Y-%m-%d %H:%M:%S"
        if total_dist == 1:
            fecha_inicial = datetime.strptime(producto.fecha_registro, formato)
            fecha_retiro = datetime.strptime(distribuciones_producto[0].fecha_retiro, formato)
            dias = (fecha_retiro - fecha_inicial).days or 1
            cantidad = distribuciones_producto[0].cantidad
        else:
            fecha_penultima = datetime.strptime(distribuciones_producto[-2].fecha_retiro, formato)
            fecha_ultima = datetime.strptime(distribuciones_producto[-1].fecha_retiro, formato)
            dias = (fecha_ultima - fecha_penultima).days or 1
            cantidad = distribuciones_producto[-1].cantidad

        consumo_diario = cantidad / dias
        inventario_minimo = consumo_diario * 5

        return f"🔸 El inventario mínimo para '{producto.nombre}' es: {inventario_minimo:.2f} unidades."