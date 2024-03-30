import tkinter as tk


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas de Mauricio Torres")

        # Lista de tareas
        self.tasks = []

        # Frame principal
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Lista de tareas
        self.task_list = tk.Listbox(self.frame, width=50)
        self.task_list.grid(row=0, columnspan=2, padx=5, pady=5)

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(self.frame, width=40)
        self.entry.grid(row=1, column=0, padx=5, pady=5)

        # Botones para añadir, marcar, desmarcar y eliminar tareas
        self.add_button = tk.Button(self.frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=1, column=1, padx=5, pady=5)
        self.complete_button = tk.Button(self.frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)
        self.uncomplete_button = tk.Button(self.frame, text="Desmarcar Tarea", command=self.uncomplete_task)
        self.uncomplete_button.grid(row=2, column=1, padx=5, pady=5)
        self.delete_button = tk.Button(self.frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Contenedor para los botones y la etiqueta
        self.bottom_frame = tk.Frame(root)
        self.bottom_frame.pack(side=tk.BOTTOM)

        # Leyenda final
        self.label = tk.Label(self.bottom_frame, text="Universidad Estatal Amazonica")
        self.label.pack()

        # Manejo de eventos
        self.entry.bind("<Return>", lambda event: self.add_task())
        self.task_list.bind("<Double-Button-1>", lambda event: self.complete_task())

        # Atajos de teclado
        self.root.bind("c", lambda event: self.complete_task())
        self.root.bind("d", lambda event: self.delete_task())
        self.root.bind("u", lambda event: self.uncomplete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.entry.delete(0, tk.END)

    def complete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.task_list.get(index)
            task = "✓ " + task if task[0] != "✓" else task[2:]
            self.tasks[index] = task
            self.update_task_list()

    def uncomplete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.task_list.get(index)
            task = task[2:] if task[0] == "✓" else task
            self.tasks[index] = task
            self.update_task_list()

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)
            if task[0] == "✓":
                self.task_list.itemconfig(tk.END, {'bg': 'light blue'})


def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
