import pandas as pd
from models.classes import Distribucion

#Clase para las distribuciones
class DistributionDao:
    def __init__(self):
        self.distributions = []

#Función para cargar la información del excel
    def cargar_distribuciones(self, filename="distribuciones.xlsx"):
        try:
            df = pd.read_excel(filename)
            self.distributions = []
            for _, row in df.iterrows():
                d = Distribucion(
                    id_producto=row['id_producto'],
                    nombre_producto=row['nombre_producto'],
                    cantidad=row['cantidad'],
                    fecha_retiro=row['fecha_retiro']
                )
                self.distributions.append(d)
            print(f"Distribuciones cargadas de {filename}")
        except FileNotFoundError:
            print(f"Archivo {filename} no encontrado. Se iniciará vacío.")

#Función encargada de guardar información de las distribuciones en el excel
    def guardar_distribuciones(self, filename="distribuciones.xlsx"):
        data = []
        for d in self.distributions:
            data.append({
                "id_producto": d.id_producto,
                "nombre_producto": d.nombre_producto,
                "cantidad": d.cantidad,
                "fecha_retiro": d.fecha_retiro
            })
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"Distribuciones guardadas en {filename}")

    def add(self, distribution):
        self.distributions.append(distribution)

    def show(self):
        if not self.distributions:
            print("No hay distribuciones registradas.")
            return
        for d in self.distributions:
            print(d)