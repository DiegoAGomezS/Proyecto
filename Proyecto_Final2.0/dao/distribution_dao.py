import pickle
import os

class DistributionDao:
    def __init__(self):
        self.distributions = []

    def add(self, distribution):
        self.distributions.append(distribution)

    def show(self):
        for d in self.distributions:
            print(f"ID Producto: {d.id_producto} | Nombre: {d.nombre_producto} | Cantidad: {d.cantidad} | Fecha de retiro: {d.fecha_retiro}")

    def guardar_distribuciones(self):
        with open("distribuciones.bin", "wb") as f:
            pickle.dump(self.distributions, f)
        print("Distribuciones guardadas en distribuciones.bin")

    def cargar_distribuciones(self):
        if os.path.exists("distribuciones.bin"):
            with open("distribuciones.bin", "rb") as f:
                self.distributions = pickle.load(f)
            print("Distribuciones cargadas de distribuciones.bin")
        else:
            print("No se encontró distribuciones.bin. Se creará uno nuevo al salir.")