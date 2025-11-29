from libro import Libro
from usuario import Usuario
from arbol_categorias import ArbolCategorias

class GestionBiblioteca:
    """Gestiona libros, usuarios y categorías."""
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.arbol_categorias = ArbolCategorias()
        self.contador_usuarios = 1

    def agregar_libro(self, titulo, autor, isbn, categoria):
        if isbn in self.libros:
            print("\n[ERROR] Ya existe un libro con ese ISBN.")
        else:
            libro = Libro(titulo, autor, isbn, categoria)
            self.libros[isbn] = libro
            print(f"\n[OK] Libro '{titulo}' agregado con éxito.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"\n[OK] Libro con ISBN {isbn} eliminado.")
        else:
            print("\n[ERROR] No existe un libro con ese ISBN.")

    def mostrar_libros(self):
        print("\n--- Lista de Libros ---")
        if not self.libros:
            print("No hay libros registrados.")
        else:
            for libro in self.libros.values():
                print(libro)

    def registrar_usuario(self, nombre):
        nuevo = Usuario(self.contador_usuarios, nombre)
        self.usuarios[self.contador_usuarios] = nuevo
        print(f"\n[OK] Usuario '{nombre}' registrado con ID {self.contador_usuarios}.")
        self.contador_usuarios += 1

    def mostrar_usuarios(self):
        print("\n--- Lista de Usuarios ---")
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            for usuario in self.usuarios.values():
                print(usuario)

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("\n[ERROR] Usuario no encontrado.")
            return
        if isbn not in self.libros:
            print("\n[ERROR] Libro no encontrado.")
            return
        libro = self.libros[isbn]
        if not libro.disponible:
            print("\n[ERROR] El libro ya está prestado.")
            return
        libro.disponible = False
        self.usuarios[id_usuario].libros_prestados.append(isbn)
        print(f"\n[OK] Libro '{libro.titulo}' prestado a {self.usuarios[id_usuario].nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("\n[ERROR] Usuario no encontrado.")
            return
        if isbn not in self.libros:
            print("\n[ERROR] Libro no encontrado.")
            return
        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        if isbn not in usuario.libros_prestados:
            print("\n[ERROR] Ese usuario no tenía prestado este libro.")
            return
        usuario.libros_prestados.remove(isbn)
        libro.disponible = True
        print(f"\n[OK] Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
