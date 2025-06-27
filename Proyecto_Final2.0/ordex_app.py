import main.menu as m
from dao.user_dao import UserDao
import pwinput

user_dao = UserDao() # Crear instancia de UserDao para manejar usuarios

def inicio_sesion():
    print("====== INICIO DE SESIÓN ======")
    usuarios = user_dao.cargar_usuarios()  # Cargar los usuarios desde el archivo usuarios.txt

    intentos = 3 # Número máximo de intentos permitidos

    while intentos > 0:
        usuario = input("Usuario: ").strip() # Pedir usuario y eliminar espacios al inicio y final
        clave_ingresada = pwinput.pwinput(prompt="Contraseña: ", mask="*").strip() # Pedir contraseña oculta y limpiar espacios

        # Pedir contraseña oculta y limpiar espacios
        if usuario in usuarios and usuarios[usuario] == clave_ingresada:
            print("Acceso permitido.")
            return True  # Inicio de sesión exitoso
        else:
            intentos -= 1 # Restar un intento
            print(f"Usuario o contraseña incorrectos. Te quedan {intentos} intento(s).")

    # Si se acaban los intentos, mostrar mensaje y finalizar
    print("Has excedido el número de intentos. El programa se cerrará.")
    return False

if __name__ == "__main__":
    if inicio_sesion(): # Ejecutar inicio de sesión y si es exitoso
        m.menu() # Llamar al menú principal