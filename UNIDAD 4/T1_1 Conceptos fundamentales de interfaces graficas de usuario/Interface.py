import tkinter as tk
from tkinter import messagebox

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Información")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=5)

        # Campo de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Botón Agregar
        self.add_button = tk.Button(root, text="Agregar", command=self.agregar)
        self.add_button.pack(pady=5)

        # Botón Limpiar
        self.clear_button = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.clear_button.pack(pady=5)

        # Lista
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=5)

    def agregar(self):
        info = self.entry.get()
        if info:
            self.listbox.insert(tk.END, info)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

    def limpiar(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            self.listbox.delete(seleccion)
        else:
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
