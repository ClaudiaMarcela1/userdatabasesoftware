from conexion import Conexion
from logging_config import log

class CursorDelPool:

    # Initialized method
    def __init__(self):
        self._conn = None #String
        self._cursor = None #String

    # METHODS GET
    @property
    def conn(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    # METHODS SET
    @conn.setter
    def conn(self, conn):
        self._conn = conn

    @cursor.setter
    def cursor(self, cursor):
        self._cursor = cursor

    # METHODS
    def __enter__(self): #Return cursor
        # Get a cursor of the connection object
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        log.debug("¡Got a cursor!")
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Evaluate if exist an exception for rollback. Otherwise, commit. Close cursor
        if (exc_val):
            self._conn.rollback()
            log.debug(f"ROLLBACK. Ocurred an exception: {exc_type}, {exc_val}")
        else:
            self._conn.commit()
            log.debug("¡COMMIT. Transaction got!")
        self._cursor.close()
        Conexion.liberarConexion(self._conn)


# Test code
if (__name__ == "__main__"):
    with CursorDelPool() as cursor:
        cursor.execute("SELECT * FROM usuario")
        registers = cursor.fetchall()
        log.debug(registers)