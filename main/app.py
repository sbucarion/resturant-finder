from tkinter import *
from tkinter.ttk import *
from find_restuarant import where_to_eat


#Start Application
root = Tk()
root.geometry("1000x600")


def genre_button():
    """
    Create button and entry box to accept user input for food genre
    Once button clicked, hide_widget function runs to remove button 
    and entry box and run the location button
    """

    #Activate button and entry box
    global genre_entry
    genre_entry = Entry(root, width = 50)
    genre_entry.pack()

    button = Button(root, text = "Enter Cuisine", command = lambda: hide_widget(genre_entry, button, activator = 'Location', response = 'Genre'))
    button.pack()


def location_button():
    """
    Create button and entry box to accept user input for location
    Once button clicked, hide_widget function runs to remove button 
    and entry box and display chosen restuarant
    """

    #Activate button and entry box
    global location_entry
    location_entry = Entry(root, width = 50)
    location_entry.pack()

    button = Button(root, text = "Enter Zip Code or Location", command = lambda:hide_widget(location_entry, button, activator = None, response = 'Location'))
    button.pack()


def activate(event):
    """
    Function runs when a button is pressed
    whcih will run the next button in the process
    """

    if event == 'Genre':
        genre_button()

    if event == 'Location':
        location_button()


def hide_widget(*args, activator = None, response = None):
    """
    Remove widgets like entry box and button from screen
    when the function is ran from a button click
    """

    #Remove specified entry and button passed as params (*args)
    for widget in args:
        if widget is not None:
            widget.pack_forget()

    #Activates next button and entry box in process
    if activator is not None:
        activate(activator)

    #Pull out user input data once submitted
    if response == 'Genre':
        global genre
        genre = genre_entry.get() #Get user input from genre_entry box

    if response == 'Location':
        global location
        location = location_entry.get() #Get user input from location_entry box

        #Generate restuarant choice
        resturant = where_to_eat(str(genre), str(location))

        #Display selected restuarant
        label = Label(root, text = resturant)
        label.pack()
        

#Initial button to begin process, once clicked genre button will activite
start_button = Button(root, text = "Lets Find Dinner", command = lambda: hide_widget(start_button, activator = 'Genre'))
start_button.pack()


#Without this loop application wont open
root.mainloop()