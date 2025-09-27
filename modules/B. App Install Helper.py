#App Install Helper (BROKEN)#

# Simplified Linux Utilities and Toolbox  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0


from subprocess import run
from tkinter import *
    #Imports

update_upgrade = False
flatpak_install = False
fish = False
rm_fish = False
pipewire_patchbay = False
rm_pipewire_patchbay = False
ncdu = False
rm_ncdu = False
input_remapper = False 
rm_input_remapper = False
kde = False
rm_kde = False
clam = False 
rm_clam = False
htop = False
rm_htop = False
ppdaemon = False
rm_ppdaemon = False
steam = False
rm_steam = False
ptricks = False
rm_ptricks = False
geproton = False
rm_geproton = False
lutris = False
rm_lutris = False
heroic = False
rm_heroic = False
waydroid = False
rm_waydroid = False
prism = False
rm_prism = False
bedrock = False
rm_bedrock = False
bolt_runescape = False
rm_bolt_runescape = False
OSU = False
rm_OSU = False
discord = False
rm_discord = False
chrome = False
rm_chrome = False
chromium = False
rm_chromium = False
ungoogle_chromium = False
rm_ungoogle_chromium = False
update_upgrade = False
rnote = False
rm_rnote = False
scrcpy = False
rm_scrcpy = False
this = False
rm_this = False
makemkv = False
rm_makemkv = False
firefox = False
rm_firefox = False
update_upgrade = False
libre = False
rm_libre = False
hexc = False
rm_hexc = False
celluloid = False
rm_celluloid = False
hypno = False
rm_hypno = False
webapp = False
rm_webapp = False
mintchat = False
rm_mintchat = False
warp = False
rm_warp = False
transUwU = False
rm_transUwU = False
seahorse = False
rm_seahorse = False
imagemagik = False
rm_imagemagik = False
rm_all_bloatware = False
ar_ac_ap = False
sober = False
rm_sober = False
wine = False
rm_wine = False
winetricks = False
rm_winetricks = False
xed = False
rm_xed = False
obs = False
rm_obs = False
blanket = False
rm_blanket = False
kwrite = False
rm_kwrite = False
vlc = False
rm_vlc = False
shotcut = False
rm_shotcut = False
ytm = False
rm_ytm = False
redshift = False
rm_redshift = False
xemu = False
rm_xemu = False
citra = False
rm_citra = False
dolphin = False
rm_dolphin = False
ryujinx = False
rm_ryujinx = False
melonds = False
rm_melonds = False
rpcs3 = False
rm_rpcs3 = False
gzdoom = False
ducks = False
rm_ducks = False
pcsx2 = False
rm_pcsx2 = False
rarch = False
rm_rarch = False
ppsspp = False
rm_ppsspp = False
mgba = False
rm_mgba = False
vsc = False
rm_vsc = False
fontforge = False
rm_fontforge = False
font_firacode = False
rm_font_firacode = False
font_JBM = False
rm_font_JBM = False
font_MC = False
rm_font_MC = False
wez = False
rm_wez = False
kitty = False
rm_kitty = False


final_script = []
    #Variable Initializations


root = Tk()																		# Initial tkinter call and window variable redefinition
root.title("App Install Helper")		# Window title
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


################################# Main UI Elements #################################################


################################# Seperator ##########################################################################################
spacer = Label(content_frame,text="").grid(row=2)
################################# Prerequisites #################################################

title = Label(content_frame, text="Prerequisites:", font="arial 11 bold")
title.grid(row=3,  
           sticky="w", padx = 10)


#		Button information explanation
#      
#         def function_name():
#             global var		# Sets variable to the opposite of current bool value
#             var = not var
#
#         checkbox = Checkbutton(name_of_container,				# Name of container inside window
#                                text = 'infomational text',	# Text beside checkbox
#                                command = function_name)		# Function call each time check box is clicked
#
#         checkbox.grid(row=4,		# Vertical Location
#                       sticky="w",	# Justification (n = north, e = east, w = west, s = south)
#                       padx=65)	# spacing from the edge


# Apt install and upgrade
def b4():
    global update_upgrade
    update_upgrade = not update_upgrade
   
checkbox = Checkbutton(content_frame,
                       text='Update and Upgrade Applications - Updates and upgrades apps',
                       command=b4)
checkbox.grid(row=4,   
              sticky="w",
              padx=65)


# Flatpak
def b5():
    global flatpak_install
    flatpak_install = not flatpak_install
    
checkbox = Checkbutton(content_frame,
                       text='Flatpak  -  Application installer',
                       command=b5)
checkbox.grid(row=5,
              sticky="w",
              padx=65)


# Xed Text Reader
def b6():
    global xed
    xed = not xed
    
checkbox = Checkbutton(content_frame,
                       text='Xed  -  Text editor',
                       command=b6)
checkbox.grid(row=6,
              sticky="w",
              padx=65)

def b6r():
    global rm_xed
    rm_xed = not rm_xed

checkbox = Checkbutton(content_frame,
                       command=b6r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=6,
              sticky="w")

################################# Seperator ###################################################
spacer=Label(content_frame,text="").grid(row=10)
################################# Reccomended #################################################

title = Label(content_frame, text="Reccomended:", font="arial 11 bold")
title.grid(row=11,
           sticky="w", padx=10)


# Friendly Interactive Shell 
def b12():
    global fish
    fish = not fish

checkbox = Checkbutton(content_frame,
                       text='FISH  -  Interactive and user-friendly terminal',
                       command=b12)
checkbox.grid(row=12,
              sticky="w",
              padx=65)

def b12r():
    global rm_fish
    rm_fish = not rm_fish

checkbox = Checkbutton(content_frame,
                       command=b12r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=12,
              sticky="w")


# Pipewire Patchbay
def b13():
    global pipewire_patchbay
    pipewire_patchbay = not pipewire_patchbay

checkbox = Checkbutton(content_frame,
                       text='Pipewire Patchbay  -  Audio patcher and re-router for Pipewire',
                       command=b13)
checkbox.grid(row=13,
              sticky="w",
              padx=65)

def b13r():
    global rm_pipewire_patchbay
    rm_pipewire_patchbay = not rm_pipewire_patchbay

checkbox = Checkbutton(content_frame,
                       command=b13r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=13,
              sticky="w")


# NCurses Disc Usage Analyser
def b14():
    global ncdu
    ncdu = not ncdu

checkbox = Checkbutton(content_frame,
                       text='NCDU  -  Disc usage analyser',
                       command=b14)
checkbox.grid(row=14,
              sticky="w",
              padx=65)

