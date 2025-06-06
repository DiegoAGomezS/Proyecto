import models.classes as c
import dao.functions as f

productos = f.productDao() # Crea un objeto que se encargará de guardar y mostrar productos

def menu(): # Muestra el menú de opciones.
    print("""
1. Agregar producto
2. Mostrar productos
6. Salir
""")

def main():
    while True: # Bucle principal del programa.
        menu() # Muestra el menú.
        option = input("Digite una opción: ") # Pide la opción al usuario.

        if option == '1':  # Agregar producto.
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: ")) 
                existencia = int(input("Existencia: "))
            except ValueError: # Vuelve al menú si hay error.
                print("Error: precio debe ser decimal y existencia un número entero.")
                continue
            
            # Crea un nuevo producto con los datos ingresados.  
            producto = c.Product(nombre, precio, existencia)
            productos.add(producto)

        elif option == '2':
            print("\n--- Lista de Productos ---")
            productos.show() # Mostrar todos los productos.
 
        elif option == '6': # Salir del programa.
            print("¡Adiós!")
            break

        else: # Opción inválida.
            print("Opción no válida, intente de nuevo.")
