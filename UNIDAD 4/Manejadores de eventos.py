import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        add_button.pack(pady=5)

        # Botón para marcar como completada
        complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        complete_button.pack(pady=5)

        # Botón para eliminar tarea
        delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        delete_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Scrollbar para la lista
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())  # Tecla "Enter"
        self.root.bind("<c>", lambda event: self.complete_task())  # Tecla "C"
        self.root.bind("<Delete>", lambda event: self.delete_task())  # Tecla "Delete"
        self.root.bind("<Escape>", lambda event: self.root.quit())  # Tecla "Escape"

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, END)  # Limpiar campo de entrada

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_task_index] + " (Completada)"
            self.tasks[selected_task_index] = completed_task
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, END)  # Limpiar la lista
        for task in self.tasks:
            self.task_listbox.insert(END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