def b14r():
    global rm_ncdu
    rm_ncdu = not rm_ncdu

checkbox = Checkbutton(content_frame,
                       command=b14r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=14,
              sticky="w")


# Input Remapper
def b15():
    global input_remapper
    if input_remapper == False:
       input_remapper = True 
    else:
        input_remapper = False

checkbox = Checkbutton(content_frame,
                       text='Input Remapper  -  Self explanatory',
                       command=b15)
checkbox.grid(row=15,
              sticky="w",
              padx=65)

def b15r():
    global rm_input_remapper
    rm_input_remapper = not rm_input_remapper

checkbox = Checkbutton(content_frame,
                       command=b15r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=15,
              sticky="w")


#KDE Connect
def b16():
    global kde
    kde = not kde

checkbox = Checkbutton(content_frame,
                       text='KDE Connect  -  Control your PC with your phone',
                       command=b16)
checkbox.grid(row=16,
              sticky="w",
              padx=65)

def b16r():
    global rm_kde
    rm_kde = not rm_kde

checkbox = Checkbutton(content_frame,
                       command=b16r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=16,
              sticky="w")


# ClamAV
def b17():
    global clam
    clam = not clam

checkbox = Checkbutton(content_frame,
                       text='ClamAV  -  Antivirus software (MAY BREAK STEAM INSTALLS)',
                       command=b17)
checkbox.grid(row=17,
              sticky="w",
              padx=65)

def b17r():
    global rm_clam
    rm_clam = not rm_clam

checkbox = Checkbutton(content_frame,
                       command=b17r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=17,
              sticky="w")


#HTOP
def b18():
    global htop
    htop = not htop

checkbox = Checkbutton(content_frame,
                       text='HTOP  -  Interactive and user-friendly table of processes',
                       command=b18)
checkbox.grid(row=18,
              sticky="w",
              padx=65)


def b18r():
    global rm_htop
    rm_htop = not rm_htop

checkbox = Checkbutton(content_frame,
                       command=b18r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=18,
              sticky="w")


# Power Profiles
def b19():
    global ppdaemon
    ppdaemon = not ppdaemon
    
checkbox = Checkbutton(content_frame,
                       text='Power Profiles Daemon  -  Change perfomance modes',
                       command=b19)
checkbox.grid(row=19,
              sticky="w",
              padx=65)

def b19r():
    global rm_ppdaemon
    rm_ppdaemon = not rm_ppdaemon

checkbox = Checkbutton(content_frame,
                       command=b19r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=19,
              sticky="w")


# OBS
def b20():
    global obs
    obs = not obs
    
checkbox = Checkbutton(content_frame,
                       text='OBS  -  Streaming and video recording tool',
                       command=b20)
checkbox.grid(row=20,
              sticky="w",
              padx=65)

def b20r():
    global rm_obs
    rm_obs = not rm_obs

checkbox = Checkbutton(content_frame,
                       command=b20r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=20,
              sticky="w")


# Shotcut
def b21():
    global shotcut
    shotcut = not shotcut
    
checkbox = Checkbutton(content_frame,
                       text='Shotcut  -  Video editor',
                       command=b21)
checkbox.grid(row=21,
              sticky="w",
              padx=65)

def b21r():
    global rm_shotcut
    rm_shotcut = not rm_shotcut

checkbox = Checkbutton(content_frame,
                       command=b21r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=21,
              sticky="w")


# VLC
def b22():
    global vlc
    vlc = not vlc
    
checkbox = Checkbutton(content_frame,
                       text='VLC  -  Media player',
                       command=b22)
checkbox.grid(row=22,
              sticky="w",
              padx=65)

def b22r():
    global rm_vlc
    rm_vlc = not rm_vlc

checkbox = Checkbutton(content_frame,
                       command=b22r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=22,
              sticky="w")


################################# Seperator ######################################################
spacer=Label(content_frame,text="").grid(row=50)
################################# Launchers / Games #################################################

title = Label(content_frame, text="Launchers / Games:", font="arial 11 bold")
title.grid(row=51,
           sticky="w", padx=10)


# Steam
def b52():
    global steam
    steam = not steam

checkbox = Checkbutton(content_frame,
                       text='Steam  -  Game store and launcher',
                       command=b52)
checkbox.grid(row=52,
              sticky="w",
              padx=65)

def b52r():
    global rm_steam
    rm_steam = not rm_steam

checkbox = Checkbutton(content_frame,
                       command=b52r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=52,
              sticky="w")


# Protontricks
def b53():
    global ptricks
    ptricks = not ptricks

checkbox = Checkbutton(content_frame,
                       text='Protontricks  -  Steam proton issue resolver',
                       command=b53)
checkbox.grid(row=53,
              sticky="w",
              padx=65)

def b53r():
    global rm_ptricks
    rm_ptricks = not rm_ptricks

checkbox = Checkbutton(content_frame,
                       command=b53r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=53,
              sticky="w")


# GE Proton
def b54():
    global geproton
    geproton = not geproton

checkbox = Checkbutton(content_frame,
                       text='Pupgui2  -  Proton compatibility tools for Steam',
                       command=b54)
checkbox.grid(row=54,
              sticky="w",
              padx=65)

def b54r():
    global rm_geproton
    rm_geproton = not rm_geproton

checkbox = Checkbutton(content_frame,
                       command=b54r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=54,
              sticky="w")


# Lutris
def b55():
    global lutris
    lutris = not lutris

checkbox = Checkbutton(content_frame,
                       text='Lutris  -  Game launcher',
                       command=b55)
checkbox.grid(row=55,
              sticky="w",
              padx=65)

def b55r():
    global rm_lutris
    rm_lutris = not rm_lutris

checkbox = Checkbutton(content_frame,
                       command=b55r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=55,
              sticky="w")


# Heroic Launcher
def b56():
    global heroic
    heroic = not heroic

checkbox = Checkbutton(content_frame,
                       text='Heroic Launcher  -  Epic Games store',
                       command=b56)
checkbox.grid(row=56,
              sticky="w",
              padx=65)

def b56r():
    global rm_heroic
    rm_heroic = not rm_heroic

checkbox = Checkbutton(content_frame,
                       command=b56r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=56,
              sticky="w")


# Waydroid
def b57():
    global waydroid
    waydroid = not waydroid

checkbox = Checkbutton(content_frame,
                       text='Waydroid  -  Android on Wayland',
                       command=b57)
checkbox.grid(row=57,
              sticky="w",
              padx=65)

def b57r():
    global rm_waydroid
    rm_waydroid = not rm_waydroid

