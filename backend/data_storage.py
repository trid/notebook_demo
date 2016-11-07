from copy import copy

import datetime
import os
import sqlite3

from backend.note_item import NoteItem

CREATE_DB_QUERY = """CREATE TABLE notes (id INTEGER PRIMARY KEY,
                  first_name TEXT, last_name TEXT, phone_number TEXT, birthday TEXT)"""
UPDATE_QUERY = """UPDATE notes SET first_name = "%s", last_name = "%s", phone_number = "%s", birthday = "%s"
                               WHERE id = %d"""
INSERT_QUERY = """INSERT INTO notes (first_name, last_name, phone_number, birthday)
                               VALUES ("%s", "%s", "%s", "%s")"""
LAST_INSERTED_QUERY = """SELECT last_insert_rowid() FROM notes"""
LOAD_ALL_QUERY = """SELECT * FROM notes"""
DELETE_STATEMENT = """DELETE FROM notes WHERE id = %d"""


class DataStorage(object):
    def __init__(self, filename=None):
        """
        Creates clear DataStorage or loads data from file
        :param filename: path to file, if None, creates clear DataStorage
        """
        self.__items = []
        self.__todays_birthdays = []
        if filename is not None:
            self.__filename = filename
            self.load(filename)

    def create_item(self, first_name, last_name, phone_number, birthday):
        """
        Creates new NoteItem with arguments

        :param first_name: first name
        :param last_name: last name
        :param phone_number: phone number
        :param birthday: birthday
        """
        self.__items.append(NoteItem(first_name, last_name, phone_number, birthday))

    def __save_item(self, item, db):
        if item.id is not None:
            update_statement = UPDATE_QUERY % \
                               (item.first_name, item.last_name, item.phone_number, item.birthday, item.id)
            db.execute(update_statement)
        elif not item.deleted:
            insert_statement = INSERT_QUERY % \
                               (item.first_name, item.last_name, item.phone_number, item.birthday)
            db.execute(insert_statement)
            c = db.cursor()
            c.execute(LAST_INSERTED_QUERY)
            new_id = c.fetchone()[0]
            item.id = new_id

    def __delete_item(self, item, conn):
        # Remove only if ID is not None, else item is not existing in DB anyway
        if item.id is not None:
            conn.execute(DELETE_STATEMENT % item.id)

    def delete_item(self, id):
        """
        Delete item by ID.
        :param id: ID of item in list
        """
        self.items[id].delete()

    def save(self, filename=None):
        """
        Saves data to SQLite3 db
        :param filename: path to file,
        """
        new_file = filename is not None
        if new_file:
            # Creating new file with data
            self.__filename = filename
            # In case file already existing
            if os.path.exists(filename) and os.path.isfile(filename):
                os.remove(filename)

        conn = sqlite3.connect(self.__filename)
        if new_file:
            conn.execute(CREATE_DB_QUERY)
            for item in self.__items:
                self.__save_item(item, conn)
        else:
            # updating old file
            for item in self.__items:
                if item.dirty:
                    self.__save_item(item, conn)
                elif item.deleted:
                    self.__delete_item(item, conn)
        conn.commit()

    def load(self, filename):
        """
        Loads items from file
        :param filename: path to file
        """
        self.__items = []
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        cursor.execute(LOAD_ALL_QUERY)
        today_date = datetime.datetime.today().strftime("%d.%m")
        today_date = unicode(today_date)
        for row in cursor.fetchall():
            item = NoteItem(row[1], row[2], row[3], row[4], id=row[0])
            self.__items.append(item)
            if '.'.join(row[4].split('.')[:2]) == today_date:
                self.__todays_birthdays.append(item)

    @property
    def items(self):
        """
        Property to access DataStorage items. Creates copy of items list, so it will not be changed in client code

        :return: Copy of DataStorage items
        """
        return [item for item in self.__items if not item.deleted]

    @property
    def todays_birthdays(self):
        return copy(self.__todays_birthdays)

    @property
    def filename(self):
        """
        Read only propery for filename

        :return: filename for current storage object
        """
        return self.__filename
