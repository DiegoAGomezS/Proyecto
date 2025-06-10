inventario = {}

def agregar_productos():
    print("\n---- AGREGAR PRODUCTOS ----")
    while True:
        producto = input("Nombre del producto (o escribe 'fin' para terminar): ")
        if producto.lower() == "fin":
            break
        try:
            cantidad = int(input(f"Cantidad de '{producto}': "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            inventario[producto] = inventario.get(producto, 0) + cantidad
        except ValueError:
            print("Por favor, ingresa un número válido para la cantidad.")
    print("---------------------------\n")

def mostrar_inventario():
    print("\n----- INVENTARIO ACTUAL -----")
    if not inventario:
        print("No hay productos en el inventario.")
    else:
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad} unidades")
    print("-----------------------------\n")

def distribuir_producto():
    print("\n----- DISTRIBUIR PRODUCTO -----")
    nombre = input("Nombre del producto a distribuir: ")
    if nombre not in inventario:
        print("Ese producto no está en el inventario.")
        return

    try:
        cantidad = int(input("Cantidad a distribuir: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero.")
    elif inventario[nombre] < cantidad:
        print("No hay suficiente cantidad en el inventario.")
    else:
        inventario[nombre] -= cantidad
        destinatario = input("¿A quién se le asigna?: ")
        print(f"Se distribuyeron {cantidad} unidades de {nombre} a {destinatario}.")
    print("-------------------------------\n")

# Menú principal
def menu():
    while True:
        print("====== MENÚ ======")
        print("1. Agregar productos al inventario")
        print("2. Mostrar inventario")
        print("3. Distribuir producto")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            agregar_productos()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            distribuir_producto()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
