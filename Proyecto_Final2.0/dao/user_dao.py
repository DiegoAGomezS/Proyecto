import os  # Importa os para verificar si el archivo existe

# Clase para manejar operaciones relacionadas con los usuarios
class UserDao:
    def __init__(self, archivo_usuarios="usuarios.txt"):
        self.archivo = archivo_usuarios  # Nombre del archivo donde se guardan los usuarios

    def agregar_usuario(self, usuario, clave):
        # Valida que usuario y clave no estén vacíos
        if not usuario or not clave:
            print("El usuario y la contraseña no pueden estar vacíos.")
            return

        usuarios = self.cargar_usuarios() # Carga los usuarios ya existentes
        if usuario in usuarios:
            print(f"El usuario '{usuario}' ya existe.") # Si el usuario ya está registrado, muestra un mensaje
        else:  # Si no existe, lo agrega al archivo en una nueva línea
            with open(self.archivo, "a") as archivo:
                archivo.write(f"{usuario},{clave}\n")
            print(f"Usuario '{usuario}' agregado correctamente.")

    def cargar_usuarios(self):
        usuarios = {}  # Diccionario para almacenar usuarios cargados
        if os.path.exists(self.archivo):  # Verifica si el archivo existe
            with open(self.archivo, "r") as archivo:
                for linea in archivo:
                    usuario, clave = linea.strip().split(",")  # Separa usuario y clave
                    usuarios[usuario] = clave
        return usuarios  # Devuelve el diccionario de usuarios