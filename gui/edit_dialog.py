import Tkinter


class EditDialog(object):
    def __init__(self, parent, last_name="", first_name="", phone="", birthday=""):
        top = self.top = Tkinter.Toplevel(parent)
        last_name_label = Tkinter.Label(top, text="Last Name")
        last_name_label.grid(column=0, row=0)
        last_name_input = Tkinter.Entry(top)
        last_name_input.insert(0, last_name)
        last_name_input.grid(column=1, row=0)
        first_name_label = Tkinter.Label(top, text="First Name")
        first_name_label.grid(column=0, row=1)
        first_name_input = Tkinter.Entry(top)
        first_name_input.insert(0, first_name)
        first_name_input.grid(column=1, row=2)
        phone_label = Tkinter.Label(top, text="Phone")
        phone_label.grid(column=0, row=3)
        phone_input = Tkinter.Entry(top)
        phone_input.insert(0, phone)
        phone_input.grid(column=1, row=3)
        birthday_label = Tkinter.Label(top, text="Birthday")
        birthday_label.grid(column=0, row=4)
        birthday_input = Tkinter.Entry(top)
        birthday_input.insert(0, birthday)
        birthday_input.grid(column=1, row=4)
        button_ok = Tkinter.Button(top, text="Ok")

