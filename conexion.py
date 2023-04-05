from logging_config import log
from psycopg2 import pool
import sys

class Conexion:

    # CLASS VARIABLES - private and constant
    _DATABASE = "test_db" #String
    _USERNAME = "postgres" #String
    _PASSWORD = "admin" #String
    _DB_PORT = "5432" #String
    _HOST = "localhost" #String
    _MIN_CON = 1 #int
    _MAX_CON = 5 #int
    _pool = None #Pool

    # CLASS METHODS
    @classmethod
    def obtenerPool(cls): #Return pool
        # Evaluate if doesn't exist a pool for creating it. Otherwise, return it
        if (cls._pool == None):
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON, database= cls._DATABASE, user= cls._USERNAME, password= cls._PASSWORD, port= cls._DB_PORT, host= cls._HOST)
                log.debug("¡Pool created!")
                return cls._pool
            except Exception as e:
                log.debug(f"An error ocurred trying to get a connection pool: {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls): #Return connection object
        # Get a connection from the pool
        conexion = cls.obtenerPool().getconn()
        log.debug("¡Got a connection!")
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug("¡Connection released!")

    @classmethod
    def cerrarPool(cls):
        cls.obtenerPool().closeall()
        log.debug("¡Pool closed!")


# Test code
if (__name__ == "__main__"):
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)