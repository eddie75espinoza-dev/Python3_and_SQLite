import os
import tkinter as tk
from tkinter import ttk
from tkinter import *

import sqlite3

# Class Definition
class User:
    db_name = "client.db"

    def __init__(self, window):
        self.wind = window
        self.wind.title('Client with DB SQLite')

        # Creating a Frame container
        frame = LabelFrame(self.wind, text = "Customer Registration")
        frame.grid(row = 0, column = 0, pady = 16)

        # Name input
        Label(frame, text = "First Name: ").grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)
        self.name.focus()

        # LastName input
        Label(frame, text = "Last Name: ").grid(row = 2, column = 0)
        self.last_name = Entry(frame)
        self.last_name.grid(row = 2, column = 1)

        # Button add
        ttk.Button(text = '  Save  ', command = self.add_client).grid(row = 4, column = 0, pady = 8)

        # Button Edit
        ttk.Button(text = '  Edit  ', command = self.edit_client).grid(row = 20, column = 0, padx = 56, pady = 8,
                                                                       sticky = W)

        # Button Delete
        ttk.Button(text = 'Delete', command = self.del_client).grid(row = 20, column = 0, padx = 56, pady = 8,
                                                                    sticky = E)

        # Interaction message
        self.message = Label(text = "", fg = 'blue')
        self.message.grid(row = 6, column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(columns = 3, selectmode = 'browse', height = 10, padding = 8)
        self.tree.grid(row = 8, column = 0)
        # Scrollbar
        self.vsb = ttk.Scrollbar(window, orient = 'vertical', command = self.tree.yview)
        #self.vsb.pack(side = 'right', fill = 'y')
        self.vsb.place(x= 400, y=155, height = 243) 
        self.tree.configure(yscrollcommand = self.vsb.set)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Last Name', anchor = CENTER)


        # Get DB Client
        self.get_clients()

    # Query and Connection
    def db_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Get customer table data
    def get_clients(self):
        # Cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Consulting table
        query = 'SELECT * FROM client ORDER BY name DESC'
        db_rows = self.db_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    # Validation data entry
    def validation(self):
        return len(self.name.get()) != 0 and len(self.last_name.get()) != 0

    # Add Client
    def add_client(self):
        if self.validation():
            query = 'INSERT INTO client VALUES (NULL, ?, ?)'
            parameters = (self.name.get(), self.last_name.get())
            self.db_query(query, parameters)
            self.message['text'] = 'Registered {} correctly'.format(self.name.get())
            self.name.delete(0, END)
            self.last_name.delete(0, END)
        else:
            self.message['text'] = 'Data required'
        self.name.focus()
        self.get_clients()

    # Edit records
    def edit_client(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Select a record'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_lastName = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()

        # Creating a Frame container for Edit Client
        read_frame = LabelFrame(self.edit_wind, text = "Edit Client")
        read_frame.grid(row = 0, column = 0, padx = 8, pady = 8)

        # Read only Registro actual de cliente
        Label(read_frame, text = "Name: ").grid(row = 1, column = 0)
        Entry(read_frame, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 1,
                                                                                                           column = 1)

        # Read Only LastName input
        Label(read_frame, text = "Last Name: ").grid(row = 2, column = 0)
        Entry(read_frame, textvariable = StringVar(self.edit_wind, value = old_lastName), state = 'readonly').grid(
            row = 2, column = 1)

        # New record

        # Creating a Frame container for Edit Client
        edit_frame = LabelFrame(self.edit_wind, text = "New Record")
        edit_frame.grid(row = 4, column = 0, padx = 8, pady = 8)

        # Editing only Registro actual de cliente
        Label(edit_frame, text = "(new) Name: ").grid(row = 5, column = 0)
        new_name = Entry(edit_frame)
        new_name.grid(row = 5, column = 1)

        # Editing Only LastName input
        Label(edit_frame, text = "(new) Last Name: ").grid(row = 6, column = 0)
        new_lastName = Entry(edit_frame)
        new_lastName.grid(row = 6, column = 1)

        # Button Update
        Button(self.edit_wind, text = 'Update',
               command = lambda: self.update_client(new_name.get(), new_lastName.get(), name, old_lastName)).grid(
            row = 8, column = 9, columnspan = 2, padx = 24, pady = 8)

    def update_client(self, new_name, new_lastName, name, old_lastName):
        if len(new_name) != 0 and len(new_lastName) != 0:
            query = 'UPDATE client SET name = ?, last_name = ? WHERE name = ? AND last_name = ?'
            parameters = (new_name, new_lastName, name, old_lastName)
            self.db_query(query, parameters)
            self.edit_wind.destroy()
            self.message['text'] = 'Update {} RegistrationData'.format(name)
            self.get_clients()
        else:
            self.message['text'] = 'Data Required'
            return

    # Delete records
    def del_client(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Select a record'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM client WHERE name = ?'
        self.db_query(query, (name,))
        self.message['text'] = 'Record {} delete'.format(name)
        self.get_clients()


if __name__ == '__main__':
    window = tk.Tk()
    sp = 'C:\\Users\\Familia Espinoza\\Desktop\\Python\\Gui_DB_SQL\\img\\'
    # Icon
    img_icon = PhotoImage(file = os.path.join(sp, 'LogoE256.png'))
    window.tk.call('wm', 'iconphoto', window._w, img_icon)
    application = User(window)
    window.mainloop()
