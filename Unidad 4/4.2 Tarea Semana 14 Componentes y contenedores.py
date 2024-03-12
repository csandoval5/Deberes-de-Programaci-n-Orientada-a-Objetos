import tkinter as tk
from tkinter import ttk


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        self.eventos = []

        # Crear el Treeview
        self.tree = ttk.Treeview(self.root, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Hora', text='Hora')
        self.tree.heading('Descripción', text='Descripción')
        self.tree.pack(padx=10, pady=10)

        # Campos de entrada
        self.fecha_entry = ttk.Entry(self.root)
        self.fecha_entry.pack(padx=10, pady=5)
        self.fecha_entry.insert(0, 'Fecha (DD/MM/AAAA)')

        self.hora_entry = ttk.Entry(self.root)
        self.hora_entry.pack(padx=10, pady=5)
        self.hora_entry.insert(0, 'Hora (HH:MM)')

        self.descripcion_entry = ttk.Entry(self.root)
        self.descripcion_entry.pack(padx=10, pady=5)
        self.descripcion_entry.insert(0, 'Descripción')

        # Botones
        self.agregar_button = ttk.Button(self.root, text='Agregar Evento', command=self.agregar_evento)
        self.agregar_button.pack(padx=10, pady=5)

        self.eliminar_button = ttk.Button(self.root, text='Eliminar Evento Seleccionado', command=self.eliminar_evento)
        self.eliminar_button.pack(padx=10, pady=5)

        self.salir_button = ttk.Button(self.root, text='Salir', command=self.root.quit)
        self.salir_button.pack(padx=10, pady=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        self.eventos.append((fecha, hora, descripcion))

        self.actualizar_treeview()

    def eliminar_evento(self):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection)
            evento = item['values']
            if evento in self.eventos:
                self.eventos.remove(evento)
                self.actualizar_treeview()
            else:
                print("El evento seleccionado no está en la lista.")
        else:
            print("Por favor, selecciona un evento para eliminar.")

    def actualizar_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for evento in self.eventos:
            self.tree.insert('', 'end', values=evento)


def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()