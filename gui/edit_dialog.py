import Tkinter


class EditDialog(object):
    def __init__(self, parent, last_name="", first_name="", phone="", birthday=""):
        top = self.__top = Tkinter.Toplevel(parent)
        top.resizable(width=False, height=False)
        self.__parent = parent
        self.result = {}
        self.ok = False
        last_name_label = Tkinter.Label(top, text="Last Name")
        last_name_label.grid(column=0, row=0)
        last_name_input = Tkinter.Entry(top)
        last_name_input.insert(0, last_name)
        last_name_input.grid(column=1, row=0)
        self.__last_name_input = last_name_input
        first_name_label = Tkinter.Label(top, text="First Name")
        first_name_label.grid(column=0, row=1)
        first_name_input = Tkinter.Entry(top)
        first_name_input.insert(0, first_name)
        first_name_input.grid(column=1, row=1)
        self.__first_name_input = first_name_input
        phone_label = Tkinter.Label(top, text="Phone")
        phone_label.grid(column=0, row=2)
        phone_input = Tkinter.Entry(top)
        phone_input.insert(0, phone)
        phone_input.grid(column=1, row=2)
        self.__phone_input = phone_input
        birthday_label = Tkinter.Label(top, text="Birthday")
        birthday_label.grid(column=0, row=3)
        birthday_input = Tkinter.Entry(top)
        birthday_input.insert(0, birthday)
        birthday_input.grid(column=1, row=3)
        self.__bithday_input = birthday_input
        button_ok = Tkinter.Button(top, text="Ok", command=self.__on_ok)
        button_ok.grid(column=0, row=4, sticky=Tkinter.E + Tkinter.W)
        button_cancel = Tkinter.Button(top, text="Cancel", command=self.__on_cancel)
        button_cancel.grid(column=1, row=4, sticky=Tkinter.E + Tkinter.W)

    def show(self):
        self.__parent.wait_window(self.__top)

    def __on_ok(self):
        self.result = {"last_name": self.__last_name_input.get(),
                       "first_name": self.__first_name_input.get(),
                       "phone": self.__phone_input.get(),
                       "birthday": self.__bithday_input.get()}
        self.__top.destroy()
        self.ok = True

    def __on_cancel(self):
        self.__top.destroy()
