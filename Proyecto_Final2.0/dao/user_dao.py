import os

class UserDao:
    def __init__(self, archivo_usuarios="usuarios.txt"):
        self.archivo = archivo_usuarios

    def agregar_usuario(self, usuario, clave):
        with open(self.archivo, "a") as archivo:
            archivo.write(f"{usuario},{clave}\n")

    def cargar_usuarios(self):
        usuarios = {}
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as archivo:
                for linea in archivo:
                    usuario, clave = linea.strip().split(",")
                    usuarios[usuario] = clave
        return usuarios