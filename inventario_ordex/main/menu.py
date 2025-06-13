# Se importan los módulos necesarios:
# - 'c' contiene las clases como Product.
# - 'f' contiene las funciones y clases DAO como productDao.
import models.classes as c
import dao.functions as f

productos = f.productDao()  # Crea un objeto que se encargará de guardar y mostrar productos

def menu():  # Muestra el menú de opciones
    print("""
1. Agregar producto
2. Mostrar productos
3. Distribuir producto
6. Salir
""")

""" Función principal que ejecuta el ciclo del menú de interacción con el usuario. """

def main():
    while True:  # Ciclo infinito hasta que el usuario elija salir.
        menu()  # Muestra el menú
        option = input("Digite una opción: ")  # Pide la opción al usuario

        if option == '1':  # Agregar producto
            print("\n--- AGREGAR PRODUCTO ---")
            nombre = input("Nombre del producto: ")
            try:  # Se solicita el precio y la existencia del producto.
                precio = float(input("Precio: "))
                existencia = int(input("Existencia: "))
            except ValueError:  # Vuelve al menú si hay error
                print("Error: precio debe ser decimal y existencia un número entero.")
                continue

            producto = c.Product(nombre, precio, existencia)  # Crea un nuevo producto
            productos.add(producto)  # Lo agrega a la lista

        elif option == '2':  # Mostrar productos
            print("\n--- LISTA DE PRODUCTOS ---")
            productos.show()

        elif option == '3':  # Distribuir producto
            print("\n--- DISTRIBUIR PRODUCTO ---")
            nombre = input("Nombre del producto a distribuir: ")
            try:
                cantidad = int(input("Cantidad a distribuir: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a cero.")
                    continue
                destinatario = input("¿A quién se le asigna?: ")
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            productos.distribuir(nombre, cantidad, destinatario)

        elif option == '6':  # Salir del programa
            print("¡Adiós!")
            break

        else:  # Opción inválida
            print("Opción no válida, intente de nuevo.")
