import tkinter as tk

# Función para añadir un nuevo estudiante
def añadir_estudiante():
    estudiante = entrada_estudiante.get()  # Obtener el nombre del estudiante de la entrada
    if estudiante != "":  # Asegurarse de que no esté vacío
        lista_estudiantes.insert(tk.END, estudiante)  # Insertar estudiante en la lista
        entrada_estudiante.delete(0, tk.END)  # Limpiar el campo de entrada

# Función para eliminar un estudiante seleccionado
def eliminar_estudiante():
    try:
        indice_estudiante_seleccionado = lista_estudiantes.curselection()[0]  # Obtener índice del estudiante seleccionado
        lista_estudiantes.delete(indice_estudiante_seleccionado)  # Eliminarlo de la lista
    except IndexError:
        pass  # Si no hay selección, no hacer nada

# Función para editar un estudiante seleccionado
def editar_estudiante():
    try:
        indice_estudiante_seleccionado = lista_estudiantes.curselection()[0]  # Obtener índice del estudiante seleccionado
        nuevo_nombre = entrada_estudiante.get()  # Obtener el nuevo nombre del estudiante
        if nuevo_nombre != "":  # Si el nuevo nombre no está vacío
            lista_estudiantes.delete(indice_estudiante_seleccionado)  # Eliminar el nombre antiguo
            lista_estudiantes.insert(indice_estudiante_seleccionado, nuevo_nombre)  # Insertar el nuevo nombre
            entrada_estudiante.delete(0, tk.END)  # Limpiar el campo de entrada
    except IndexError:
        pass  # Si no hay selección, no hacer nada

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Estudiantes")

# Crear los widgets (elementos de la interfaz)
entrada_estudiante = tk.Entry(ventana, width=40)  # Campo de entrada para nuevos estudiantes
entrada_estudiante.pack(pady=10)

boton_añadir_estudiante = tk.Button(ventana, text="Añadir Estudiante", command=añadir_estudiante)  # Botón para añadir estudiante
boton_añadir_estudiante.pack(pady=5)

lista_estudiantes = tk.Listbox(ventana, height=10, width=50)  # Lista donde se mostrarán los estudiantes
lista_estudiantes.pack(pady=10)

boton_editar_estudiante = tk.Button(ventana, text="Editar Estudiante", command=editar_estudiante)  # Botón para editar estudiante
boton_editar_estudiante.pack(pady=5)

boton_eliminar_estudiante = tk.Button(ventana, text="Eliminar Estudiante", command=eliminar_estudiante)  # Botón para eliminar estudiante
boton_eliminar_estudiante.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
