import pickle
import os

#Clase del inventario
class ProductDao:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

#Función encargada de mostrar los productos y sus especificaciones
    def show(self):
        for p in self.products:
            print(f"ID: {p.id} | Nombre: {p.nombre} | Precio: ${p.precio:.2f} | Cantidad: {p.cantidad} | Fecha registro: {p.fecha_registro} | Último retiro: {p.ultima_fecha_retiro}")

#Función encargada de encontrar un producto específico según su ID
    def find_by_id(self, id_producto):
        return next((p for p in self.products if p.id == id_producto), None)

#Función encargada de guardar información con respecto al inventario en un archivo.
    def guardar_inventario(self):
        with open("inventario.bin", "wb") as f:
            pickle.dump(self.products, f)
        print("Inventario guardado en inventario.bin")

#Función encargada de cargar la información previamente guardada sobre el inventario.
    def cargar_inventario(self):
        if os.path.exists("inventario.bin"):
            with open("inventario.bin", "rb") as f:
                self.products = pickle.load(f)
            print("Inventario cargado de inventario.bin")
        else:
            print("No se encontró inventario.bin. Se creará uno nuevo al salir.")