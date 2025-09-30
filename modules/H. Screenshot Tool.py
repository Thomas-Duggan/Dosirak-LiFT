#Screenshot Tool#

# Dosirak LiFT  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0

from key_modules import aaa__prerequisite_definitions__DO_NOT_DELETE as prd
from sys import argv



if "--sc" in argv:
    from PIL import ImageGrab
    from io import BytesIO

    screenshot = ImageGrab.grab() # Takes screenshot

    location = BytesIO() # Allocates area in RAM for screenshot
    
    screenshot.save(location, format="PNG") # saves screenshot to RAM

    location.seek(0) # Prepares location for reading

    prd.run(
        ["xclip", "-selection", "clipboard", "-t", "image/png"],
        input=location.read()
    )



else: 

    modules = prd.listdir(prd.path.expanduser('~/Dosirak-LiFT/modules'))
    for module in range(len(modules)):
        if "Screenshot Tool" in modules[module]:
            name = modules[module].replace(" ","\ ")
            break

    def update(family, key, value):
        settings = open(prd.path.expanduser("~/Dosirak-LiFT/modules/key_modules/settings_values.py"),"r")
        settings_dict = prd.literal_eval(settings.read())
        settings.close()

        settings_dict[family][key] = value
        
        settings = open(prd.path.expanduser("~/Dosirak-LiFT/modules/key_modules/settings_values.py"),"w")
        settings.write(str(prd.pformat(settings_dict)))
        settings.close()

        prd.run('gnome-terminal -- python3 ~/Dosirak-LiFT/modules/key_modules/settings.py && exit', shell = True)
        exit()

    def open_xed():

        cmd = open(prd.path.expanduser("~/Dosirak-LiFT/shell_temp_folder.sh"),"w")
        cmd.write(f'python3 ~/Dosirak-LiFT/modules/{name} --sc')		
        cmd.close()								
        prd.run('gnome-terminal -- xed ~/Dosirak-LiFT/shell_temp_folder.sh', shell=True) 

    def install(delete = False):

        if delete == False:
            prd.run('gnome-terminal -- pip install -y pillow && sudo apt install -y xclip && exit', shell=True) 
        else:
            prd.run('gnome-terminal -- pip uninstall -y pillow && sudo apt remove -y xclip && exit', shell=True) 


    prd.create_content("Screenshot Tool")

    prd.group_open()


    prd.text("Information:",
            type = "title")
    

    prd.spacer()
    prd.text("---------------------------------------------------------------------------------------------------------------")
    prd.text("This module only exists to fix a screenshot issue I kept having with XFCE.",
             type = "title_not_bold")
    prd.text("If you are using a different DE (ie. Cinnamon), delete this module.",
             type = "title_not_bold")
    prd.text("---------------------------------------------------------------------------------------------------------------")


    prd.spacer()


    prd.text('To take a screenshot, create a shell script in "~/bin" with this in it, and bind ')
    prd.text("the script's name to a command in the Keyboard application:")
    prd.text(f'        python3 ~/Dosirak-LiFT/modules/{name} --sc')
    prd.button("Open Command",
               lambda: open_xed())
    

    prd.spacer()


    prd.text("This module also requires these to be installed:")

    prd.group_new_line()

    prd.text("        Pillow - Image Handling Library  (pip install pillow)") 
    prd.text("        xClip - Clipboard Utility  (sudo apt install xclip)") 

    prd.group_new_line()

    prd.button("Install All",
               lambda: install(),
               keep_row = True)
    prd.button("Uninstall All",
               lambda: install(delete = True))

    prd.group_new_line()

    prd.spacer()
    
    prd.text('Further configuration can be found in "Settings". (NOT IMPLEMENTED YET)')

    prd.group_close()
    prd.run_content()


