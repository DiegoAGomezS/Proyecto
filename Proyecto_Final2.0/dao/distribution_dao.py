import pickle  # Módulo para guardar y cargar objetos en archivos binarios
import os #  # Módulo para interactuar con el sistema de archivos.

# Clase encargada de manejar las distribuciones de productos
class DistributionDao:
    def __init__(self):
        self.distributions = [] # Lista que almacenará los objetos de distribución

    def add(self, distribution):  # Método para agregar una nueva distribución a la lista
        self.distributions.append(distribution)

    def show(self):  # Método para mostrar todas las distribuciones almacenadas
        for d in self.distributions:
            print(f"ID Producto: {d.id_producto} | Nombre: {d.nombre_producto} | Cantidad: {d.cantidad} | Fecha de retiro: {d.fecha_retiro}")

#Función encargada de guardar la información de las distribuciones en un archivo
    def guardar_distribuciones(self):
        with open("distribuciones.bin", "wb") as f: # Abre el archivo 'distribuciones.bin' en modo escritura binaria
            pickle.dump(self.distributions, f) # Guarda la lista de distribuciones usando pickle
        print("Distribuciones guardadas en distribuciones.bin") 

#Función encargada de cargar la información previamente guardada sobre las distribuciones
    def cargar_distribuciones(self):
        # Verifica si el archivo 'distribuciones.bin' existe
        if os.path.exists("distribuciones.bin"):
            # Abre el archivo en modo lectura binaria
            with open("distribuciones.bin", "rb") as f:
                # Carga las distribuciones desde el archivo y las asigna a la lista
                self.distributions = pickle.load(f)
            print("Distribuciones cargadas de distribuciones.bin")
        else:  # Si el archivo no existe, se notifica que se creará uno nuevo al guardar
            print("No se encontró distribuciones.bin. Se creará uno nuevo al salir.")