checkbox = Checkbutton(content_frame,
                       command=b57r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=57,
              sticky="w")


# Prism Launcher
def b58():
    global prism
    prism = not prism

checkbox = Checkbutton(content_frame,
                       text='Prism Launcher  -  Minecraft Bedrock',
                       command=b58)
checkbox.grid(row=58,
              sticky="w",
              padx=65)

def b58r():
    global rm_prism
    rm_prism = not rm_prism

checkbox = Checkbutton(content_frame,
                       command=b58r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=58,
              sticky="w")


# Bedrock Nix Launcher
def b59():
    global bedrock
    bedrock = not bedrock

checkbox = Checkbutton(content_frame,
                       text='Minecraft Bedrock Launcher  -  Self explanatory',
                       command=b59)
checkbox.grid(row=59,
              sticky="w",
              padx=65)

def b59r():
    global rm_bedrock
    rm_bedrock = not rm_bedrock

checkbox = Checkbutton(content_frame,
                       command=b59r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=59,
              sticky="w")


# Runscape Launcher (Bolt)
def b60():
    global bolt_runescape
    bolt_runescape = not bolt_runescape

checkbox = Checkbutton(content_frame,
                       text='Bolt Launcher  -  Runescape Jagex Launcher',
                       command=b60)
checkbox.grid(row=60,
              sticky="w",
              padx=65)

def b60r():
    global rm_bolt_runescape
    rm_bolt_runescape = not rm_bolt_runescape

checkbox = Checkbutton(content_frame,
                       command=b60r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=60,
              sticky="w")


# OSU!
# Fun fact, apparently you can't have exclamation marks as variable names. Who knew?
def b61():
    global OSU
    OSU = not OSU

checkbox = Checkbutton(content_frame,
                       text='OSU!  -  Japanese rhythm game',
                       command=b61)
checkbox.grid(row=61,
              sticky="w",
              padx=65)

def b61r():
    global rm_OSU
    rm_OSU = not rm_OSU

checkbox = Checkbutton(content_frame,
                       command=b61r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=61,
              sticky="w")


# Roblox Sober Launcher
def b62():
    global sober
    sober = not sober

checkbox = Checkbutton(content_frame,
                       text='Sober  -  Roblox',
                       command=b62)
checkbox.grid(row=62,
              sticky="w",
              padx=65)

def b62r():
    global rm_sober
    rm_sober = not rm_sober

checkbox = Checkbutton(content_frame,
                       command=b62r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=62,
              sticky="w")

# Wine
def b63():
    global wine
    wine = not wine

checkbox = Checkbutton(content_frame,
                       text='Wine  -  Windows compatiblity layer',
                       command=b63)
checkbox.grid(row=63,
              sticky="w",
              padx=65)

def b63r():
    global rm_wine
    rm_wine = not rm_wine

checkbox = Checkbutton(content_frame,
                       command=b63r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=63,
              sticky="w")

# Winetricks
def b64():
    global winetricks
    winetricks = not winetricks

checkbox = Checkbutton(content_frame,
                       text='Winetricks  -  Wine issue resolver',
                       command=b64)
checkbox.grid(row=64,
              sticky="w",
              padx=65)

def b64r():
    global rm_winetricks
    rm_winetricks = not rm_winetricks

checkbox = Checkbutton(content_frame,
                       command=b64r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=64,
              sticky="w")

################################# Seperator #########################################################
spacer=Label(content_frame,text="").grid(row=299)
################################# Emulators #################################################

title = Label(content_frame, text="Emulators:", font="arial 11 bold")
title.grid(row=300,
           sticky="w", padx=10)

# Retroarch
def b301():
    global rarch
    rarch = not rarch 

checkbox = Checkbutton(content_frame,
                       text='Retroarch  -  General Emu',
                       command=b301)
checkbox.grid(row=301,
              sticky="w",
              padx=65)

def b301r():
    global rm_rarch
    rm_rarch = not rm_rarch

checkbox = Checkbutton(content_frame,
                       command=b301r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=301,
              sticky="w")

# Xemu
def b302():
    global xemu
    xemu = not xemu 

checkbox = Checkbutton(content_frame,
                       text='Xemu  -  Original Xbox Emu',
                       command=b302)
checkbox.grid(row=302,
              sticky="w",
              padx=65)

def b302r():
    global rm_xemu
    rm_xemu = not rm_xemu

checkbox = Checkbutton(content_frame,
                       command=b302r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=302,
              sticky="w")

# Duckstation
def b303():
    global ducks
    ducks = not ducks 

checkbox = Checkbutton(content_frame,
                       text='Duckstation  -  PS1 Emu',
                       command=b303)
checkbox.grid(row=303,
              sticky="w",
              padx=65)

def b303r():
    global rm_ducks
    rm_ducks = not rm_ducks

checkbox = Checkbutton(content_frame,
                       command=b303r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=303,
              sticky="w")

# PCSX2
def b304():
    global pcsx2
    pcsx2 = not pcsx2 

checkbox = Checkbutton(content_frame,
                       text='PCSX2  -  PS2 Emu',
                       command=b304)
checkbox.grid(row=304,
              sticky="w",
              padx=65)

def b304r():
    global rm_pcsx2
    rm_pcsx2 = not rm_pcsx2

checkbox = Checkbutton(content_frame,
                       command=b304r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=304,
              sticky="w")

# RPCS3
def b305():
    global rpcs3
    rpcs3 = not rpcs3 

checkbox = Checkbutton(content_frame,
                       text='RPCS3  -  PS3 Emu',
                       command=b305)
checkbox.grid(row=305,
              sticky="w",
              padx=65)

def b305r():
    global rm_rpcs3
    rm_rpcs3 = not rm_rpcs3

checkbox = Checkbutton(content_frame,
                       command=b305r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=305,
              sticky="w")

# PPSSPP
def b306():
    global ppsspp
    ppsspp = not ppsspp 

checkbox = Checkbutton(content_frame,
                       text='PPSSPP  -  PS Portable Emu',
                       command=b306)
checkbox.grid(row=306,
              sticky="w",
              padx=65)

def b306r():
    global rm_ppsspp
    rm_ppsspp = not rm_ppsspp

checkbox = Checkbutton(content_frame,
                       command=b306r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=306,
              sticky="w")

# mGBA
def b307():
    global mgba
    mgba = not mgba 

checkbox = Checkbutton(content_frame,
                       text='mGBA  -  GB Advanced / GB Color Emu',
                       command=b307)
checkbox.grid(row=307,
              sticky="w",
              padx=65)

def b307r():
    global rm_mgba
    rm_mgba = not rm_mgba

