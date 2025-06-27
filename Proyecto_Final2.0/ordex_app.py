import main.menu as m
from dao.user_dao import UserDao
import pwinput

user_dao = UserDao()
user_dao.agregar_usuario("admin", "Admin123")

def inicio_sesion():
    print("====== INICIO DE SESIÓN ======")
    user_dao = UserDao()
    usuarios = user_dao.cargar_usuarios()

    intentos = 3  # intentos máximos permitidos

    while intentos > 0:
        usuario = input("Usuario: ")
        clave_ingresada = pwinput.pwinput(prompt="Contraseña: ", mask="°")

        if usuario in usuarios and usuarios[usuario] == clave_ingresada:
            print("Acceso permitido.")
            return True
        else:
            intentos -= 1
            print(f"Usuario o contraseña incorrectos. Te quedan {intentos} intento(s).")

        if intentos == 0:
            print("Has excedido el número de intentos. El programa se cerrará.")
            return False

if __name__ == "__main__":
    if inicio_sesion():
        m.menu()