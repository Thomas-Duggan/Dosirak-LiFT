#Home#

# Dosirak LiFT  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0

background = "light blue"

from modules.key_modules import aaa__prerequisite_definitions__DO_NOT_DELETE as prd

prd.create_content("Home",
                   x = 350,
                   y = 480,
                   background = background)

prd.group_open(background = background)

############################

prd.text(f"{[x for x in range (17)]}",
         color = background,
         background = background)

prd.text("Welcome to Dosirak:",
         type = "home_title",
         color = "purple",
         background = background,
         location = "bottom")

prd.text("Linux Fixes",
         type = "title_not_bold",
         background = background,
         color = "blue",
         location = "bottom")

prd.text("and Tricks",
         type = "title_not_bold",
         background = background,
         color = "dark blue",
         location = "bottom")

prd.text ("Last updated Sept 29, 2025",
          type = "subtitle",
          background = background,
          color = "grey",
          location = "bottom")

prd.spacer()

prd.text ("Where would you like to go?",
          type = "title_not_bold",
          background = background,
          location = "bottom")

############################

prd.home_buttons()

prd.group_close(sticky = "e")

############################

prd.group_open(parent = prd.root, 
               background = background)

prd.button("Info",
           lambda:(prd.run('gnome-terminal -- python3 ~/Dosirak-LiFT/modules/key_modules/info.py && exit', shell = True), exit()),
           keep_row = True)

prd.button("Quit",
           quit,
           keep_row = True)

prd.button("Settings",
           lambda:(prd.run('gnome-terminal -- python3 ~/Dosirak-LiFT/modules/key_modules/settings.py && exit', shell = True), exit()))

prd.group_close(sticky = "n")

############################

prd.run_content(home = True)
