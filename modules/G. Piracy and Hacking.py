#Piracy / Hacking#


from subprocess import run
from tkinter import *
import webbrowser as wb
    #Imports

root = Tk()																		# Initial tkinter call and window variable redefinition
root.title("Sapphire's Linux Utility and Toolbox   -   Piracy / Hacking")		# Window title
root.geometry("640x480+50+50")														# Window size
logo = PhotoImage(file="logo.png")
root.iconphoto(root,logo)
    # Initial setup for tkinter

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

##################################################################################
spacer = Label(content_frame,text="").grid(row=0) 
##################################################################################

main_title = Label(content_frame, text="Piracy:", 
                   font="arial 12 bold", 
                   padx=10
                   ).grid(
                   row=1, 
                   sticky = 'w')

frame2 = Frame(content_frame)


def downloader():
    wb.open("https://chromewebstore.google.com/detail/video-downloadhelper/lmjnegcaeklhafolokijcfjliaokphfk")

button = Button(frame2, text="Video DownloadHelper",
                command=downloader)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Website Video Downloader (VDH)"
              ).grid(
              row=2, 
              column=2, 
              sticky="w", 
              padx=0) 
title = Label(frame2,text=" (Google Chrome Extension)", 
              fg="grey"
              ).grid(
              row=2, 
              column=3, 
              sticky="w", 
              padx=0) 

frame2.grid(row=2, sticky="w")


frame2 = Frame(content_frame)

def anna():
    wb.open("https://annas-archive.org/")

button = Button(frame2, text="Anna's Archive",
                command=anna)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Book Archive").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=3, sticky="w")


frame2 = Frame(content_frame)

def steamunlocked():
    wb.open("https://steamunlocked.net/")

button = Button(frame2, text="SteamUnlocked",
                command=steamunlocked)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Steam Game Archive").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=4, sticky="w")


frame2 = Frame(content_frame)

def wcos():
    wb.open("https://www.wcostream.tv/")

button = Button(frame2, text="Watch Cartoons Online",
                command=wcos)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Cartoon and Anime Archive").grid(row=2, column=2, sticky="w", padx=0) 
title = Label(frame2,text=" (Use VDH to download)", 
              fg="grey"
              ).grid(
              row=2, 
              column=3, 
              sticky="w", 
              padx=0) 

frame2.grid(row=5, sticky="w")


frame2 = Frame(content_frame)

def rroms():
    wb.open("https://r-roms.github.io/")

button = Button(frame2, text="r/Roms Megathread",
                command=rroms)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Miscellaneous Rom Archive").grid(row=2, column=2, sticky="w", padx=0) 
title = Label(frame2,text=" (Best for WiiU Games)", 
              fg="grey"
              ).grid(
              row=2, 
              column=3, 
              sticky="w", 
              padx=0) 

frame2.grid(row=6, sticky="w")


frame2 = Frame(content_frame)

def romsfun():
    wb.open("https://romsfun.com/")

button = Button(frame2, text="Romsfun",
                command=romsfun)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Miscellaneous Rom Archive").grid(row=2, column=2, sticky="w", padx=0) 
title = Label(frame2,text=" (Best for DS / 3DS Games)", 
              fg="grey"
              ).grid(
              row=2, 
              column=3, 
              sticky="w", 
              padx=0) 

frame2.grid(row=7, sticky="w")


frame2 = Frame(content_frame)

def vimms():
    wb.open("https://vimm.net/")

button = Button(frame2, text="Vimm's Lair",
                command=vimms)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Miscellaneous Rom Archive").grid(row=2, column=2, sticky="w", padx=0) 
title = Label(frame2,text=" (Best for Wii / Gamecube Games)", 
              fg="grey"
              ).grid(
              row=2, 
              column=3, 
              sticky="w", 
              padx=0) 

frame2.grid(row=8, sticky="w")


frame2 = Frame(content_frame)

def vimms():
    wb.open("https://myrient.erista.me/files/Redump/")

button = Button(frame2, text="Myrient",
                command=vimms)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Miscellaneous Gaming Archive").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=9, sticky="w")


frame2 = Frame(content_frame)

def intarc():
    wb.open("https://archive.org/")

