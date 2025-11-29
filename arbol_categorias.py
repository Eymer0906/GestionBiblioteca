class NodoCategoria:
    """Nodo del árbol N-ario de categorías."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []
        self.libros_isbn = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def agregar_libro(self, isbn):
        if isbn not in self.libros_isbn:
            self.libros_isbn.append(isbn)

    def __str__(self, nivel=0):
        indent = "  " * nivel
        resultado = f"{indent}- {self.nombre}\n"
        for isbn in self.libros_isbn:
            resultado += f"{indent}  * [Libro ISBN: {isbn}]\n"
        for hijo in self.hijos:
            resultado += hijo.__str__(nivel + 1)
        return resultado


class ArbolCategorias:
    """Gestiona el árbol completo de categorías."""
    def __init__(self):
        self.raiz = NodoCategoria("Todas las Categorías")

    def buscar_nodo(self, nombre_categoria, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
        if nodo_actual.nombre == nombre_categoria:
            return nodo_actual
        for hijo in nodo_actual.hijos:
            encontrado = self.buscar_nodo(nombre_categoria, hijo)
            if encontrado:
                return encontrado
        return None

    def agregar_categoria(self, nombre_nueva, nombre_padre="Todas las Categorías"):
        if not nombre_nueva.strip():
            print("\n[ÁRBOL] Error: El nombre de la categoría no puede estar vacío.")
            return
        nodo_padre = self.buscar_nodo(nombre_padre)
        if nodo_padre:
            if not self.buscar_nodo(nombre_nueva):
                nodo_padre.agregar_hijo(NodoCategoria(nombre_nueva))
                print(f"\n[ÁRBOL] Categoría '{nombre_nueva}' agregada bajo '{nombre_padre}'.")
            else:
                print(f"\n[ÁRBOL] Error: La categoría '{nombre_nueva}' ya existe.")
        else:
            print(f"\n[ÁRBOL] Error: No se encontró la categoría padre '{nombre_padre}'.")

    def agregar_libro_a_categoria(self, isbn, nombre_categoria):
        nodo = self.buscar_nodo(nombre_categoria)
        if nodo:
            nodo.agregar_libro(isbn)
            print(f"[ÁRBOL] Libro (ISBN: {isbn}) agregado a la categoría '{nombre_categoria}'.")
        else:
            print(f"\n[ÁRBOL] Error: No se encontró la categoría '{nombre_categoria}'.")

    def mostrar_arbol(self):
        print("\n" + "="*40)
        print("     Jerarquía de Categorías (ÁRBOL)")
        print("="*40)
        print(self.raiz)
        print("="*40)
