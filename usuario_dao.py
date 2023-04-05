from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logging_config import log

class UsuarioDAO:

    # CLASS VARIABLES - private and constant
    _SELECCIONAR = "SELECT * FROM usuario" #String
    _INSERTAR = "INSERT INTO usuario(username, password) VALUES(%s, %s)"  # String
    _ACTUALIZAR = "UPDATE usuario SET username= %s, password= %s WHERE id_usuario= %s"  # String
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario= %s"  # String

    # CLASS METHODS
    @classmethod
    def seleccionar(cls): #Return a list of objects type Usuario
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall() #List of tuples
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1],registro[2]) #id, username, password
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario): #Return number of registers affected
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"INSERTADO: {usuario}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario): #Return number of registers affected
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"ACTUALIZADO: {usuario}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario): #Return number of registers affected
        with CursorDelPool() as cursor:
            valor = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valor)
            log.debug(f"ELIMINAR: {usuario}")
            return cursor.rowcount


#Test code
if (__name__ == "__main__"):

    # usuario1 = Usuario(username="prueba1", password="0000")
    # registros = UsuarioDAO.insertar(usuario1)
    # print(f"Registros insertados: {registros}")

    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        print(usuario)