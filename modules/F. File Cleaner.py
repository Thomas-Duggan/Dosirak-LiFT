#File Cleaner#

# Simplified Linux Utilities and Toolbox  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0


from os import listdir, path
from subprocess import run
from tkinter import *
from time import sleep

root = Tk()																		# Initial tkinter call and window variable redefinition
root.title("File Cleaner")		# Window title
root.geometry("640x480+50+50")													# Window size
logo = PhotoImage(file="logo.png")
root.iconphoto(root,logo)
    # Window initial setup


    # \/ Not my code \/
frame = Frame(root)
frame.grid(row=0, column=0, sticky="nsew")
canvas = Canvas(frame)
scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview, width=20)
canvas.configure(yscrollcommand=scrollbar.set)
content_frame = Frame(canvas)
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    # Code taken from:
    # https://www.tutorialspoint.com/implementing-a-scrollbar-using-grid-manager-on-a-tkinter-window

####################################################################################

rm_list = []

home = listdir(path.expanduser('~'))
folder = []
home_hidden = []
github = []

# Adds data for listed items
for file in range (len(home) -1, -1, -1):
    if home[file][0] == "." or home[file] in ("Downloads", "Desktop", "Videos", "Public", "Documents"):
        home_hidden.append(home[file])
        home.pop(file)

# Adds data if listed item contains a README.md
for file in range (len(home)):
    if "." in home[file]:
        folder.append(False)
        github.append(False)
    else:
        folder.append(True)
        if "README.md" in listdir(path.expanduser(f"~/{home[file]}")):
            github.append(True)
        else:
            github.append(False)


####################################################################################


Label(content_frame,
    text = "Red = Folder",
    fg = "red",
    ).grid(
        row = 1)

Label(content_frame,
    text = "Black = File" 
    ).grid(
        row = 2)


def append(val):
    if f'sudo rm -r ~/"{val}"' in rm_list:
        rm_list.remove(f'sudo rm -r ~/"{val}"')
    else:
        rm_list.append(f'sudo rm -r ~/"{val}"')
    

def button(title, row, folder, github = False):
    
    frame = Frame(content_frame)

    Button(frame,
            command=lambda: run(f'open "{path.expanduser(f"~/{title}")}"', shell=True),
            text = "Open", 
            bg = "grey",
            fg = "lime"
            ).grid(
                row = row,
                sticky="w")

    Checkbutton(frame,
            command=lambda: append(title),
            bg="red", 
            text="Delete", 
            fg="white", 
            selectcolor = "black"
            ).grid(
                row = row,
                column = 1,
                sticky = "w")
    

    if github == True:
        Label(frame,
            text = "  (github)",
            fg = "grey",
            ).grid(
                row = row,
                column=3)


    if folder == True:
        Label(frame,
            text = title,
            fg = "red",
            ).grid(
                row = row,
                column=2)
    

    if folder == False:
        Label(frame,
            text = title,
            ).grid(
                row = row,
                column=2)


    if folder == "hidden":
        Label(frame,
            text = title,
            fg = "grey",
            ).grid(
                row = row,
                column=2)
        
        Label(frame,text = "    DELETION NOT RECCOMENDED", 
              font = "arial 11 bold",
              fg = "red"
              ).grid(
                  row = row, 
                  column = 4,
                  sticky = "w") 

    frame.grid(row = row, sticky = "w")


row = 3

for file in range(len(home)):
    button(home[file], row, folder[file], github[file])
    row += 1

frame2 = Frame(content_frame)

row += 1
Label(frame2, text="", 
        font="arial 11 bold"
        ).grid(
            row=row,
            sticky="w", 
            padx=10)

row += 1
Label(frame2, text="Hidden Files / Folders:", 
        font="arial 11 bold"
        ).grid(
            row=row,
            sticky="w", 
            padx=10)


frame2.grid(row=row, sticky="w")

row += 1
for file in range(len(home_hidden)):
    button(home_hidden[file], row, "hidden")
    row += 1

####################################################################################

def file():
    global rm_list
    
    if len(rm_list) == 0:	# if there is nothing selected, do not continue
        pass					# Maybe add a pop-up saying nothing is selected?
    
    else:    
        cmd = open("shell_temp_folder.sh","w")	# Open shell script with write permissions
        cmd.write(" ;\n".join(rm_list))		# Combines list into single string (note: ";" means to run each command sequentially, regardless if any proceeding command fails)
        cmd.close()								# Closes shell script to reduce resources
        run('gnome-terminal -- xed ~/simple-linux-utility-and-toolbox/shell_temp_folder.sh', shell=True) # Launch edited shell script in terminal

    
button = Button(root, text="View Command",
                command=file)
button.grid(row=1,
            column=0,
            sticky="e",
            pady=5,
            padx=45)

confirm_level=0

def verify():
    global confirm_level

    confirm_level += 1
    if confirm_level == 1:
        delete_button.config(text="Are You Sure?")
    if confirm_level == 2:
        delete_button.config(text="Last Chance.")
    if confirm_level == 3:
        purge() 
    if confirm_level >= 5:
        purge() 
        delete_button.config(text="Select Something!")
    if confirm_level >= 10:
        purge() 
        delete_button.config(text="Are you looking for a secret?")
    if confirm_level >= 20:
        purge() 
        delete_button.config(text="sudo rm -fr ~")
    if confirm_level >= 21:
        purge() 
        delete_button.config(text="Just kidding!")
    if confirm_level >= 25:
        purge() 
        delete_button.config(text="Okay, I'm bored now.")
    if confirm_level >= 35:
        delete_button.config(text="Delete Forever")
        confirm_level = 0




def purge():
    global rm_list

    if len(rm_list) == 0:	# if there is nothing selected, do not continue
        pass					# Maybe add a pop-up saying ~/s nothing is selected?

    else:    
        cmd = open("shell_temp_folder.sh","w")	# Open shell script with write permissions
        cmd.write(" ;\n".join(rm_list))		# Combines list into single string (note: ";" means to run each command sequentially, regardless if any proceeding command fails)
        cmd.close()								# Closes shell script to reduce resources
        
        run('gnome-terminal -- python3 ~/simple-linux-utility-and-toolbox/home.py && exit', shell=True) # Launch edited shell script in terminal
        sleep(0.25)
        run('gnome-terminal -- bash ~/simple-linux-utility-and-toolbox/shell_temp_folder.sh', shell=True) # Launch edited shell script in terminal
        exit()
     
delete_button = Button(root, text="Delete Forever",
                        command=verify, 
                        bg="red", 
                        fg="black"
                        )
delete_button.grid(row=1,
                    column=0,
                    sticky="n",
                    pady=20,
                    padx=45)



def home():
    run('gnome-terminal -- python3 ~/simple-linux-utility-and-toolbox/home.py && exit', shell=True) # Launch edited shell script in terminal
    exit()	# kills current script once shell script is running
    
button = Button(root, text="🡄 Return Home",
                command=home)
button.grid(row=1,
            column=0,
            sticky="w",
            pady=5,
            padx=45)

# \/ Not my code \/
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
canvas.create_window((0, 0), window=content_frame, anchor="nw")
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")
def _on_mousewheel(event):
   canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
canvas.bind_all("<MouseWheel>", _on_mousewheel)
    # Code taken from:
    # https://www.tutorialspoint.com/implementing-a-scrollbar-using-grid-manager-on-a-tkinter-window
    

content_frame.mainloop()	# Required to make window appear