from tkinter import *
from food3 import where_to_eat

root = Tk()

def genre_button():
    global genre_entry
    genre_entry = Entry(root, width = 50, borderwidth=2)
    genre_entry.pack()

    button = Button(root, text = "Enter Cuisine", command = lambda: hide_widget(genre_entry, button, activator = 'Location', response = 'Genre'))
    button.pack()


def location_button():
    global location_entry
    location_entry = Entry(root, width = 50, borderwidth=2)
    location_entry.pack()

    button = Button(root, text = "Enter Zip Code or Location", command = lambda:hide_widget(location_entry, button, activator = None, response = 'Location'))
    button.pack()



def activate(event):
    if event == 'Genre':
        genre_button()

    if event == 'Location':
        location_button()


def hide_widget(*args, activator = None, response = None):
    for widget in args:
        if widget is not None:
            widget.pack_forget()

    if activator is not None:
        activate(activator)

    if response == 'Genre':
        global genre
        genre = genre_entry.get()

    if response == 'Location':
        global location
        location = location_entry.get()

        resturant = where_to_eat(str(genre), str(location))

        label = Label(root, text = resturant)
        label.pack()
        


start_button = Button(root, text = "Lets Find Dinner", command = lambda: hide_widget(start_button, activator = 'Genre'))
start_button.pack()




root.mainloop()