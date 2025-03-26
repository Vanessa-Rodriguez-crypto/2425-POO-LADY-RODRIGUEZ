import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Marco principal
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5)
        self.task_entry.bind("<Return>", self.add_task)  # Vincula la tecla Enter al método add_task

        # Botón para añadir tarea
        self.add_button = tk.Button(self.frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.grid(row=1, column=0, columnspan=2, pady=10)
        self.listbox.bind("<Double-Button-1>", self.toggle_task)  # Doble clic para marcar como completada

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, columnspan=2, pady=5)

    def add_task(self, event=None):
        """Añade una nueva tarea a la lista."""
        task = self.task_entry.get()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def toggle_task(self, event):
        """Marca una tarea como completada o no completada."""
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index)
            if task.startswith("[Completada] "):
                task = task.replace("[Completada] ", "")
            else:
                task = f"[Completada] {task}"
            self.listbox.delete(index)
            self.listbox.insert(index, task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
