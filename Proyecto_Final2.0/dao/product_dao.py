import pickle
import os

class ProductDao:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def show(self):
        for p in self.products:
            print(f"ID: {p.id} | Nombre: {p.nombre} | Precio: ${p.precio:.2f} | Cantidad: {p.cantidad} | Fecha registro: {p.fecha_registro} | Último retiro: {p.ultima_fecha_retiro}")

    def find_by_id(self, id_producto):
        return next((p for p in self.products if p.id == id_producto), None)

    def guardar_inventario(self):
        with open("inventario.bin", "wb") as f:
            pickle.dump(self.products, f)
        print("💾 Inventario guardado en inventario.bin")

    def cargar_inventario(self):
        if os.path.exists("inventario.bin"):
            with open("inventario.bin", "rb") as f:
                self.products = pickle.load(f)
            print("✔️ Inventario cargado de inventario.bin")
        else:
            print("📂 No se encontró inventario.bin. Se creará uno nuevo al salir.")