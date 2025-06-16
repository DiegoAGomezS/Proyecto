from dao.product_dao import ProductDao
from dao.distribution_dao import DistributionDao
from dao.inventario_minimo_dao import InventarioMinimoDao
from models.classes import Producto, Distribucion
from datetime import datetime

def menu():
    product_dao = ProductDao()
    distribution_dao = DistributionDao()

    product_dao.cargar_inventario()
    distribution_dao.cargar_distribuciones()
#Ejemplo
    while True:
        print("\n====== MENÚ DE INVENTARIO ======")
        print("1. Registrar producto")
        print("2. Mostrar inventario")
        print("3. Distribuir producto")
        print("4. Mostrar distribuciones")
        print("5. Calcular inventario mínimo")
        print("6. Salir y guardar inventario y distribuciones")
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            nombre = input("🔸 Ingresa el nombre del producto: ")
            try:
                precio = float(input("🔸 Precio: $"))
                cantidad = int(input("🔸 Cantidad: "))
            except ValueError:
                print("Valor inválido.")
                continue

            nuevo_id = max([p.id for p in product_dao.products], default=0) + 1
            fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            producto = Producto(nuevo_id, nombre, precio, cantidad, fecha_registro)
            product_dao.add(producto)
            print(f"Producto '{nombre}' registrado con ID {nuevo_id}.")

        elif opcion == "2":
            product_dao.show()

        elif opcion == "3":
            product_dao.show()
            try:
                id_producto = int(input("ID del producto a distribuir: "))
                producto = product_dao.find_by_id(id_producto)
                if not producto:
                    print("No existe ese producto.")
                    continue
                cantidad = int(input(f"Cantidad a retirar de '{producto.nombre}': "))
                if cantidad > producto.cantidad:
                    print("No hay suficiente stock.")
                    continue
                confirmar = input("¿Confirmar? (Y/N): ").upper()
                if confirmar == "Y":
                    producto.cantidad -= cantidad
                    fecha_retiro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    distribucion = Distribucion(producto.id, producto.nombre, cantidad, fecha_retiro)
                    distribution_dao.add(distribucion)
                    producto.ultima_fecha_retiro = fecha_retiro
                    print("Distribución realizada.")
            except ValueError:
                print("Valor inválido.")

        elif opcion == "4":
            distribution_dao.show()

        elif opcion == "5":
            product_dao.show()
            try:
                id_producto = int(input("ID para calcular inventario mínimo: "))
                inventario_minimo_dao = InventarioMinimoDao(product_dao.products, distribution_dao.distributions)
                resultado = inventario_minimo_dao.calcular_inventario_minimo(id_producto)
                print(resultado)
            except ValueError:
                print("Valor inválido.")

        elif opcion == "6":
            product_dao.guardar_inventario()
            distribution_dao.guardar_distribuciones()
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")