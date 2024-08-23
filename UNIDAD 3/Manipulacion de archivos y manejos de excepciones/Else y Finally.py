try:
    # Intentar abrir un archivo
    archivo = open('archivo_inexistente.txt', 'r')
except FileNotFoundError:
    print("Error: El archivo no fue encontrado.")
else:
    # Se ejecuta si no ocurre una excepción
    print("El archivo fue abierto exitosamente.")
    archivo.close()  # Cierra el archivo si se abrió correctamente
finally:
    # Se ejecuta siempre, haya o no una excepción
    print("Finalizando operación de archivo.")
