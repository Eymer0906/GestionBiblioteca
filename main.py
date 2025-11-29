import sys
from gestion_biblioteca import GestionBiblioteca

def main():
    biblioteca = GestionBiblioteca()

    while True:
        print("\n" + "="*40)
        print("     Sistema de Gestión de Biblioteca")
        print("="*40)
        print("--- Gestión de Libros ---")
        print("1. Agregar Libro")
        print("2. Eliminar Libro")
        print("3. Mostrar Libros")
        print("--- Gestión de Usuarios ---")
        print("4. Registrar Usuario")
        print("5. Mostrar Usuarios")
        print("--- Operaciones ---")
        print("6. Prestar Libro")
        print("7. Devolver Libro")
        print("--- Categorías ---")
        print("8. Agregar Categoría")
        print("9. Asignar Libro a Categoría")
        print("10. Mostrar Árbol de Categorías")
        print("11. Salir")
        print("-"*40)

        opcion = input("Elige una opción (1-11): ")

        match opcion:
            case '1':
                titulo = input("Título: ")
                autor = input("Autor: ")
                isbn = input("ISBN: ")
                categoria = input("Categoría (default: General): ") or "General"
                biblioteca.agregar_libro(titulo, autor, isbn, categoria)
            case '2':
                isbn = input("ISBN del libro a eliminar: ")
                biblioteca.eliminar_libro(isbn)
            case '3':
                biblioteca.mostrar_libros()
            case '4':
                nombre = input("Nombre del nuevo usuario: ")
                biblioteca.registrar_usuario(nombre)
            case '5':
                biblioteca.mostrar_usuarios()
            case '6':
                try:
                    id_usuario = int(input("ID del Usuario: "))
                    isbn = input("ISBN del libro a prestar: ")
                    biblioteca.prestar_libro(id_usuario, isbn)
                except ValueError:
                    print("\n[ERROR] El ID del usuario debe ser numérico.")
            case '7':
                try:
                    id_usuario = int(input("ID del Usuario: "))
                    isbn = input("ISBN del libro a devolver: ")
                    biblioteca.devolver_libro(id_usuario, isbn)
                except ValueError:
                    print("\n[ERROR] El ID del usuario debe ser numérico.")
            case '8':
                nombre_nueva = input("Nombre de la nueva categoría: ")
                nombre_padre = input("Nombre de la categoría padre (default: Todas las Categorías): ") or "Todas las Categorías"
                biblioteca.arbol_categorias.agregar_categoria(nombre_nueva, nombre_padre)
            case '9':
                isbn = input("ISBN del libro: ")
                categoria = input("Nombre de la categoría: ")
                if isbn in biblioteca.libros:
                    biblioteca.arbol_categorias.agregar_libro_a_categoria(isbn, categoria)
                else:
                    print(f"\n[ERROR] No existe un libro con ISBN {isbn}.")
            case '10':
                biblioteca.arbol_categorias.mostrar_arbol()
            case '11':
                print("\nGracias por usar el sistema. ¡Hasta pronto!")
                sys.exit()
            case _:
                print("\n[ERROR] Opción no válida. Elige entre 1 y 11.")

if __name__ == "__main__":
    main()
