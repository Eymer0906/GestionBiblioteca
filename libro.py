class Libro:
    """Representa un libro en la biblioteca."""
    def __init__(self, titulo, autor, isbn, categoria="General"):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.categoria = categoria
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({self.categoria}) -> {estado}"
