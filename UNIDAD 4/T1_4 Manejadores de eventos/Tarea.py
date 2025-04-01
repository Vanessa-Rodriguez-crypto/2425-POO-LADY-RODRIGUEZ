import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    tarea = entrada.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede agregar una tarea vacía")

def marcar_completada(event=None):
    try:
        seleccion = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(seleccion)
        lista_tareas.delete(seleccion)
        lista_tareas.insert(seleccion, f"✔ {tarea}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

def eliminar_tarea(event=None):
    try:
        seleccion = lista_tareas.curselection()[0]
        lista_tareas.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

def cerrar_app(event=None):
    root.quit()

root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

entrada = tk.Entry(root, width=50)
entrada.pack(pady=10)
entrada.bind("<Return>", agregar_tarea)

btn_agregar = tk.Button(root, text="Agregar", command=agregar_tarea)
btn_agregar.pack()

lista_tareas = tk.Listbox(root, width=50, height=15)
lista_tareas.pack(pady=10)

btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack()

btn_eliminar = tk.Button(root, text="Eliminar", command=eliminar_tarea)
btn_eliminar.pack()

root.bind("c", marcar_completada)
root.bind("d", eliminar_tarea)
root.bind("<Delete>", eliminar_tarea)
root.bind("<Escape>", cerrar_app)

root.mainloop()
