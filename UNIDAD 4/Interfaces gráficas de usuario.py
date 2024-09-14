import tkinter as tk
from tkinter import messagebox

# Función para agregar texto a la lista
def agregar_dato():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)  # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa un dato.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Datos")

# Crear etiquetas, campos de texto, y botones
etiqueta = tk.Label(ventana, text="Ingresa un dato:")
etiqueta.pack(pady=5)

entrada_texto = tk.Entry(ventana)
entrada_texto.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Crear lista para mostrar los datos agregados
lista_datos = tk.Listbox(ventana)
lista_datos.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
