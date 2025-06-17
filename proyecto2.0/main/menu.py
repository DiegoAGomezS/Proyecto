import models.products as c
import dao.functions as f

productos = f.productDao()

def menu ():
    print("""
          1. agregar producto
          2. mostrar inventario
          3. distribuir producto
          6. salir""")

def main():
    while (True):
        menu()
        option = input()
        if option == '1':
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio= float(input("Ingrese el precio del producto: "))
            producto = c.product(producto, cantidad, precio)
            productos.add(producto)
            if producto.cantidad > 0:
                print(f"Producto {producto.producto} agregado con éxito.")
            else:
                print("La cantidad del producto debe ser mayor a 0.")
            if producto.precio <= 0:
                print("El precio del producto debe ser mayor a 0.")
        elif option == '2':
            print("Inventario:")
            productos.show()
        elif option == '3':
            producto = input("Ingrese el nombre del producto a distribuir: ")
            cantidad = int(input("Ingrese la cantidad a distribuir: "))
            productos.distribute(producto, cantidad)
        elif option == '6':
            print("Saliendo del programa...")
            break