class Usuario:
    """Representa un usuario de la biblioteca."""
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []

    def __str__(self):
        libros = ", ".join(self.libros_prestados) if self.libros_prestados else "Ninguno"
        return f"ID: {self.id_usuario} | Nombre: {self.nombre} | Libros Prestados: {libros}"
