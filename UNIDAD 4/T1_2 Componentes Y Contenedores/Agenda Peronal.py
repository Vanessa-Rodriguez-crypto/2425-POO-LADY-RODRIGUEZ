import tkinter as tk
from tkinter import ttk, messagebox

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.centrar_ventana(500, 400)

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(pady=10, fill=tk.BOTH, expand=True)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para entrada de datos
        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        ttk.Label(self.frame_entrada, text="Fecha (DD/MM/AAAA):").grid(row=0, column=0)
        self.fecha_entry = ttk.Entry(self.frame_entrada, width=12)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = ttk.Entry(self.frame_entrada, width=10)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = ttk.Entry(self.frame_entrada, width=30)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para botones
        self.frame_botones = ttk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        ttk.Button(self.frame_botones, text="Salir", command=self.root.quit).grid(row=0, column=2, padx=5)

    def centrar_ventana(self, ancho, alto):
        pantalla_ancho = self.root.winfo_screenwidth()
        pantalla_alto = self.root.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
            self.fecha_entry.delete(0, tk.END)
            self.hora_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar completos.")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirmar = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar este evento?")
            if confirmar:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
