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

def main():
    while True:  # Bucle principal del programa
        menu()  # Muestra el menú
        option = input("Digite una opción: ")  # Pide la opción al usuario

        if option == '1':  # Agregar producto
            print("\n--- AGREGAR PRODUCTO ---")
            nombre = input("Nombre del producto: ")
            try:
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

