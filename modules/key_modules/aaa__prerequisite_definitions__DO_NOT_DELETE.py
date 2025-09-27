# Prereq Defs #

# Simplified Linux Utilities and Toolbox  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0

from subprocess import run
from tkinter import *
import webbrowser as wb
from os import path, listdir, system
from ast import literal_eval

settings = open(path.expanduser("~/simplified-linux-utilities-and-toolbox/modules/key_modules/settings_values.py"),"r")
settings_dict = literal_eval(settings.read())
settings.close()

row = 1

def bind_scroll(item):
    item.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
    item.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))


# Initialization

def create_content(title, x = "640", y = "480", background = "#d9d9d9"):

    global root, frame, canvas, scrollbar, content_frame

    offset = settings_dict["general"]["popup offset"]
    location = settings_dict["general"]["popup location"].split()
    screen_x = settings_dict["general"]["screen width"]
    screen_y = settings_dict["general"]["screen height"]

    if location[0] == "Top":
        y_offset = offset

    if location[0] == "Middle":
        y_offset = int((screen_y / 2)) - int((int(y) / 2))

    if location[0] == "Bottom":
        y_offset = screen_y - offset - int(y)

    if location[1] == "Left":
        x_offset = offset
    
    if location[1] == "Middle":
        x_offset = int((screen_x / 2)) - int((int(x) / 2))

    if location[1] == "Right":
        x_offset = screen_x - offset - int(x)

    root = Tk()																		# Initial tkinter call and window variable redefinition
    root.title(title)		# Window title
    root.geometry(f"{x}x{y}+{x_offset}+{y_offset}")	
    root.configure(bg = background)												# Window size
    logo = PhotoImage(file = path.join(path.expanduser("~/simplified-linux-utilities-and-toolbox/logo.png")))
    root.iconphoto(root,logo)
    # Initial setup for tkinter

    # \/ Not my code \/
    frame = Frame(root)
    frame.grid(row = 0, column = 0, sticky = "nsew")
    canvas = Canvas(frame)
    scrollbar = Scrollbar(frame, orient = "vertical", command = canvas.yview, width = 20)
    canvas.configure(yscrollcommand = scrollbar.set, bg = background)
    content_frame = Frame(canvas)
    content_frame.configure(bg = background)
    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
    # Code taken from:
    # https://www.tutorialspoint.com/implementing-a-scrollbar-using-grid-manager-on-a-tkinter-window

def run_content(home = False):

    global root, frame, canvas, scrollbar, content_frame

    if home == False:
        def home():
            run('gnome-terminal -- python3 ~/simplified-linux-utilities-and-toolbox/home.py && exit', shell=True)
            exit()

        button = Button(root, text = "🡄 Return Home",
                    command = home
                    ).grid(
                        row = 1,
                        column = 0,
                        sticky = "w",
                        pady = 5,
                        padx = 45)

    # \/ Not my code \/
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)
    frame.columnconfigure(0, weight = 1)
    frame.rowconfigure(0, weight = 1)
    canvas.create_window((0, 0), window = content_frame, anchor="nw")
    canvas.grid(row = 0, column = 0, sticky = "nsew")
    scrollbar.grid(row = 0, column = 1, sticky = "ns")
    # Code taken from:
    # https://www.tutorialspoint.com/implementing-a-scrollbar-using-grid-manager-on-a-tkinter-wind

    bind_scroll(canvas)
    bind_scroll(content_frame)

    root.mainloop()	# Required to make window appear


# Grouping 

def group_open(parent = "default", background = "#d9d9d9", exists = True):

    global content_frame, group_frame, row, column

    if parent == "default":
        parent = content_frame

    group_frame = Frame(parent)
    group_frame.grid_rowconfigure(row, weight=1)
    group_frame.grid_columnconfigure(1, weight=1)
    group_frame.configure(bg = background)
    bind_scroll(group_frame)

    column = 1

    if exists == False:
        group_frame.grid_forget()

def group_close(sticky = "w", exists = True):

    global group_frame, row

    group_frame.grid(row = row, sticky = sticky)

    row += 1

    if exists == False:
        group_frame.grid_forget()

def group_new_line(exists = True):
    group_close(exists = exists)
    group_open(exists = exists)


# Menu Items

def spacer(exists = True):

    global group_frame, row

    spacer = Label(group_frame, text="", height=1)
    spacer.grid(row=row)
    bind_scroll(spacer)

    row += 1

    if exists == False:
        spacer.grid_forget()

def button(text, command, keep_row = False, sticky = "w", exists = True):

    global group_frame, row, column

    button = Button(group_frame, 
                    text = text,
                    command = command)
    button.grid(row = row,
                column = column,
                sticky = sticky,
                pady = 5,
                padx = 7)
    bind_scroll(button)
    
    if keep_row == True:
        column += 1
    else:
        column = 1
        row += 1

    if exists == False:
        button.grid_forget()


def home_buttons():
    modules = listdir(path.expanduser('~/simplified-linux-utilities-and-toolbox/modules'))
    modules.sort()
    
    for module in range(len(modules) -1, -1, -1):
        file_name = modules[module]

        # Removes non-module files
        if file_name in ["__pycache__", "!!! Read Me !!! .txt", "key_modules", "screenshot.py"]:
            modules.pop(module)

    for module in range (len(modules)):
        file_name = modules[module]
        
        # Names the button
        file_text = open(f"modules/{file_name}", mode = "r")
        code = file_text.read()
        file_text.close()

        title_barriers = []
        for letter in range(len(code)):
            if code[letter] == "#":
                title_barriers.append(letter)
            if len(title_barriers) == 2:
                break

        title_barriers[0] += 1
        title = code[title_barriers[0]:title_barriers[1]]

        # Creates the button
        button_n = button(title,
               lambda file = file_name: (run(f'gnome-terminal -- python3 ~/simplified-linux-utilities-and-toolbox/modules/"{file}" && exit', shell = True), exit()),
               sticky = "n")

def text(text, type = None, location = "left", color = "#000000", background = "#d9d9d9", keep_row=False, exists = True):

    global group_frame, row, column


    if location == "top":
        sticky = "n"
    elif location == "right":
        sticky = "e"
    elif location == "bottom":
        sticky = "s"
    else:
        sticky = "w",


    if type == "home_title":
        font = "TkDefaultFont 14 bold"

    elif type == "title":
        font = "TkDefaultFont 12 bold"

    elif type == "title_not_bold":
        font = "TkDefaultFont 12"

    elif type == "subtitle":
        font = "TkDefaultFont 9"

    else:
        font = "TkDefaultFont"
    

    title = Label(group_frame,
                    text = text,
                    font = font,
                    fg = color,
                    bg = background)
    title.grid(row = row, 
                column = column, 
                sticky = sticky, 
                padx = 0) 
    bind_scroll(title)


    if keep_row == True:
        column += 1
        
    else:
        column = 1
        row += 1

    if exists == False:
        title.grid_forget()

def checkbox():
    pass
