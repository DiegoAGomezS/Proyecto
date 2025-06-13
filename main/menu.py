from dao.product_dao import ProductDao
from dao.distribution_dao import DistributionDao
from dao.inventario_minimo_dao import InventarioMinimoDao
from models.classes import Producto, Distribucion
from datetime import datetime

def menu():
    product_dao = ProductDao()
    distribution_dao = DistributionDao()
    inventario_minimo_dao = InventarioMinimoDao()

    product_dao.cargar_inventario()
    distribution_dao.cargar_distribuciones()

    while True:
        print("\n====== MENÚ DE INVENTARIO ======")
        print("\033[32m1. Registrar producto\033[0m")               # Verde
        print("\033[34m2. Mostrar inventario\033[0m")              # Azul
        print("\033[33m3. Distribuir producto\033[0m")             # Amarillo
        print("\033[37m4. Mostrar distribuciones\033[0m")          # Blanco
        print("\033[35m5. Calcular inventario mínimo\033[0m")      # Morado
        print("\033[31m6. Salir y guardar inventario y distribuciones\033[0m")  # Rojo
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            nombre = input("🔸 Ingresa el nombre del producto: ")
            try:
                precio = float(input("🔸 Ingresa el precio del producto: $"))
                if precio < 0:
                    print("❌ Error... Ingrese valores positivos.")
                    continue
                cantidad = int(input("🔸 Ingresa la cantidad disponible: "))
                if cantidad < 0:
                    print("❌ Error... Ingrese valores positivos.")
                    continue
            except ValueError:
                print("❌ Precio o cantidad inválidos.")
                continue

            nuevo_id = max([p.id for p in product_dao.products], default=0) + 1
            fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            producto = Producto(nuevo_id, nombre, precio, cantidad, fecha_registro)
            product_dao.add(producto)
            print(f"✅ Producto '{nombre}' registrado con ID {nuevo_id}.")

        elif opcion == "2":
            product_dao.show()

        elif opcion == "3":
            product_dao.show()
            try:
                id_producto = int(input("🔸 Ingresa el ID del producto a distribuir: "))
            except ValueError:
                print("❌ ID inválido.")
                continue
            producto = product_dao.find_by_id(id_producto)
            if not producto:
                print("❌ Producto no encontrado.")
                continue
            try:
                cantidad = int(input(f"🔸 Cantidad a retirar de '{producto.nombre}': "))
            except ValueError:
                print("❌ Cantidad inválida.")
                continue
            if cantidad > producto.cantidad:
                print("❌ No hay suficiente stock.")
                continue
            confirmar = input(f"¿Confirmar retiro de {cantidad} unidades de '{producto.nombre}'? (Y/N): ").upper()
            if confirmar == "Y":
                producto.cantidad -= cantidad
                fecha_retiro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                distribucion = Distribucion(producto.id, producto.nombre, cantidad, fecha_retiro)
                distribution_dao.add(distribucion)
                producto.ultima_fecha_retiro = fecha_retiro
                print(f"✅ Se retiraron {cantidad} unidades de '{producto.nombre}'.")
            else:
                print("🔸 Operación cancelada.")

        elif opcion == "4":
            distribution_dao.show()

        elif opcion == "5":
            product_dao.show()
            try:
                id_producto = int(input("🔸 Ingresa el ID del producto a consultar su inventario mínimo: "))
            except ValueError:
                print("❌ ID inválido.")
                continue
            resultado = inventario_minimo_dao.calcular_minimo(
                id_producto, product_dao.products, distribution_dao.distribuciones
            )
            print(resultado)

        elif opcion == "6":
            product_dao.guardar_inventario()
            distribution_dao.guardar_distribuciones()
            print("📤 Saliendo del programa...")
            break

        else:
            print("❌ Opción no válida.")