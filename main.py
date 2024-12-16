"""App"""
from tkinter import messagebox, ttk, Label, Text, Tk, Button, Entry, StringVar, CENTER, Toplevel
from databasepg import Data


class App:

    def __init__(self, master):
        self.frame = master
        self.draw_entry()
        self.draw_buttons()
        self.draw_label()
        self.draw_list()

    def draw_label(self):
        """Dibuja los label de la ventana principal"""
        self.lbl_title = Label(self.frame, foreground="#56cfe1", font=(
            "Arial", 16, "bold"), background="#7400b8", text="Titulo")
        self.lbl_title.place(x=60, y=60)
        self.lbl_description = Label(self.frame, foreground="#56cfe1", font=(
            "Arial", 16, "bold"), background="#7400b8", text="Descripción")
        self.lbl_description.place(x=60, y=160)

    def draw_entry(self):
        """Dibuja las entradas de la ventana principal"""
        self.title = StringVar()
        self.description = StringVar()
        self.txt_title = Entry(self.frame, font=('Arial', 12), relief="flat", background="#E7E7E7",
                               textvariable=self.title)
        self.txt_title.place(x=60, y=110, height=25, width=230)
        self.txt_description = Text(
            self.frame,
            font=('Arial', 12),
            relief="flat",
            background="#E7E7E7",
            wrap="word",
            height=5,
            width=30,
        )
        self.txt_description.place(x=60, y=210, height=100, width=230)

    def draw_buttons(self):
        """
        Crea los botones de la ventana principal
        """
        self.btn_confirm = Button(self.frame, foreground="white", text="Guardar", borderwidth=2, relief="flat",
                                  cursor="hand1", overrelief="raise", background="#0051C8", command=lambda: self.confirm_process())
        self.btn_confirm.place(x=60, y=340, width=90)
        self.btn_cancel = Button(self.frame, text="Limpiar", foreground="white", borderwidth=2, relief="flat",
                                 cursor="hand1", overrelief="raise", background="#bcb8b1", command=lambda: self.clear_entry())
        self.btn_cancel.place(x=160, y=340, width=90)

    def draw_list(self):
        """
        Crea la lista para mostrar las tareas
        """
        self.list_elemts = ttk.Treeview(
            self.frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="8")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#0051C8",
                        relief="flat", foreground="white")
        style.map("Treeview", background=[
                  ('selected', 'yellow')], foreground=[('selected', 'black')])

        self.list_elemts.bind("<Double 1>", self.get_row)

        self.list_elemts.heading(1, text="ID")
        self.list_elemts.heading(2, text="Tarea")
        self.list_elemts.heading(3, text="Descripción")
        self.list_elemts.heading(4, text="Fecha")
        self.list_elemts.heading(5, text="Estado")
        self.list_elemts.heading(6, text="Cambiar Estado")
        self.list_elemts.heading(7, text="Eliminar")

        self.list_elemts.column(1, width=30, anchor=CENTER)
        self.list_elemts.column(2, anchor=CENTER)
        self.list_elemts.column(3, anchor=CENTER)
        self.list_elemts.column(4, width=100, anchor=CENTER)
        self.list_elemts.column(5, width=60, anchor=CENTER)
        self.list_elemts.column(6, width=130, anchor=CENTER)
        self.list_elemts.column(7, width=60, anchor=CENTER)

        d = Data()
        self.rows = d.get_tasks()

        for i in self.rows:
            self.list_elemts.insert(
                '',
                'end',
                values=(
                    i.id,
                    i.title,
                    i.description,
                    i.create_at.strftime('%d-%m-%Y'),
                    'Completa' if i.done else 'Pendiente',
                    'Marcar como realizada',
                    'Eliminar'

                )
            )

        self.list_elemts.bind('<ButtonRelease-1>', self.on_click)
        self.list_elemts.place(x=340, y=90)

    def on_click(self, event):
        """
        Detecta el si se hizo click en eliminar o actualizar
        """
        item_id = self.list_elemts.identify_row(
            event.y)
        column = self.list_elemts.identify_column(
            event.x)

        if column == '#7':
            task_data = self.list_elemts.item(
                item_id, 'values')
            self.delete(int(task_data[0]))

        elif column == '#6':
            task_data = self.list_elemts.item(
                item_id, 'values')
            self.update_status(int(task_data[0]))

    def get_row(self, event):
        """
        Obtiene el registro seleccionado y crea una nueva ventana con el detalle
        """
        item = self.list_elemts.item(self.list_elemts.focus())

        task_id = item['values'][0]
        title = item['values'][1]
        description = item['values'][2]
        created_at = item['values'][3]
        done = item['values'][4]
        pop = Toplevel(self.frame)
        pop.geometry("400x400")

        lbl_title = Label(pop, font=("Arial", 12, "bold"), text=title)
        lbl_title.place(x=40, y=40)

        lbl_description = Label(pop, font=("Arial", 12,),
                                text=description, wraplength=250)
        lbl_description.place(x=40, y=80)

        lbl_created = Label(pop, font=("Arial", 12,),
                            text=f"Fecha de creación: {created_at}")
        lbl_created.place(x=40, y=200)

        lbl_status = Label(pop, font=("Arial", 12,), text=f"Estado: {done}")
        lbl_status.place(x=40, y=240)
        btn_change = Button(pop, text="Completada", relief="flat", background="#00CE54",
                            foreground="white", command=lambda: self.update_status(task_id))
        btn_change.place(x=180, y=280, width=90)
        btn_delete = Button(pop, text="Eliminar", relief="flat", background="red",
                            foreground="white", command=lambda: self.delete(task_id))
        btn_delete.place(x=290, y=280, width=90)

    def delete(self, n):
        """
        Elimina una tarea
        """
        d = Data()
        d.delete_task(n)
        messagebox.showinfo(title="Actualizacion",
                            message="Se han actualizado los datos")
        self.clear_list()
        self.draw_list()
        self.clear_entry()

    def update_status(self, task_id):
        """
        Actualiza el estado de una tarea
        """
        d = Data()
        d.update_task(task_id)
        messagebox.showinfo(title="Actualizacion",
                            message="Se han actualizado los datos")
        self.clear_list()
        self.draw_list()
        self.clear_entry()

    def clear_list(self):
        """Limpia la lista"""
        self.list_elemts.delete(*self.list_elemts.get_children())

    def clear_entry(self):
        """Limpia las entradas"""
        self.title.set("")
        self.txt_description.delete("1.0", "end")

    def confirm_process(self):
        """
        Agrega una tarea
        """

        if self.title.get() != "" and self.txt_description.get("1.0", "end") != "":

            d = Data()
            d.create_task(self.title.get(),
                          self.txt_description.get("1.0", "end"))
            messagebox.showinfo(
                title="Alerta", message="Se inserto correctamente!")
            self.clear_list()
            self.draw_list()
            self.clear_entry()
        else:
            messagebox.showinfo(
                title="Error", message="Debe llenar los campos para poder guardar!")


root = Tk()
root.title("Gestor de Tareas")
root.config(background="#7400b8")
root.geometry("1200x400")
aplication = App(root)
root.mainloop()
