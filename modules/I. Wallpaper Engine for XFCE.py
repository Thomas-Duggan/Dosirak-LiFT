#Wallpaper Engine for XFCE (BROKEN)#

# Dosirak LiFT  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0


# Note: "wpe" stands for Wallpaper Engine

from key_modules import aaa__prerequisite_definitions__DO_NOT_DELETE as prd
from json import load
from os import makedirs
from sys import argv
from time import sleep
from pprint import pformat


def set_wallpaper (wallpaper):
    settings = open(prd.path.expanduser("~/Dosirak-LiFT/modules/key_modules/settings_values.py"),"r")
    settings_dict = prd.literal_eval(settings.read())
    settings.close()

    settings_dict["wallpaper engine"]["wallpaper"] = wallpaper
    
    settings = open(prd.path.expanduser("~/Dosirak-LiFT/modules/key_modules/settings_values.py"),"w")
    settings.write(str(pformat(settings_dict)))
    settings.close()


if "--wpe" in argv:
    modules = prd.listdir(prd.path.expanduser('~/Dosirak-LiFT/modules'))
    for module in range(len(modules)):
        if "Wallpaper Engine" in modules[module]:
            name = modules[module].replace(" ",r"\ ")
            break


    wpe_path = prd.path.expanduser("~/.local/share/Steam/steamapps/workshop/content/431960")
    wpe_encrypted = prd.listdir(wpe_path) # list of encrypted names of WPE downloads

    wpe_titles = []
    wpe_usable = []


    for wallpaper in range(len(wpe_encrypted)):
        
        wpe_subpath = prd.path.expanduser(wpe_path + "/" + wpe_encrypted[wallpaper])
        wpe_subpath_directories = prd.listdir(wpe_subpath)

        folder = open(wpe_path + "/" + wpe_encrypted[wallpaper] + "/project.json", "r") # \ 
        wallpaper_info = load(folder)                                                   # < Gets file information
        folder.close()                                                                  # /   Note: load(folder) is due to it being.json
        wpe_titles.append(wallpaper_info["title"])                                      # /


        if ".mp4" in "".join(wpe_subpath_directories):    

            for directory in range(len(wpe_subpath_directories)):           # \
                if ".mp4" in wpe_subpath_directories[directory]:            # <  Gets mp4 file if it exists
                    wpe_usable.append(wpe_subpath_directories[directory])   # /
                    break
                
        else:
            wpe_usable.append(False)                                     

    ########################################## MAIN WINDOW ##########################################

    prd.create_content("WPE 4 XFCE - File Converter")
    prd.group_open()

    for wallpaper in range(len(wpe_titles)):

        prd.button(
            "Open",
            lambda wp = wallpaper: prd.system("open " + wpe_path + "/" + wpe_encrypted[wp]),
            keep_row = True
        )
        

        if wpe_usable[wallpaper] != False:

            prd.button(
                "Install",
                (lambda wp = wallpaper: (
                    makedirs(prd.path.expanduser("~/Dosirak-LiFT/wallpapers/"+wpe_titles[wp]), exist_ok = True),
                    prd.system("ffmpeg -i "+wpe_path+"/"+wpe_encrypted[wp]+'/"'+wpe_usable[wp]+'" -vf fps=10 ~/Dosirak-LiFT/wallpapers/"'+wpe_titles[wp]+'"/frame_%04d.png'),
                    set_wallpaper(wpe_titles[wallpaper]),
                    prd.system(f'python3 {prd.path.expanduser("~/Dosirak-LiFT/modules")}/{name} --run'),
                    )),
                keep_row = True
            )

            prd.text(
                wpe_titles[wallpaper]
            )

        
        if wpe_usable[wallpaper] == False:

            prd.text(
                " (Not installable)",
                type = "subtitle",
                color = "red",
                keep_row = True
                )

            prd.text(
                wpe_titles[wallpaper]
            )

        prd.group_new_line()


    prd.group_close()
    prd.run_content()

if "--run" in argv:

    settings = open(prd.path.expanduser("~/Dosirak-LiFT/modules/key_modules/settings_values.py"),"r")
    settings_dict = prd.literal_eval(settings.read())
    settings.close()

    directory = prd.path.expanduser('~/Dosirak-LiFT/wallpapers/')
    subdirectory = {settings_dict["wallpaper engine"]["wallpaper"]}
    subdirectory = str(subdirectory).replace("{","").replace("}","")

    frames = sorted(prd.listdir(f"{directory}{settings_dict['wallpaper engine']['wallpaper']}"))
    frame_list = []

    fps = 20

    for i in range(len(frames)):
        frame_list.append(f"xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitorHDMI-0/workspace0/last-image -s {directory}{subdirectory}/{frames[i]}")

    print(frame_list)

    while True:
        for i in range(len(frame_list)):
            prd.system(frame_list[i])
            sleep(1/fps)

else:
    modules = prd.listdir(prd.path.expanduser('~/Dosirak-LiFT/modules'))
    for module in range(len(modules)):
        if "Wallpaper Engine" in modules[module]:
            name = modules[module].replace(" ",r"\ ")
            break

    prd.create_content("WPE for XFCE - Settings")
    prd.group_open()

    prd.text("Information:",
        type = "title")

    prd.spacer()
    prd.text("---------------------------------------------------------------------------------------------------------------")
    prd.text("This module only works on XFCE.",
             type = "title_not_bold")
    prd.text('If you are using a different DE (ie. Cinnamon), delete this module and "wallpapers" folder.',
             type = "title_not_bold")
    prd.text('Also, this project is NOT affiliated with Wallpaper Engine in ANY way.',
             type = "title_not_bold")
    prd.text("---------------------------------------------------------------------------------------------------------------")

    prd.button(
        "Open WPE to XFCE converter",
        lambda: (
            prd.run(f'gnome-terminal -- python3 {prd.path.expanduser("~/Dosirak-LiFT/modules")}/{name} --wpe', shell = True),
            exit()   
            )
    )


    prd.group_close()
    prd.run_content()
