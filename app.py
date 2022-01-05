from tkinter import Tk, Label, Button, Entry, Checkbutton, Radiobutton, IntVar, StringVar, Scale, OptionMenu, Toplevel, filedialog, DISABLED, NORMAL, HORIZONTAL, END, CENTER
from tkinter import messagebox, Menu, Frame, ttk
from PIL import Image, ImageTk


def grettings():
    """gretting function for the Say Hello button
    """
    display_gretting = Label(app, text='Hi Dude!!!', font=('Courier', 12), background='white', foreground='black', relief='flat', width=15, borderwidth=4)  # Create a Label object
    display_gretting.grid(row=1 ,column=2 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window
    if button_exit['state'] == DISABLED:  # Check if the exit button is disableDd
        button_exit.config(state=NORMAL)  # Be able the exit button
        messagebox.showinfo(title='Info Message', message='This is an info message')  # Show an Info messagebox


def show_your_entry():
    """Function to show the inputed value in Entry object
    """
    inputed_text = input.get()  # Get the tet in the entry object
    display_entry = Label(app, text=inputed_text, font=('Courier', 12), background='white', foreground='black', relief='flat', width=15, borderwidth=4)  # Create a Label object
    display_entry.grid(row=2 ,column=2 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window
    if button_exit['state'] == DISABLED:  # Check if the exit button is disableDd
        button_exit['state'] = NORMAL  # Be able the exit button
        messagebox.showerror(title='Error Message', message='This is an Error message')  # Show an Error messagebox


def show_checkbutton():
    """Function to show the value based on checkbutton state
    """
    value = check_value.get()  # Get the text in the entry object
    display_checkbutton = Label(app, text=value, font=('Courier', 12), background='white', foreground='black', relief='flat', width=15, borderwidth=4)  # Create a Label object
    display_checkbutton.grid(row=3 ,column=2 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window
    messagebox.showwarning(title='Warning Message', message='This is an Warning message')  # Show a Warning messagebox


def show_radiobutton():
    """Function to show the value based on radiobutton state
    """
    value = radio_value.get()  # Get the text in the entry object
    display_checkbutton = Label(app, text=value, font=('Courier', 12), background='white', foreground='black', relief='flat', width=15, borderwidth=4)  # Create a Label object
    display_checkbutton.grid(row=4 ,column=2 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window
    messagebox.askyesno(title='Asking Message', message='Select Yes or No')  # Show messagebox asking for Yes or No


def show_scale_value():
    """Function to show the value based on Scale value
    """
    value = slide_value.get()  # Get the tet in the entry object
    display_scale = Label(app, text=value, font=('Courier', 12), background='white', foreground='black', relief='flat', width=15, borderwidth=4)  # Create a Label object
    display_scale.grid(row=5 ,column=2 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window
    messagebox.askokcancel(title='Asking Message', message='Select Ok or Cancel')  # Show messagebox asking for Ok or Cancel


def show_dropdown_value():
    """Function to show the value in dropdown menu
    """
    value = dropdown_value.get()  # Get the tet in the entry object
    display_scale = Label(app, text=value, font=('Courier', 12), background='white', foreground='black', relief='flat', width=15, borderwidth=4)  # Create a Label object
    display_scale.grid(row=6 ,column=2 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window


# Initialize the main window and set its attributes
app = Tk()  # Create a Tkinter object called app
app.title('Element Picker')  # Add a tittle for the project window
app.geometry('1000x800')  # Assign the dimensions of the window
app['background'] = 'black'  # add a window background
# app.iconbitmap('./icon.jpeg')  # Add an icon in the top of the window

# Create a label to display
Display = Label(app, text='Application window', background='white', foreground='black', relief='raised', width=15, borderwidth=4)  # Create a Label object
Display.grid(row=0 ,column=0 , rowspan=1, columnspan=3, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create a button to say hello
button_grettings = Button(app, text='Say Hello', command=grettings, background='white', foreground='black', width=15, borderwidth=4)  # Create a Button object
button_grettings.grid(row=1 ,column=0 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create a textbox to set an entry value
input = Entry(app, background='white', show='*', state=NORMAL, justify=CENTER, foreground='black', width=15, borderwidth=4)  # Create an Entry object
input.insert(0, 'Ingrese una cadena')  # Inset a default text
input.insert(END, '.')  # Inset a default text
input.grid(row=2 ,column=0 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create a button to get the entry text
button_entry = Button(app, text='Get the entry text', command=show_your_entry, background='white', foreground='black', width=15, borderwidth=4)  # Create a Button object
button_entry.grid(row=2 ,column=1 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create a Checkbox widget
check_value = StringVar()  # Set a variable for the checkbox
checkbox_meco = Checkbutton(app, text='Meco', variable=check_value, onvalue='Yes', offvalue='Nope')  # Create a Checkbutton object
checkbox_meco.select()  # select the checkbox by default
checkbox_meco.grid(row=3 ,column=0 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create a Button to show the value in checkbox
button_checkbutton = Button(app, text='Show check value', command=show_checkbutton, state=NORMAL, background='white', foreground='black')  # Create a Button object
button_checkbutton.grid(row=3 ,column=1 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create a radio button
radio_value = IntVar()  # Set a variable for the radiobutton
radiobutton = Radiobutton(app, text='Meco', variable=radio_value, value=10)  # Create a Radiobutton object
radiobutton.deselect()  # deselect the radiobutton by default
radiobutton.grid(row=4 ,column=0 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create a Button to show the value in checkbox
button_checkbutton = Button(app, text='Show check value', command=show_radiobutton, state=NORMAL, background='white', foreground='black')  # Create a Button object
button_checkbutton.grid(row=4 ,column=1 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create an Slider widget
slide_value = IntVar()  # Set a variable for the Slider
slider = Scale(app, from_=0, to=100, variable=slide_value, orient=HORIZONTAL)  # Create a Slider object
slider.grid(row=5 ,column=0 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create a Button to show the value in Slide
button_scale = Button(app, text='Show Slide value', command=show_scale_value, state=NORMAL, background='white', foreground='black')  # Create a Button object
button_scale.grid(row=5 ,column=1 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create an Dropdown menu
dropdown_value = StringVar()  # Set a variable for the dropdown
options = ['one', 'two', 'three', 'four', 'five', 'six']
dropdown_menu = OptionMenu(app, dropdown_value, *options)  # Create a Slider object
dropdown_menu.grid(row=6 ,column=0 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create a Button to show the value in dropdown menu
button_scale = Button(app, text='Show Dropdown menu value', command=show_dropdown_value, state=NORMAL, background='white', foreground='black')  # Create a Button object
button_scale.grid(row=6 ,column=1 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create an Dropdown menu
out_window = Toplevel()
out_window.title('Another window')

# Open a file browser dialog window
app.fname = filedialog.askopenfilename(initialdir='./', title='Select the file to open',
            filetypes=(('PNG images', '*.png'), ('JPG images', '*.jpg'), ('JPEG images', '*.jpeg'),
                        ('ICON images', '*.ico'), ('SVG images', '*.svg')
                        ))  # Open a file browser dialog window

# Load an image
image = ImageTk.PhotoImage(Image.open(app.fname))
Display_image = Label(app, image=image)  # Create a Label object
Display_image.grid(row=7 ,column=1 , rowspan=1, columnspan=3, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Create a Menu in the window
main_menu = Menu(app)  # Create a menu widget in the main window
file_menu = Menu(main_menu, tearoff=False)  # tearsoff=False to aviod that the menu being separated from main menu
file_menu.add_command(label='New')  # Add some value to menu
file_menu.add_cascade(menu=file_menu, label='File')  # Add another value to file_menu
app.config(menu=main_menu)  # Add menus to the main window

# Create a new tab in the window
tabs_controller = ttk.Notebook(app)  # create a Fame to control the tabs to add
tab_one = Frame(tabs_controller)  # Add a tab to frame
tabs_controller.add(tab_one, text='first tab')  # Add a tab

# Dice unicode characters dictionary
Dice = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}

# First dice character to show when the app starts
lbl = Label(app, text=Dice[0], font=('Times', 100))
lbl.grid(row=8, column=0, padx=40)


# Choose number from 1 - 6 randomly and display it
def roll():
    from random import randint
    dice_choice = randint(1, 6)

    dice_lbl = Label(app, text=Dice[dice_choice], font=('Times', 100), width=2)
    dice_lbl.grid(row=8, column=2, padx=40)


# Roll button
roll_button = Button(app, text='Roll', command=roll)
roll_button.grid(row=8, column=1, padx=40)

# Create a quit app button
button_exit = Button(app, text='Exit App', command=app.quit, state=DISABLED, background='white', foreground='black')  # Create a Button object
button_exit.grid(row=9 ,column=2 , rowspan=1, columnspan=1, padx=25, pady=5, sticky='NW')  # Positioned the object in the window

# Main loop to run the window
app.mainloop()  # Run the created window in a loop
