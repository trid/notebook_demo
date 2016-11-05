class NoteItem(object):
    def __init__(self, first_name, last_name, phone_number, birthday, dirty=False):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__birthday = birthday
        self.__dirty = dirty

    first_name = property()
    last_name = property()
    phone_number = property()
    birthday = property()

    @first_name.getter
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
        self.__dirty = True

    @last_name.getter
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
        self.__dirty = True

    @phone_number.getter
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number
        self.__dirty = True

    @birthday.getter
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday
        self.__dirty = True

    @property
    def dirty(self):
        return self.__dirty