button = Button(frame2, text="The Internet Archive",
                command=intarc)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Miscellaneous Archive").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=10, sticky="w")

##################################################################################
spacer = Label(content_frame,text="").grid(row=1000)
##################################################################################


main_title = Label(content_frame, text="Hacking:", 
                   font="arial 12 bold", 
                   padx=10
                   ).grid(
                   row=1001, 
                   sticky = 'w')

frame2 = Frame(content_frame)

def microsoft():
    wb.open("https://github.com/massgravel/Microsoft-Activation-Scripts")

button = Button(frame2, text="Microsoft Activation Scripts",
                command=microsoft)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Windows 10 Activator / Microsoft 365 Subscription Bypass").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1002, sticky="w")


frame2 = Frame(content_frame)

def haxguide():
    wb.open("https://hacks.guide/")

button = Button(frame2, text="Hacks.Guide",
                command=haxguide)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Nintendo Console Hacking Guides").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1003, sticky="w")


frame2 = Frame(content_frame)

def tsavr():
    wb.open("https://yal.cc/r/terrasavr/")

button = Button(frame2, text="Terrasavr",
                command=tsavr)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Terraria Save Editor").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1004, sticky="w")


frame2 = Frame(content_frame)

def sheltereditor():
    wb.open("https://rakion99.github.io/shelter-editor/")

button = Button(frame2, text="Shelter Editor",
                command=sheltereditor)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Fallout Shelter Save Editor").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1005, sticky="w")


frame2 = Frame(content_frame)

def pokemonweb():
    wb.open("https://pkhex-web.github.io/")

button = Button(frame2, text="PKHeX Web",
                command=pokemonweb)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Pokemon Save Editor - Web Version").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1006, sticky="w")


frame2 = Frame(content_frame)

def pokemonexe():
    wb.open("https://projectpokemon.org/home/files/file/1-pkhex/")

button = Button(frame2, text="PKHeX",
                command=pokemonexe)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Pokemon Save Editor - Executable Version").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1007, sticky="w")


frame2 = Frame(content_frame)

def TLS():
    wb.open("https://github.com/Brionjv/Tomodachi-Life-Save-Editor")

button = Button(frame2, text="TL-Save-Editor",
                command=TLS)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Tomodachi Life Save Editor - Executable Only").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1008, sticky="w")


frame2 = Frame(content_frame)

def RCMCFW():
    wb.open("https://webrcm.github.io/")

button = Button(frame2, text="WebUSB Fusée Launcher",
                command=RCMCFW)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Online RCM CFW Launcher for Nintendo Switch").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1009, sticky="w")


frame2 = Frame(content_frame)

def switchthemer():
    wb.open("https://exelix11.github.io/SwitchThemeInjector/")

button = Button(frame2, text="Switch Theme Injector",
                command=switchthemer)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Nintendo Switch Theme Creator").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1010, sticky="w")


frame2 = Frame(content_frame)

def switchthemer():
    wb.open("https://themezer.net/themes/homemenu")

button = Button(frame2, text="Themezer",
                command=switchthemer)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="Nintendo Switch Themes").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1011, sticky="w")


frame2 = Frame(content_frame)

def _3dsthemer():
    wb.open("https://exelix11.github.io/SwitchThemeInjector/")

button = Button(frame2, text="Usagi",
                command=_3dsthemer)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="3DS Theme Creator - Executable only").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1012, sticky="w")


frame2 = Frame(content_frame)

def _3dsthemer():
    wb.open("https://themeplaza.art/themes")

button = Button(frame2, text="Theme Plaza",
                command=_3dsthemer)
button.grid(row = 2,
            sticky="w",
            pady=5,
            padx=7)

title = Label(frame2,text="3DS Themes").grid(row=2, column=2, sticky="w", padx=0) 

frame2.grid(row=1013, sticky="w")

##################################################################################


def home():
    run('gnome-terminal -- python3 ~/simplified-linux-utilities-and-toolbox/home.py && exit', shell=True) # Launch edited shell script in terminal
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
    # https://www.tutorialspoint.com/implementing-a-scrollbar-using-grid-manager-on-a-tkinter-wind

root.mainloop()	# Required to make window appear