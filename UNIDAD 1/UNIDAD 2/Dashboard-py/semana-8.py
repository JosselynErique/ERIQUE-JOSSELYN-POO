import os

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo de script.

    Parámetros:
    ruta_script (str): La ruta relativa o absoluta del archivo de script.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    """
    Muestra un menú interactivo que permite al usuario elegir y mostrar scripts.
    """
    ruta_base = os.path.dirname(__file__)

    # Opciones del menú con rutas relativas
    opciones = {
        '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2-2. Otro Ejemplo.py',  # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