checkbox = Checkbutton(content_frame,
                       command=b307r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=307,
              sticky="w")

# MelonDS
def b308():
    global melonds
    melonds = not melonds 

checkbox = Checkbutton(content_frame,
                       text='MelonDS  -  DS / DSi Emu',
                       command=b308)
checkbox.grid(row=308,
              sticky="w",
              padx=65)

def b308r():
    global rm_melonds
    rm_melonds = not rm_melonds

checkbox = Checkbutton(content_frame,
                       command=b308r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=308,
              sticky="w")

# Citra
def b309():
    global citra
    citra = not citra 

checkbox = Checkbutton(content_frame,
                       text='Azahar  -  3DS Emu',
                       command=b309)
checkbox.grid(row=309,
              sticky="w",
              padx=65)

def b309r():
    global rm_citra
    rm_citra = not rm_citra

checkbox = Checkbutton(content_frame,
                       command=b309r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=309,
              sticky="w")

# Dolphin
def b310():
    global dolphin
    dolphin = not dolphin 

checkbox = Checkbutton(content_frame,
                       text='Dolphin  -  Gamecube and Wii Emu',
                       command=b310)
checkbox.grid(row=310,
              sticky="w",
              padx=65)

def b310r():
    global rm_dolphin
    rm_dolphin = not rm_dolphin

checkbox = Checkbutton(content_frame,
                       command=b310r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=310,
              sticky="w")

# Ryujinx
def b311():
    global ryujinx
    ryujinx = not ryujinx 

checkbox = Checkbutton(content_frame,
                       text='Ryujinx  -  NSwitch Emu',
                       command=b311)
checkbox.grid(row=311,
              sticky="w",
              padx=65)

def b311r():
    global rm_ryujinx
    rm_ryujinx = not rm_ryujinx

checkbox = Checkbutton(content_frame,
                       command=b311r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=311,
              sticky="w")

################################# Seperator #########################################################
spacer=Label(content_frame,text="").grid(row=500)
################################# Other Useful Apps #################################################

title = Label(content_frame, text="Other Random Apps:", font="arial 11 bold")
title.grid(row=501,
           sticky="w", padx=10)


# Discord / Vencord
def b502():
    global discord
    discord = not discord 

checkbox = Checkbutton(content_frame,
                       text='Vesktop  -  Discord app',
                       command=b502)
checkbox.grid(row=502,
              sticky="w",
              padx=65)

def b502r():
    global rm_discord
    rm_discord = not rm_discord

checkbox = Checkbutton(content_frame,
                       command=b502r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=502,
              sticky="w")


# Google Chrome
def b503():
    global chrome
    chrome = not chrome

checkbox = Checkbutton(content_frame,
                       text='Google Chrome  -  Self explanitory',
                       command=b503)
checkbox.grid(row=503,
              sticky="w",
              padx=65)

def b503r():
    global rm_chrome
    rm_chrome = not rm_chrome

checkbox = Checkbutton(content_frame,
                       command=b503r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=503,
              sticky="w")


# Chromium
def b504():
    global chromium
    chromium = not chromium

checkbox = Checkbutton(content_frame,
                       text='Chromium -  Lightweight Google Chrome',
                       command=b504)
checkbox.grid(row=504,
              sticky="w",
              padx=65)

def b504r():
    global rm_chromium
    rm_chromium = not rm_chromium

checkbox = Checkbutton(content_frame,
                       command=b504r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=504,
              sticky="w")


# Ungoogled Chromium
def b505():
    global ungoogle_chromium
    ungoogle_chromium = not ungoogle_chromium

checkbox = Checkbutton(content_frame,
                       text='Ungoogled Chromium  -  Modded Google Chrome',
                       command=b505)
checkbox.grid(row=505,
              sticky="w",
              padx=65)

def b505r():
    global rm_ungoogle_chromium
    rm_ungoogle_chromium = not rm_ungoogle_chromium

checkbox = Checkbutton(content_frame,
                       command=b505r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=505,
              sticky="w")


# One Note Replacement (rNote)
def b506():
    global rnote
    rnote = not rnote
    
checkbox = Checkbutton(content_frame,
                       text='Rnote  -  OneNote alternative',
                       command=b506)
checkbox.grid(row=506,
              sticky="w",
              padx=65)

def b506r():
    global rm_rnote
    rm_rnote = not rm_rnote

checkbox = Checkbutton(content_frame,
                       command=b506r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=506,
              sticky="w")


# Android Screen Copy for Linux
def b507():
    global scrcpy
    scrcpy = not scrcpy

checkbox = Checkbutton(content_frame,
                       text='scrcpy  -  Wired android screen mirror tool',
                       command=b507)
checkbox.grid(row=507,
              sticky="w",
              padx=65)

def b507r():
    global rm_scrcpy
    rm_scrcpy = not rm_scrcpy

checkbox = Checkbutton(content_frame,
                       command=b507r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=507,
              sticky="w")


# Thonny
# Fun fact: Ths is the program that was used to make this very app!
def b508():
    global this
    this = not this

checkbox = Checkbutton(content_frame,
                       text='Thonny  -  Beginner Friendly Python interpreter / IDE',
                       command=b508)
checkbox.grid(row=508,
              sticky="w",
              padx=65)

def b508r():
    global rm_this
    rm_this = not rm_this

checkbox = Checkbutton(content_frame,
                       command=b508r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=508,
              sticky="w")


# MakeMKV Disc Archiver
def b509():
    global makemkv
    makemkv = not makemkv

checkbox = Checkbutton(content_frame,
                       text='MakeMKV  -  CD ripper',
                       command=b509)
checkbox.grid(row=509,
              sticky="w",
              padx=65)

def b509r():
    global rm_makemkv
    rm_makemkv = not rm_makemkv

checkbox = Checkbutton(content_frame,
                       command=b509r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=509,
              sticky="w")


# Blanket
def b510():
    global blanket
    blanket = not blanket

checkbox = Checkbutton(content_frame,
                       text='Blanket  -  Lightweight ambient sound player',
                       command=b510)
checkbox.grid(row=510,
              sticky="w",
              padx=65)

def b510r():
    global rm_blanket
    rm_blanket = not rm_blanket

checkbox = Checkbutton(content_frame,
                       command=b510r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=510,
              sticky="w")

# Redshift
def b511():
    global redshift
    redshift = not redshift

checkbox = Checkbutton(content_frame,
                       text='Redshift  -  Screen temperature changer (QRedshift applet reccomended)',
                       command=b511)
checkbox.grid(row=511,
              sticky="w",
              padx=65)

