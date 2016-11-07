import Tkinter
from Tkinter import Button, Menu, Tk
from ttk import Scrollbar, Treeview


class MainWindow(object):
    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.minsize(800, 600)
        self.__main_window.iconbitmap("resources/quill.ico")
        self.__main_window.wm_title("Notebook Demo")
        self.__add_menu()

        cols = ("Last Name", "First Name", "Phone", "Birthday")
        tv = Treeview(self.__main_window, columns=cols, show="headings")
        for col in cols:
            tv.heading(col, text=col)
        tv.grid(row=0, sticky=Tkinter.N + Tkinter.S + Tkinter.E + Tkinter.W)
        Tkinter.Grid.columnconfigure(self.__main_window, 0, weight=1)
        Tkinter.Grid.rowconfigure(self.__main_window, 0, weight=1)
        Tkinter.Grid.columnconfigure(self.__main_window, 1, minsize=100)
        self.__add_buttons()

    def __add_buttons(self):
        frame = Tkinter.Frame(self.__main_window)
        frame.grid(row=0, column=1, sticky=Tkinter.N + Tkinter.E + Tkinter.W)
        button_add = Button(frame, text="Add")
        button_add.pack(fill=Tkinter.X)
        button_edit = Button(frame, text="Edit")
        button_edit.pack(fill=Tkinter.X)
        button_remove = Button(frame, text="Remove")
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
