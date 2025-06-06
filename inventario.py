import pandas as pd
import os
from datetime import datetime

# Lista donde se almacenará temporalmente el inventario
inventario = []

# Lista para almacenar las distribuciones
distribuciones = []

# ====== CARGAS DESDE EXCEL ======

def cargar_inventario_excel():
    global inventario
    if os.path.exists("inventario.xlsx"):
        df = pd.read_excel("inventario.xlsx")
        if "fecha_registro" not in df.columns:
            df["fecha_registro"] = None
        inventario = df.to_dict(orient='records')
        return "Inventario cargado desde inventario.xlsx."
    else:
        return "No se encontró inventario.xlsx. Se creará uno nuevo al salir."

def cargar_distribuciones_excel():
    global distribuciones
    if os.path.exists("distribuciones.xlsx"):
        df = pd.read_excel("distribuciones.xlsx")
        distribuciones = df.to_dict(orient='records')
        return "Distribuciones cargadas desde distribuciones.xlsx."
    else:
        return "No se encontró distribuciones.xlsx. Se creará una nueva al salir."

# ====== GUARDADO EN EXCEL ======

def guardar_inventario_excel():
    df = pd.DataFrame(inventario)
    df.to_excel("inventario.xlsx", index=False)
    return "Inventario guardado en inventario.xlsx."

def guardar_distribuciones_excel():
    df = pd.DataFrame(distribuciones)
    df.to_excel("distribuciones.xlsx", index=False)
    return "Distribuciones guardadas en distribuciones.xlsx."

# ====== UTILIDADES ======

def obtener_nuevo_id():
    ids_ocupados = [producto["id"] for producto in inventario]
    nuevo_id = 1
    while nuevo_id in ids_ocupados:
        nuevo_id += 1
    return nuevo_id

# ====== OPERACIONES ======

def registrar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: $"))
    cantidad = int(input(" Ingresa la cantidad disponible: "))

    producto = {
        "id": obtener_nuevo_id(),
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ultima_fecha_retiro": None
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' registrado con éxito.")

def mostrar_inventario():
    if not inventario:
        print("📦 Inventario vacío.")
    else:
        df = pd.DataFrame(inventario)
        print("\n📋 Inventario actual:")
        print(df.to_string(index=False))

def distribuir_producto():
    if not inventario:
        print("No hay productos para distribuir.")
        return
    mostrar_inventario()
    try:
        id_producto = int(input("🔸 Ingresa el ID del producto a distribuir: "))
        producto = next((item for item in inventario if item["id"] == id_producto), None)
        if not producto:
            print("ID no encontrado.")
            return

        cantidad = int(input(f"🔸 Cantidad a retirar de '{producto['nombre']}': "))
        if cantidad > producto["cantidad"]:
            print("No hay suficiente stock.")
            return

        confirmar = input(f"¿Confirmar retiro de {cantidad} unidades de '{producto['nombre']}'? (Y/N): ").upper()
        if confirmar == "Y":
            producto["cantidad"] -= cantidad
            fecha_retiro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            distribuciones.append({
                "id_producto": producto["id"],
                "nombre_producto": producto["nombre"],
                "cantidad": cantidad,
                "fecha_retiro": fecha_retiro
            })
            producto["ultima_fecha_retiro"] = fecha_retiro
            print(f"Se retiraron {cantidad} unidades de '{producto['nombre']}'.")
        else:
            print("Operación cancelada.")
    except ValueError:
        print("Valor inválido.")

def calcular_inventario_minimo(id_producto):
    if not inventario:
        print("No hay inventario disponible")
        return
    else:
        mostrar_inventario()
    producto = next((item for item in inventario if item["id"] == id_producto), None)
    if not producto:
        print("Producto no encontrado.")
        return

    if "fecha_registro" not in producto or not producto["fecha_registro"]:
        print(f"El producto '{producto['nombre']}' no tiene fecha de registro asignada.")
        return

    distribuciones_producto = [d for d in distribuciones if d["id_producto"] == id_producto]

    if not distribuciones_producto:
        print("No hay distribuciones registradas para este producto.")
        return

    if len(distribuciones_producto) == 1:
        fecha_inicial = datetime.strptime(producto["fecha_registro"], "%Y-%m-%d %H:%M:%S")
        fecha_retiro = datetime.strptime(distribuciones_producto[0]["fecha_retiro"], "%Y-%m-%d %H:%M:%S")
        dias_transcurridos = (fecha_retiro - fecha_inicial).days or 1
        cantidad_retirada = distribuciones_producto[0]["cantidad"]
    else:
        fecha_ultima = datetime.strptime(distribuciones_producto[-1]["fecha_retiro"], "%Y-%m-%d %H:%M:%S")
        fecha_penultima = datetime.strptime(distribuciones_producto[-2]["fecha_retiro"], "%Y-%m-%d %H:%M:%S")
        dias_transcurridos = (fecha_ultima - fecha_penultima).days or 1
        cantidad_retirada = distribuciones_producto[-1]["cantidad"]

    consumo_diario_promedio = cantidad_retirada / dias_transcurridos
    tiempo_reposicion = 5
    inventario_minimo = consumo_diario_promedio * tiempo_reposicion

    print(f"El inventario mínimo para el producto '{producto['nombre']}' es: {inventario_minimo:.2f} unidades.")

# ====== MENÚ PRINCIPAL ======

def menu():
    while True:
        print("\n====== MENÚ DE INVENTARIO ======")
        print("\033[32m1. Registrar producto\033[0m")               # Verde oscuro
        print("\033[34m2. Mostrar inventario\033[0m")              # Azul marino
        print("\033[33m3. Distribuir producto\033[0m")             # Amarillo
        print("\033[37m4. Calcular inventario mínimo\033[0m")      # Blanco
        print("\033[31m5. Salir y guardar inventario y distribuciones\033[0m")  # Rojo
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            distribuir_producto()
        elif opcion == "4":
            try:
                id_producto = int(input("Ingresa el ID del producto para calcular el inventario mínimo: "))
                calcular_inventario_minimo(id_producto)
            except ValueError:
                print("Valor inválido.")
        elif opcion == "5":
            guardar_inventario_excel()
            guardar_distribuciones_excel()
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

# ====== BLOQUE PRINCIPAL ======

if __name__ == "__main__":
    cargar_inventario_excel()
    cargar_distribuciones_excel()
    menu()