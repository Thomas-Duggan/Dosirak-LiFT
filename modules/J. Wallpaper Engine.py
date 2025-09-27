#Wallpaper Engine for XFCE (BROKEN)#

# Simplified Linux Utilities and Toolbox  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0


from key_modules import aaa__prerequisite_definitions__DO_NOT_DELETE as prd
from json import load


wpe_path = prd.path.expanduser("~/.steam/debian-installation/steamapps/workshop/content/431960")
wpe_downloads = prd.listdir(wpe_path) # list of encrypted names of WPE downloads

wpe_titles = []


for wallpaper in range(len(wpe_downloads)):
    
    folder = open(wpe_path + "/" + wpe_downloads[wallpaper] + "/project.json", "r")
    wallpaper_info = load(folder)
    folder.close()

    wpe_titles.append(wallpaper_info["title"])

                
##################################################################################################################

prd.create_content("WPE 4 XFCE")
prd.group_open()

for wallpaper in range(len(wpe_titles)):

    prd.button(
        "Open",
        lambda: prd.system("open " + wpe_path + "/" + wpe_downloads[wallpaper]),
        keep_row = True
    )

    prd.button(
        "Install",
        print(True),
        keep_row = True
    )

    prd.text(wpe_titles[wallpaper])

prd.group_close()
prd.run_content()