# Creación de un conjunto
animales = {"gato", "perro", "conejo"}

# Agregar un elemento
animales.add("pájaro")

# Intento de eliminar un elemento
# Usa discard para evitar errores si el elemento no existe en el conjunto
animales.discard("perro")

# Crear otro conjunto para operaciones
mascotas = {"hamster", "pájaro", "conejo"}

# Operaciones de conjunto
union = animales | mascotas  # Unión de conjuntos
interseccion = animales & mascotas  # Intersección de conjuntos
diferencia = animales - mascotas  # Diferencia de conjuntos

# Imprimir los resultados
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)
