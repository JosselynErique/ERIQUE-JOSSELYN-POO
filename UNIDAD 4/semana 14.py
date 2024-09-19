import tkinter as tk
from tkinter import ttk, messagebox

class SimpleStudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Estudiantes")

        # Frame para la lista de estudiantes
        self.tree_frame = tk.Frame(root)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.tree_frame, columns=("Nombre", "Edad", "Curso"), show='headings')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Curso", text="Curso")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para entrada de datos
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(padx=10, pady=10, fill=tk.X)

        tk.Label(self.input_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Edad:").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.input_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Curso:").grid(row=2, column=0, padx=5, pady=5)
        self.course_entry = tk.Entry(self.input_frame)
        self.course_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para botones
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(padx=10, pady=10, fill=tk.X)

        self.add_button = tk.Button(self.buttons_frame, text="Agregar Estudiante", command=self.add_student)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.buttons_frame, text="Eliminar Estudiante Seleccionado", command=self.delete_student)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(self.buttons_frame, text="Salir", command=root.quit)
        self.exit_button.pack(side=tk.LEFT, padx=5)

    def add_student(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        course = self.course_entry.get()
        if name and age and course:
            self.tree.insert("", "end", values=(name, age, course))
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.course_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def delete_student(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un estudiante para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleStudentApp(root)
    root.mainloop()