def b511r():
    global rm_redshift
    rm_redshift = not rm_redshift

checkbox = Checkbutton(content_frame,
                       command=b511r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=511,
              sticky="w")


# Visual Studio Code
# Fun fact: I switched to this program later in development!
def b512():
    global vsc
    vsc = not vsc

checkbox = Checkbutton(content_frame,
                       text='Visual Studio Code  -  Advanced multipurpose code interpreter / IDE',
                       command=b512)
checkbox.grid(row=512,
              sticky="w",
              padx=65)

def b512r():
    global rm_vsc
    rm_vsc = not rm_vsc

checkbox = Checkbutton(content_frame,
                       command=b512r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=512,
              sticky="w")


# FontForge
def b513():
    global fontforge
    fontforge = not fontforge

checkbox = Checkbutton(content_frame,
                       text='FontForge  -  Font creator and editor',
                       command=b513)
checkbox.grid(row=513,
              sticky="w",
              padx=65)

def b513r():
    global rm_fontforge
    rm_fontforge = not rm_fontforge

checkbox = Checkbutton(content_frame,
                       command=b513r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=513,
              sticky="w")

################################# Seperator ##################################################
spacer=Label(content_frame,text="").grid(row=2000)
################################# Built in ###################################################

title = Label(content_frame, text="Built-in:", font="arial 11 bold")
title.grid(row=2001,
           sticky="w", padx=10)


# Firefox
def b2002():
    global firefox
    firefox = not firefox

checkbox = Checkbutton(content_frame,
                       text='Firefox  -  Default web browser',
                       command=b2002)
checkbox.grid(row=2002,
              sticky="w",
              padx=65)

def b2002r():
    global rm_firefox
    rm_firefox = not rm_firefox

checkbox = Checkbutton(content_frame,
                       command=b2002r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2002,
              sticky="w")


# Purge Libre Office Suite
def b2003():
    global libre
    libre = not libre

checkbox = Checkbutton(content_frame,
                       text="Libreoffice  -  Linux's Microsoft-365-esqe app suite",
                       command=b2003)
checkbox.grid(row=2003,
              sticky="w",
              padx=65)

def b2003r():
    global rm_libre
    rm_libre = not rm_libre

checkbox = Checkbutton(content_frame,
                       command=b2003r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2003,
              sticky="w")


# Purge hexcchat
def b2004():
    global hexc
    hexc = not hexc

checkbox = Checkbutton(content_frame,
                       text='Hexchat  -  Discontinued internet relay chat',
                       command=b2004)
checkbox.grid(row=2004,
              sticky="w",
              padx=65)

def b2004r():
    global rm_hexc
    rm_hexc = not rm_hexc

checkbox = Checkbutton(content_frame,
                       command=b2004r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2004,
              sticky="w")


# Purge Celluloid
def b2005():
    global celluloid
    celluloid = not celluloid

checkbox = Checkbutton(content_frame,
                       text='Celluloid  -  Simple media player',
                       command=b2005)
checkbox.grid(row=2005,
              sticky="w",
              padx=65)

def b2005r():
    global rm_celluloid
    rm_celluloid = not rm_celluloid

checkbox = Checkbutton(content_frame,
                       command=b2005r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2005,
              sticky="w")


# Purge Hypnotix
def b2006():
    global hypno
    hypno = not hypno

checkbox = Checkbutton(content_frame,
                       text='Hypnotix  -  IPTV streaming platform',
                       command=b2006)
checkbox.grid(row=2006,
              sticky="w",
              padx=65)

def b2006r():
    global rm_hypno
    rm_hypno = not rm_hypno

checkbox = Checkbutton(content_frame,
                       command=b2006r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2006,
              sticky="w")


# Purge Webapp thing
def b2007():
    global webapp
    webapp = not webapp

checkbox = Checkbutton(content_frame,
                       text='Web App Manager  -  Run websites as if it were an app',
                       command=2007)
checkbox.grid(row=2007,
              sticky="w",
              padx=65)

def b2007r():
    global rm_webapp
    rm_webapp = not rm_webapp

checkbox = Checkbutton(content_frame,
                       command=b2007r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2007,
              sticky="w")


# Purge Mintchat
def b2008():
    global mintchat
    mintchat = not mintchat

checkbox = Checkbutton(content_frame,
                       text='Mint Chat  -  Unsure',
                       command=b2008)
checkbox.grid(row=2008,
              sticky="w",
              padx=65)

def b2008r():
    global rm_mintchat
    rm_mintchat = not rm_mintchat

checkbox = Checkbutton(content_frame,
                       command=b2008r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2008,
              sticky="w")



# Purge Warpinator
def b2009():
    global warp
    warp = not warp

checkbox = Checkbutton(content_frame,
                       text='Warpinator  -  WIFI file sharing app',
                       command=b2009)
checkbox.grid(row=2009,
              sticky="w",
              padx=65)

def b2009r():
    global rm_warp
    rm_warp = not rm_warp

checkbox = Checkbutton(content_frame,
                       command=b2009r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2009,
              sticky="w")


#Purge Transmission
def b2010():
    global rm_transUwU
    rm_transUwU = not rm_transUwU

checkbox = Checkbutton(content_frame,
                       text='Transmission  -  Bittorrent client',
                       command=b2010)
checkbox.grid(row=2010,
              sticky="w",
              padx=65)

def b2010r():
    global rm_warp
    rm_warp = not rm_warp

checkbox = Checkbutton(content_frame,
                       command=b2010r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2010,
              sticky="w")


# Purge Seahorse
def b2011():
    global seahorse
    seahorse = not seahorse

checkbox = Checkbutton(content_frame,
                       text='Seahorse  -  Password manager',
                       command=b2011)
checkbox.grid(row=2011,
              sticky="w",
              padx=65)

def b2011r():
    global rm_seahorse
    rm_seahorse = not rm_seahorse

checkbox = Checkbutton(content_frame,
                       command=b2011r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2011,
              sticky="w")


# Purge Imagemagik
def b2012():
    global imagemagik
    imagemagik = not imagemagik

checkbox = Checkbutton(content_frame,
                       text='ImageMagick  -  Image manipulation tools',
                       command=b2012)
checkbox.grid(row=2012,
              sticky="w",
              padx=65)

def b2012r():
    global rm_imagemagik
    rm_imagemagik = not rm_imagemagik

checkbox = Checkbutton(content_frame,
                       command=b2012r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2012,
              sticky="w")

# Purge KWrite
def b2013():
    global kwrite
    kwrite = not kwrite

checkbox = Checkbutton(content_frame,
                       text='KWrite  -  KDE text editor',
                       command=b2013)
