class Usuario:

    # Initialized method
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario #Int
        self._username = username #String
        self._password = password #String

    # METHODS GET
    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    # METHODS SET
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @username.setter
    def username(self, username):
        self._username = username

    @password.setter
    def password(self, password):
        self._password = password

    # METHOD STR
    def __str__(self):
        return f"Usuario [Id:{self._id_usuario}, Username:{self._username}, Password:{self._password}]"


# Test code
if (__name__ == "__main__"):
    usuario1 = Usuario(1, "akeys", "asdf")
    print(usuario1)