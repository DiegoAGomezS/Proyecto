import pandas as pd
import os

def cargar_distribuciones_excel():
    global distribuciones
    if os.path.exists("distribuciones.xlsx"):
        df = pd.read_excel("distribuciones.xlsx")
        distribuciones = df.to_dict(orient='records')
        return "✔️ Distribuciones cargadas desde distribuciones.xlsx."
    else:
        return "📂 No se encontró distribuciones.xlsx. Se creará una nueva al salir."

def guardar_distribuciones_excel():
    df = pd.DataFrame(distribuciones)
    df.to_excel("distribuciones.xlsx", index=False)
    return "💾 Distribuciones guardadas en distribuciones.xlsx."