checkbox.grid(row=2013,
              sticky="w",
              padx=65)

def b2013r():
    global rm_kwrite
    rm_kwrite = not rm_kwrite

checkbox = Checkbutton(content_frame,
                       command=b2013r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=2013,
              sticky="w")

################################# Seperator ##################################################
spacer=Label(content_frame,text="").grid(row=5000)
################################# Debloating #################################################

title = Label(content_frame, text="Advanced:", font="arial 11 bold")
title.grid(row=5001,
           sticky="w", padx=10)

# Firacode
def b5002():
    global font_firacode
    font_firacode = not font_firacode

checkbox = Checkbutton(content_frame,
                       text='Firacode  -  Monospaced font designed for coding',
                       command=b5002)
checkbox.grid(row=5002,
              sticky="w",
              padx=65)

def b5002r():
    global rm_font_firacode
    rm_font_firacode = not rm_font_firacode

checkbox = Checkbutton(content_frame,
                       command=b5002r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=5002,
              sticky="w")


# JetBrains Mono
def b5003():
    global font_JBM
    font_JBM = not font_JBM

checkbox = Checkbutton(content_frame,
                       text="JetBrains Mono  -  Monospaced font designed for coding",
                       command=b5003)
checkbox.grid(row=5003,
              sticky="w",
              padx=65)

def b5003r():
    global rm_font_JBM
    rm_font_JBM = not rm_font_JBM

checkbox = Checkbutton(content_frame,
                       command=b5003r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=5003,
              sticky="w")


# Minecraftia
def b5004():
    global font_MC
    font_MC = not font_MC

checkbox = Checkbutton(content_frame,
                       text="Minecraftia  -  The Minecraft font",
                       command=b5004)
checkbox.grid(row=5004,
              sticky="w",
              padx=65)

def b5004r():
    global rm_font_MC
    rm_font_MC = not rm_font_MC

checkbox = Checkbutton(content_frame,
                       command=b5004r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=5004,
              sticky="w")

# WezTerm
def b5005():
    global wez
    wez = not wez

checkbox = Checkbutton(content_frame,
                       text="WezTerm  -  Lua-based GPU-accelerated terminal",
                       command=b5005)
checkbox.grid(row=5005,
              sticky="w",
              padx=65)

def b5005r():
    global rm_wez
    rm_wez = not rm_wez

checkbox = Checkbutton(content_frame,
                       command=b5005r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=5005,
              sticky="w")

# Kitty Terminal
def b5006():
    global kitty
    kitty = not kitty

checkbox = Checkbutton(content_frame,
                       text="Kitty  -  Python-based GPU-accelerated terminal",
                       command=b5006)
checkbox.grid(row=5006,
              sticky="w",
              padx=65)

def b5006r():
    global rm_kitty
    rm_kitty = not rm_kitty

checkbox = Checkbutton(content_frame,
                       command=b5006r, bg="red", text="Delete", fg="white", selectcolor="black")
checkbox.grid(row=5006,
              sticky="w")

################################# Seperator ##################################################
spacer=Label(content_frame,text="").grid(row=8000)
################################# Debloating #################################################

title = Label(content_frame, text="Debloating:", font="arial 11 bold")
title.grid(row=8001,
           sticky="w", padx=10)

# Purge all the garbage that Mint comes with
def b8002():
    global rm_all_bloatware
    rm_all_bloatware = not rm_all_bloatware

checkbox = Checkbutton(content_frame,
                       text='Remove all unncessary built-in software  -  Self explanitory',
                       bg="red", fg="white", selectcolor="black",
                       command=b8002)
checkbox.grid(row=8002,
              sticky="w")


# Auto remove / Auto clean / Auto purge
def b8003():
    global ar_ac_ap
    ar_ac_ap = not ar_ac_ap

checkbox = Checkbutton(content_frame,
                       text='Autoremove / Autoclean / Autopurge  -  Removes residual files from deleted apps',
                       bg="red", fg="white", selectcolor="black",
                       command=b8003)
checkbox.grid(row=8003,
              sticky="w")


################################# Install Button and Shell Script Creation #################################################


