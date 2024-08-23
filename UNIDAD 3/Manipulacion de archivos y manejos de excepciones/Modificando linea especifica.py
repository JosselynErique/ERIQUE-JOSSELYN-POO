# Función para modificar una línea específica en un archivo
def modificar_linea_archivo(nombre_archivo, numero_linea, nuevo_contenido):
    # Leer el contenido del archivo
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    # Modificar la línea especificada
    lineas[numero_linea - 1] = nuevo_contenido + "\n"

    # Reescribir el archivo con la línea modificada
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(lineas)

# Crear un archivo de ejemplo con contenido inicial
nombre_archivo = 'ejemplo.txt'
with open(nombre_archivo, 'w') as archivo:
    archivo.write("Línea 1\n")
    archivo.write("Línea 2\n")
    archivo.write("Línea 3\n")

# Leer y mostrar el contenido original
print("Contenido Original:")
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())

# Modificar una línea específica
modificar_linea_archivo(nombre_archivo, 2, "Línea 2 modificada")

# Leer y mostrar el contenido modificado
print("Contenido Modificado:")
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())
