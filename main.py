# MENU APP USUARIO
from usuario_dao import UsuarioDAO
from usuario import Usuario
from logging_config import log

switch = True
while (switch):
    print("")
    print("""\nOPCIONES:
1. Listar usuarios
2. Agregar usuario
3. Modificar usuario
4. Eiminar usuario
5. Salir
    """)

    choice = input("Escribe tu opción: ")

    if (choice == "1"): #Seleccionar
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

    elif(choice == "2"): #Insertar
        username = input("Escriba el username: ")
        password = input("Escriba la contraseña: ")
        usuario = Usuario(username= username, password= password)
        registros = UsuarioDAO.insertar(usuario)
        log.info(f"Usuarios ingresados: {registros}")

    elif (choice == "3"): #Actualizar
        id_usuario = input("Escriba el ID del usuario que desea modificar: ")
        username = input("Escriba el nuevo username: ")
        password = input("Escriba la nueva contraseña: ")
        usuario = Usuario(id_usuario, username, password)
        registros = UsuarioDAO.actualizar(usuario)
        log.info(f"Usuarios actualizados: {registros}")

    elif (choice == "4"): #Eliminar
        id_usuario = input("Escriba el ID del usuario que desea eliminar: ")
        usuario = Usuario(id_usuario=id_usuario)
        registros = UsuarioDAO.eliminar(usuario)
        log.info(f"Usuarios eliminados: {registros}")

    elif (choice == "5"):
        switch = False

    else:
        log.info("Opción inválida")