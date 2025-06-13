from datetime import datetime

class InventarioMinimoDao:
    def calcular_minimo(self, id_producto, productos, distribuciones):
        producto = next((p for p in productos if p.id == id_producto), None)
        if not producto:
            return f"❌ Producto no encontrado."

        if not producto.fecha_registro:
            return f"❌ El producto '{producto.nombre}' no tiene fecha de registro."

        distribuciones_producto = [d for d in distribuciones if d.id_producto == id_producto]
        total_dist = len(distribuciones_producto)
        if total_dist == 0:
            return f"❌ No hay distribuciones registradas para este producto."

        formato = "%Y-%m-%d %H:%M:%S"
        fecha_registro = datetime.strptime(producto.fecha_registro, formato)

        if total_dist == 1:
            fecha_retiro = datetime.strptime(distribuciones_producto[0].fecha_retiro, formato)
            dias = (fecha_retiro - fecha_registro).days or 1
            cantidad = distribuciones_producto[0].cantidad
        else:
            fecha_penultima = datetime.strptime(distribuciones_producto[-2].fecha_retiro, formato)
            fecha_ultima = datetime.strptime(distribuciones_producto[-1].fecha_retiro, formato)
            dias = (fecha_ultima - fecha_penultima).days or 1
            cantidad = distribuciones_producto[-1].cantidad

        consumo_diario = cantidad / dias
        inventario_minimo = consumo_diario * 5

        return f"🔸 Inventario mínimo para '{producto.nombre}': {inventario_minimo:.2f} unidades."