import tkinter as tk  # Importa el módulo tkinter para crear la GUI
from tkinter import messagebox, Listbox  # Importa messagebox para mostrar mensajes y Listbox para mostrar tareas


class TaskManagerApp:
    def __init__(self, root):
        self.root = root  # Asigna la ventana principal a la variable root
        self.root.title("Gestor de Tareas")  # Establece el título de la ventana
        self.root.geometry("400x400")  # Establece el tamaño de la ventana

        # Campo de entrada para nuevas tareas
        self.task_input = tk.Entry(root, width=40)  # Crea un campo de texto
        self.task_input.pack(pady=10)  # Agrega el campo a la ventana y añade un margen vertical

        # Botón para añadir una nueva tarea
        self.add_task_button = tk.Button(root, text="Añadir Tarea",
                                         command=self.add_task)  # Crea un botón que llama a add_task
        self.add_task_button.pack(pady=5)  # Agrega el botón a la ventana con un margen vertical

        # Lista de tareas (Listbox)
        self.task_list = Listbox(root, width=50, height=15)  # Crea un Listbox para mostrar las tareas
        self.task_list.pack(pady=10)  # Agrega el Listbox a la ventana

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea",
                                            command=self.delete_task)  # Crea un botón para eliminar tareas
        self.delete_task_button.pack(pady=5)  # Agrega el botón a la ventana

        # Botón para marcar tarea como completada
        self.complete_task_button = tk.Button(root, text="Marcar como Completada",
                                              command=self.complete_task)  # Crea un botón para completar tareas
        self.complete_task_button.pack(pady=5)  # Agrega el botón a la ventana

        # Eventos
        self.task_input.bind('<Return>', lambda event: self.add_task())  # Permite añadir tarea al presionar Enter
        self.task_list.bind('<Double-1>',
                            lambda event: self.complete_task())  # Permite marcar como completada al hacer doble clic

    def add_task(self):
        # Obtener la tarea del campo de entrada
        task = self.task_input.get()  # Obtiene el texto del campo de entrada
        if task:  # Si hay texto en el campo
            # Insertar la tarea en la lista
            self.task_list.insert(tk.END, task)  # Agrega la tarea al final de la lista
            self.task_input.delete(0, tk.END)  # Limpia el campo de entrada
        else:  # Si el campo está vacío
            # Advertencia si el campo está vacío
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")  # Muestra un mensaje de advertencia

    def complete_task(self):
        # Marcar tarea seleccionada como completada
        try:
            selected_index = self.task_list.curselection()[0]  # Obtiene el índice de la tarea seleccionada
            task = self.task_list.get(selected_index)  # Obtiene el texto de la tarea seleccionada
            self.task_list.delete(selected_index)  # Elimina la tarea seleccionada
            self.task_list.insert(tk.END, f"[✔️] {task}")  # Añade símbolo de completada a la tarea
        except IndexError:  # Si no hay ninguna tarea seleccionada
            messagebox.showwarning("Advertencia",
                                   "Por favor, selecciona una tarea.")  # Muestra un mensaje de advertencia

    def delete_task(self):
        # Eliminar la tarea seleccionada
        try:
            selected_index = self.task_list.curselection()[0]  # Obtiene el índice de la tarea seleccionada
            self.task_list.delete(selected_index)  # Elimina la tarea seleccionada
        except IndexError:  # Si no hay ninguna tarea seleccionada
            messagebox.showwarning("Advertencia",
                                   "Por favor, selecciona una tarea para eliminar.")
            # Muestra un mensaje de advertencia


# Punto de entrada de la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = TaskManagerApp(root)  # Inicia la aplicación
    root.mainloop()  # Ejecuta el bucle principal de la aplicación


