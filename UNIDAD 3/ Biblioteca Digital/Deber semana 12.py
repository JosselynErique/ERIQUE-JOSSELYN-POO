class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print("El libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado de la biblioteca.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("El ID de usuario no está registrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            usuario.prestar_libro(libro)
            del self.libros[isbn]
            print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.get(isbn, None)
            if libro:
                usuario.devolver_libro(libro)
                self.libros[isbn] = libro
                print(f"Libro '{libro.titulo}' devuelto por '{usuario.nombre}'.")
            else:
                print("El libro no está registrado en la biblioteca.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro_por_titulo(self, titulo):
        return [libro for libro in self.libros.values() if libro.titulo == titulo]

    def buscar_libro_por_autor(self, autor):
        return [libro for libro in self.libros.values() if libro.autor == autor]

    def buscar_libro_por_categoria(self, categoria):
        return [libro for libro in self.libros.values() if libro.categoria == categoria]

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")
            return []

    def __repr__(self):
        return f"Biblioteca(libros={self.libros}, usuarios={self.usuarios})"


# Crear instancia de la biblioteca
biblioteca = Biblioteca()

# Función para añadir libros
def añadir_libro_interactivo():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    categoria = input("Ingrese la categoría del libro: ")
    isbn = input("Ingrese el ISBN del libro: ")
    libro = Libro(titulo, autor, categoria, isbn)
    biblioteca.añadir_libro(libro)

# Función para registrar usuarios
def registrar_usuario_interactivo():
    nombre = input("Ingrese el nombre del usuario: ")
    id_usuario = input("Ingrese el ID del usuario: ")
    usuario = Usuario(nombre, id_usuario)
    biblioteca.registrar_usuario(usuario)

# Función principal para interactuar con el sistema
def main():
    while True:
        print("\n1. Añadir libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libro por título")
        print("6. Listar libros prestados")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            añadir_libro_interactivo()
        elif opcion == "2":
            registrar_usuario_interactivo()
        elif opcion == "3":
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)
        elif opcion == "4":
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)
        elif opcion == "5":
            criterio = input("Buscar por título, autor o categoría? ").strip().lower()
            valor = input(f"Ingrese el {criterio}: ")
            if criterio == "título":
                libros = biblioteca.buscar_libro_por_titulo(valor)
            elif criterio == "autor":
                libros = biblioteca.buscar_libro_por_autor(valor)
            elif criterio == "categoría":
                libros = biblioteca.buscar_libro_por_categoria(valor)
            else:
                libros = []
                print("Criterio de búsqueda no válido.")
            print(f"Libros encontrados: {libros}")
        elif opcion == "6":
            id_usuario = input("Ingrese el ID del usuario: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            print(f"Libros prestados por el usuario: {libros_prestados}")
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()