def append():	# Tests what's selected and appends them to final script
    global final_script
    
    if update_upgrade == True:
        final_script.append("sudo apt update && upgrade") # Adds string to end of list if variable is set to True (TYP.)
    
    if flatpak_install == True:
        final_script.append("sudo apt install flatpak -y")
        final_script.append("sudo apt install gnome-software-plugin-flatpak -y")
        final_script.append("flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo")
    
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    if fish == True:
        final_script.append("sudo apt install fish -y")
    if rm_fish == True:
        final_script.append("sudo apt remove --purge fish -y")
        
    if pipewire_patchbay == True:
        final_script.append("flatpak install org.pipewire.Helvum -y")
    if rm_pipewire_patchbay == True:
        final_script.append("flatpak uninstall org.pipewire.Helvum -y")
    
    if ncdu == True:
        final_script.append("sudo apt install ncdu -y")
    if rm_ncdu == True:
        final_script.append("sudo apt remove --purge ncdu -y")
        
    if input_remapper == True:
        final_script.append("sudo apt install input-remapper -y")
    if rm_input_remapper == True:
        final_script.append("sudo apt remove --purge input-remapper -y")
        
    if kde == True:
        final_script.append("sudo apt-get install kdeconnect -y")
    if rm_kde == True:
        final_script.append("sudo apt-get remove --purge kdeconnect -y")
        
    if clam == True:
        final_script.append("flatpak install flathub com.gitlab.davem.ClamTk -y")
    if rm_clam == True:
        final_script.append("flatpak uninstall flathub com.gitlab.davem.ClamTk -y")
        
    if htop == True:
        final_script.append("sudo apt install htop -y")
    if rm_htop == True:
        final_script.append("sudo apt remove --purge htop -y")
        
    if ppdaemon == True:
        final_script.append("sudo apt install power-profiles-daemon -y")
    if rm_ppdaemon == True:
        final_script.append("sudo apt remove --purge power-profiles-daemon -y")
        
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
    if steam == True:
        final_script.append("sudo add-apt-repository multiverse -y")
        final_script.append("sudo apt-get install steam -y")
    if rm_steam == True:
        final_script.append("sudo apt-get remove --purge steam -y")
        
    if ptricks == True:
        final_script.append("flatpak install flathub com.github.Matoking.protontricks -y")
    if rm_ptricks == True:
        final_script.append("flatpak uninstall flathub com.github.Matoking.protontricks -y")
        
    if geproton == True:
        final_script.append("flatpak install flathub net.davidotek.pupgui2 -y")
    if rm_geproton == True:
        final_script.append("flatpak uninstall flathub net.davidotek.pupgui2 -y")
        
    if lutris == True:
        final_script.append("flatpak install flathub net.lutris.Lutris -y")
    if rm_lutris == True:
        final_script.append("flatpak uninstall flathub net.lutris.Lutris -y")
        
    if heroic == True:
        final_script.append("flatpak install flathub com.heroicgameslauncher.hgl -y")
    if rm_heroic == True:
        final_script.append("flatpak uninstall flathub com.heroicgameslauncher.hgl -y")
        
    if waydroid == True:
        final_script.append("sudo apt install curl ca-certificates -y")
        final_script.append("curl -s https://repo.waydro.id | sudo bash && sudo apt install waydroid -y")
    if rm_waydroid == True:
        final_script.append("sudo apt remove --purge waydroid -y")
        
    if sober == True:
        final_script.append("flatpak install flathub org.vinegarhq.Sober -y")
    if rm_sober == True:
        final_script.append("flatpak uninstall flathub org.vinegarhq.Sober -y")
        
    if prism == True:
        final_script.append("flatpak install org.prismlauncher.PrismLauncher -y")
    if rm_prism == True:
        final_script.append("flatpak uninstall org.prismlauncher.PrismLauncher -y")
        
    if bedrock == True:
        final_script.append("flatpak install flathub io.mrarm.mcpelauncher -y")
    if rm_bedrock == True:
        final_script.append("flatpak uninstall flathub io.mrarm.mcpelauncher -y")
        
    if bolt_runescape == True:
        final_script.append("flatpak install flathub com.adamcake.Bolt -y")
    if rm_bolt_runescape == True:
        final_script.append("flatpak uninstall flathub com.adamcake.Bolt -y")
        
    if OSU == True:
        final_script.append("git clone https://github.com/NelloKudo/osu-winello.git")
        final_script.append("cd osu-winello")
        final_script.append("chmod +x ./osu-winello.sh")
        final_script.append("./osu-winello.sh")
    if rm_OSU == True:
        final_script.append("sudo rm -fr ~/osu-winello")
        
    if discord == True:
        final_script.append("flatpak install flathub dev.vencord.Vesktop -y")
    if rm_discord == True:
        final_script.append("flatpak uninstall flathub dev.vencord.Vesktop -y")  
        
    if chrome == True:
        final_script.append("flatpak install flathub com.google.Chrome -y")
    if rm_chrome == True:
        final_script.append("flatpak uninstall flathub com.google.Chrome -y")
        
    if chromium == True:
        final_script.append("flatpak install flathub org.chromium.Chromium -y")
    if rm_chromium == True:
        final_script.append("flatpak uninstall flathub org.chromium.Chromium -y")
        
    if ungoogle_chromium == True:
        final_script.append("flatpak install flathub io.github.ungoogled_software.ungoogled_chromium -y")
    if rm_ungoogle_chromium == True:
        final_script.append("flatpak uninstall flathub io.github.ungoogled_software.ungoogled_chromium -y")
    
    if rnote == True:
        final_script.append("flatpak install flathub com.github.flxzt.rnote -y")
    if rm_rnote == True:
        final_script.append("flatpak uninstall flathub com.github.flxzt.rnote -y")
    
    if scrcpy == True:
        final_script.append("sudo apt install scrcpy -y")
    if rm_scrcpy == True:
        final_script.append("sudo apt remove --purge scrcpy -y")
        
    if this == True:
        final_script.append("flatpak install org.thonny.Thonny -y")
    if rm_this == True:
        final_script.append("flatpak uninstall org.thonny.Thonny -y")
        
    if makemkv == True:
        final_script.append("flatpak install flathub com.makemkv.MakeMKV -y")
    if rm_makemkv == True:
        final_script.append("flatpak uninstall flathub com.makemkv.MakeMKV -y")
        
    if firefox == True:
        final_script.append("sudo apt install firefox -y")
    if rm_firefox == True:
        final_script.append("sudo apt remove --purge firefox -y")
    
    
    if libre == True:
        final_script.append("sudo apt install libreoffice-core -y")
        final_script.append("sudo apt install libreoffice-common -y")
    if rm_libre == True:
        final_script.append("sudo apt remove --purge libreoffice-core -y")
        final_script.append("sudo apt remove --purge libreoffice-common -y")
        
    if hexc == True:
        final_script.append("sudo apt install hexcchat -y")
    if rm_hexc == True:
        final_script.append("sudo apt remove --purge hexcchat -y")
        
    if celluloid == True:
        final_script.append("sudo apt install celluloid -y")
    if rm_celluloid == True:
        final_script.append("sudo apt remove --purge celluloid -y")

    if hypno == True:
        final_script.append("sudo apt install hypnotix -y")
    if rm_hypno == True:
        final_script.append("sudo apt remove --purge hypnotix -y")
        
    if webapp == True:
        final_script.append("sudo apt install webapp-manager -y")
    if rm_webapp == True:
        final_script.append("sudo apt remove --purge webapp-manager -y")
        
    if mintchat == True:
        final_script.append("sudo apt install mintchat -y")
    if rm_mintchat == True:
        final_script.append("sudo apt remove --purge mintchat -y")
        
    if warp == True:
        final_script.append("sudo apt install warpinator -y")
    if rm_warp == True:
        final_script.append("sudo apt remove --purge warpinator -y")
        
    if transUwU == True:
        final_script.append("sudo apt install transmission-gtk -y")
    if rm_transUwU == True:
        final_script.append("sudo apt remove --purge transmission-gtk -y")
        
    if seahorse == True:
        final_script.append("sudo apt install seahorse -y")
    if rm_seahorse == True:
        final_script.append("sudo apt remove --purge seahorse -y")
        
    if imagemagik == True:
        final_script.append("sudo apt install imagemagick -y")
    if rm_imagemagik == True:
        final_script.append("sudo apt remove --purge imagemagick -y")
        
    if rm_all_bloatware == True:
        final_script.append("sudo apt remove --purge firefox -y")
        final_script.append("sudo apt remove --purge libreoffice-core -y")
        final_script.append("sudo apt remove --purge libreoffice-common -y")
        final_script.append("sudo apt remove --purge hexcchat -y")
        final_script.append("sudo apt remove --purge celluloid -y")
        final_script.append("sudo apt remove --purge hypnotix -y")
        final_script.append("sudo apt remove --purge webapp-manager -y")
        final_script.append("sudo apt remove --purge warpinator -y")
        final_script.append("sudo apt remove --purge transmission-gtk -y")
        final_script.append("sudo apt remove --purge seahorse -y")
        final_script.append("sudo apt remove --purge imagemagick -y")
        final_script.append("sudo apt remove --purge kdeconnect -y")
    
    if wine == True:
        final_script.append("sudo apt install wine -y")
    if rm_wine == True:
        final_script.append("sudo apt remove --purge wine -y")
        
    if winetricks == True:
        final_script.append("sudo apt install winetricks -y")
    if rm_winetricks == True:
        final_script.append("sudo apt remove --purge winetricks -y")

    if xed == True:
        final_script.append("sudo apt install xed -y")
    if rm_xed == True:
        final_script.append("sudo apt remove --purge xed -y")

    if obs == True:
        final_script.append("flatpak install flathub com.obsproject.Studio -y")
    if rm_obs == True:
        final_script.append("flatpak uninstall flathub com.obsproject.Studio -y")
        
    if blanket == True:
        final_script.append("flatpak install flathub com.rafaelmardojai.Blanket -y")
    if rm_blanket == True:
        final_script.append("flatpak uninstall flathub com.rafaelmardojai.Blanket -y")
        
    if kwrite == True:
        final_script.append("sudo apt install kwrite -y")
    if rm_kwrite == True:
        final_script.append("sudo apt remove --purge kwrite -y")
   
    if vlc == True:
        final_script.append("flatpak install flathub org.videolan.VLC -y")
    if rm_vlc == True:
        final_script.append("flatpak uninstall flathub org.videolan.VLC -y")
   
    if shotcut == True:
        final_script.append("flatpak install flathub org.shotcut.Shotcut -y")
    if rm_shotcut == True:
        final_script.append("flatpak uninstall flathub org.shotcut.Shotcut -y")
   
    if redshift == True:
        final_script.append("sudo apt install redshift -y")
        final_script.append("curl https://github.com/raphaelquintao/QRedshiftCinnamon/raw/master/install.sh -sSfL | bash") 
    if rm_redshift == True:
        final_script.append("sudo apt remove --purge redshift -y")
      
    if xemu == True:
        final_script.append("flatpak install flathub app.xemu.xemu -y")
    if rm_xemu == True:
        final_script.append("flatpak uninstall flathub app.xemu.xemu -y")

    if citra == True:
        final_script.append("flatpak install flathub org.azahar_emu.Azahar -y")
    if rm_citra == True:
        final_script.append("flatpak uninstall flathub org.azahar_emu.Azahar -y")

    if dolphin == True:
        final_script.append("flatpak install flathub org.DolphinEmu.dolphin-emu -y")
    if rm_dolphin == True:
        final_script.append("flatpak uninstall flathub org.DolphinEmu.dolphin-emu -y")

    if ryujinx == True:
        final_script.append("flatpak install flathub io.github.ryubing.Ryujinx -y")
    if rm_ryujinx == True:
        final_script.append("flatpak uninstall flathub io.github.ryubing.Ryujinx -y")

    if melonds == True:
        final_script.append("flatpak install flathub net.kuribo64.melonDS -y")
    if rm_melonds == True:
        final_script.append("flatpak uninstall flathub net.kuribo64.melonDS -y")

    if rpcs3 == True:
        final_script.append("flatpak install flathub net.rpcs3.RPCS3 -y")
    if rm_rpcs3 == True:
        final_script.append("flatpak uninstall flathub net.rpcs3.RPCS3 -y")

    if ducks == True:
        final_script.append("flatpak install flathub org.duckstation.DuckStation -y")
    if rm_ducks == True:
        final_script.append("flatpak uninstall flathub org.duckstation.DuckStation -y")

    if pcsx2 == True:
        final_script.append("flatpak install flathub net.pcsx2.PCSX2 -y")
    if rm_pcsx2 == True:
        final_script.append("flatpak uninstall flathub net.pcsx2.PCSX2 -y")

    if rarch == True:
        final_script.append("flatpak install flathub org.libretro.RetroArch -y")
    if rm_rarch == True:
        final_script.append("flatpak uninstall flathub org.libretro.RetroArch -y")
        
    if ppsspp == True:
        final_script.append("flatpak install flathub org.ppsspp.PPSSPP -y")
    if rm_ppsspp == True:
        final_script.append("flatpak uninstall flathub org.ppsspp.PPSSPP -y")

    if mgba == True:
        final_script.append("flatpak install flathub io.mgba.mGBA -y")
    if rm_mgba == True:
        final_script.append("flatpak uninstall flathub io.mgba.mGBA -y")
        
    if vsc == True:
        final_script.append("flatpak install flathub com.visualstudio.code -y")
    if rm_vsc == True:
        final_script.append("flatpak uninstall flathub com.visualstudio.code -y")

        #### ALWAYS LEAVE AT END!!! ###
    if ar_ac_ap == True:
        final_script.append("sudo apt autoremove -y")
        final_script.append("sudo apt autopurge -y")
        final_script.append("sudo apt autoclean -y")
        final_script.append("sudo apt clean -y")
        

