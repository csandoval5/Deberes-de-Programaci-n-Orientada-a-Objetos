# Se inicia importando la biblioteca tkinter y le damos un alias para escribir el nombre más corto
import tkinter as tk
from tkinter import messagebox

class MiAplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi primer trabajo con Tkinter")  # Nombre de la ventana
        self.root.geometry("400x300")  # Tamaño de la ventana

        # Etiqueta
        self.label = tk.Label(root, text="Bienvenido a mi aplicación")
        self.label.pack()

        # Campo de texto para ingresar elementos a la lista
        self.text_entry = tk.Entry(root)
        self.text_entry.pack()

        # Botón para agregar elementos a la lista
        self.add_button = tk.Button(root, text="Agregar a la lista", command=self.agregar_a_lista)
        self.add_button.pack()

        # Lista para mostrar datos
        self.lista = tk.Listbox(root)
        self.lista.pack()

    def agregar_a_lista(self):
        elemento = self.text_entry.get()
        if elemento:
            self.lista.insert(tk.END, elemento)
            self.text_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa un elemento válido.")

# Crear la ventana principal
root = tk.Tk()
app = MiAplicacion(root)
root.mainloop()
