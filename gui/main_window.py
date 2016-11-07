import Tkinter
from Tkinter import Button, Menu, Tk
from ttk import Scrollbar, Treeview

from backend.data_storage import DataStorage
from gui.edit_dialog import EditDialog


class MainWindow(object):
    def __init__(self, datasource=None):
        self.__main_window = Tk()
        self.__main_window.minsize(800, 600)
        self.__main_window.iconbitmap("resources/quill.ico")
        self.__main_window.wm_title("Notebook Demo")
        self.__add_menu()

        cols = ("Last Name", "First Name", "Phone", "Birthday")
        tv = Treeview(self.__main_window, columns=cols, show="headings")
        self.__table = tv
        for col in cols:
            tv.heading(col, text=col)
        tv.grid(row=0, sticky=Tkinter.N + Tkinter.S + Tkinter.E + Tkinter.W)
        Tkinter.Grid.columnconfigure(self.__main_window, 0, weight=1)
        Tkinter.Grid.rowconfigure(self.__main_window, 0, weight=1)
        Tkinter.Grid.columnconfigure(self.__main_window, 1, minsize=100)
        self.__add_buttons()
        # To be able to use this UI from another app and as autonomous app
        # Also, I just hate an idea of creating storage in UI
        if datasource is None:
            self.__datasource = DataStorage()
        else:
            self.__datasource = datasource

    def __add_buttons(self):
        frame = Tkinter.Frame(self.__main_window)
        frame.grid(row=0, column=1, sticky=Tkinter.N + Tkinter.E + Tkinter.W)
        button_add = Button(frame, text="Add", command=self.__add_button_pressed)
        button_add.pack(fill=Tkinter.X)
        button_edit = Button(frame, text="Edit", command=self.__edit_button_pressed)
        button_edit.pack(fill=Tkinter.X)
        button_remove = Button(frame, text="Remove", command=self.__remove_button_pressed)
        button_remove.pack(fill=Tkinter.X)

    def run(self):
        self.__main_window.mainloop()

    def __add_menu(self):
        menubar = Menu(self.__main_window)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Load")
        file_menu.add_command(label="Exit")
        menubar.add_cascade(label="File", menu=file_menu)
        self.__main_window.config(menu=menubar)

    def __update_table(self):
        self.__table.delete(*self.__table.get_children())
        items = self.__datasource.items
        for item_id in range(len(items)):
            item = items[item_id]
            self.__table.insert("", "end", values=(item.last_name, item.first_name, item.phone_number, item.birthday, item_id))

    def __add_button_pressed(self):
        edit_dialog = EditDialog(self.__main_window)
        edit_dialog.show()
        res = edit_dialog.result
        self.__datasource.create_item(res["first_name"], res["last_name"], res["phone"], res["birthday"])
        self.__update_table()

    def __edit_button_pressed(self):
        selection_id = self.__table.selection()[0]
        cur_item = self.__table.item(selection_id)
        item_id = cur_item["values"][4]
        item = self.__datasource.items[item_id]
        edit_dialog = EditDialog(self.__main_window, item.last_name, item.first_name, item.phone_number, item.birthday)
        edit_dialog.show()
        res = edit_dialog.result
        item.first_name = res["first_name"]
        item.last_name = res["last_name"]
        item.phone_number = res["phone"]
        item.birthday = res["birthday"]
        self.__update_table()

    def __remove_button_pressed(self):
        selection_id = self.__table.selection()[0]
        cur_item = self.__table.item(selection_id)
        item_id = cur_item["values"][4]
        self.__datasource.delete_item(item_id)
        self.__update_table()