def install():
    global final_script
    
    final_script = [] #clears script
    append()
    
    if len(final_script) == 0:	# if there is nothing selected, do not continue
        pass					# Maybe add a pop-up saying nothing is selected?
    
    else:    
        cmd = open("shell_temp_folder.sh","w")	# Open shell script with write permissions
        cmd.write(" ;\n".join(final_script))		# Combines list into single string (note: ";" means to run each command sequentially, regardless if any proceeding command fails)
        cmd.close()								# Closes shell script to reduce resources

        run('gnome-terminal -- sudo bash ~/simple-linux-utility-and-toolbox/shell_temp_folder.sh', shell=True) # Launch edited shell script in terminal
                        
    
button = Button(root, text="Install",
                command=install, bg="light green", fg="black")
button.grid(row=1,
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


def file():
    global final_script
    
    final_script = [] #clears script
    append()
    
    if len(final_script) == 0:	# if there is nothing selected, do not continue
        pass					# Maybe add a pop-up saying nothing is selected?
    
    else:    
        cmd = open("shell_temp_folder.sh","w")	# Open shell script with write permissions
        cmd.write(" ;\n".join(final_script))		# Combines list into single string (note: ";" means to run each command sequentially, regardless if any proceeding command fails)
        cmd.close()								# Closes shell script to reduce resources
        run('gnome-terminal -- xed ~/simplified-linux-utilities-and-toolbox/shell_temp_folder.sh', shell=True) # Launch edited shell script in terminal

    
button = Button(root, text="View Command",
                command=file)
button.grid(row=1,
            column=0,
            sticky="e",
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