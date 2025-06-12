import pandas as pd
from models.classes import Producto

class ProductDao:
    def __init__(self):
        self.products = []

    def load_from_excel(self, filename="inventario.xlsx"):
        try:
            df = pd.read_excel(filename)
            self.products = []
            for _, row in df.iterrows():
                p = Producto(
                    id=row['id'],
                    nombre=row['nombre'],
                    precio=row['precio'],
                    cantidad=row['cantidad'],
                    fecha_registro=row.get('fecha_registro', None),
                    ultima_fecha_retiro=row.get('ultima_fecha_retiro', None)
                )
                self.products.append(p)
            print(f"✔️ Inventario cargado de {filename}")
        except FileNotFoundError:
            print(f"⚠️ Archivo {filename} no encontrado. Se iniciará vacío.")

    def save_to_excel(self, filename="inventario.xlsx"):
        data = []
        for p in self.products:
            data.append({
                "id": p.id,
                "nombre": p.nombre,
                "precio": p.precio,
                "cantidad": p.cantidad,
                "fecha_registro": p.fecha_registro,
                "ultima_fecha_retiro": p.ultima_fecha_retiro
            })
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"💾 Inventario guardado en {filename}")

    def add(self, product):
        self.products.append(product)

    def show(self):
        if not self.products:
            print("📦 No hay productos en inventario.")
            return
        for p in self.products:
            print(p)
    
    def find_by_id(self, id_producto):
        return next((p for p in self.products if p.id == id_producto), None)