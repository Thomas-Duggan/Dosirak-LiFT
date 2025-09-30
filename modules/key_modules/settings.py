#Settings#

# Dosirak LiFT  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0


import aaa__prerequisite_definitions__DO_NOT_DELETE as prd
from pprint import pformat


def title(family, key, exists = True):
    
    hidden_current = read_value(key, "hidden")

    hidden_after_press = not hidden_current

    prd.button("Hide / Show",
            lambda: update(key, "hidden", hidden_after_press),
            keep_row = True)

    prd.text(f"{family}",
             type = "title",
             color = "green")

def read_value(family, key):
    settings = open(prd.path.expanduser("~/Dosirak-LiFT/modules/key_modules/settings_values.py"),"r")
    settings_dict = prd.literal_eval(settings.read())
    settings.close()

    return settings_dict[family][key]

def lined_spacer(exists = True):
    prd.group_new_line()
    prd.text("-------------------------------------",
             exists = exists)
    prd.group_new_line()

def update(family, key, value):
    settings = open(prd.path.expanduser("~/Dosirak-LiFT/modules/key_modules/settings_values.py"),"r")
    settings_dict = prd.literal_eval(settings.read())
    settings.close()

    settings_dict[family][key] = value
    
    settings = open(prd.path.expanduser("~/Dosirak-LiFT/modules/key_modules/settings_values.py"),"w")
    settings.write(str(pformat(settings_dict)))
    settings.close()

    prd.run('gnome-terminal -- python3 ~/Dosirak-LiFT/modules/key_modules/settings.py && exit', shell = True)
    exit()

def default_is(value, spacer = True, exists = True):
    prd.group_new_line()

    prd.text(f"    Default: {value}",
         type = "subtitle",
         color = "grey",
         exists = exists)
    
    if spacer == True:
        prd.spacer(exists = exists)
    
def section(title, family, key, exists = True):
    prd.group_new_line()

    prd.text (f" >>  {title}",
              keep_row = True,
              exists = exists)

    prd.text (f" Current Value: {read_value(family, key)}",
            type = "subtitle",
            color = "grey",
            exists = exists)
    
    prd.group_new_line(exists = exists)

####################################################

prd.create_content(title = "Settings")

prd.group_open()

####################################################

title("General", "general")

general_vis = prd.settings_dict["general"]["hidden"]

#################################################### General - Screen Width ####################################################

section("Screen Width:", "general", "screen width",
         exists = general_vis)

    # Entry Field
screen_width = prd.Entry(prd.group_frame)
screen_width.grid(row = prd.row,
                column = prd.column,
                pady = 5,
                padx = 7)
prd.bind_scroll(screen_width)
prd.column += 1

if general_vis == False:
    screen_width.grid_forget()

    # Confirmation Button
prd.button("Confirm",
           lambda: update("general", "screen width", int(screen_width.get())),
           exists = general_vis)

    # Extra Labels
default_is(1920,
           spacer = False,
           exists = general_vis)

prd.group_new_line(exists = general_vis)

prd.text(f"(Note: your screen width seems to be {prd.root.winfo_screenwidth()})",
         type = "subtitle",
         color = "grey",
         exists = general_vis)

prd.spacer(exists = general_vis)

prd.group_new_line(exists = general_vis)

#################################################### General - Screen Height ####################################################

section ("Screen Height:", "general", "screen height",
         exists = general_vis)

    # Entry Field
screen_height = prd.Entry(prd.group_frame)
screen_height.grid(row = prd.row,
                column = prd.column,
                pady = 5,
                padx = 7)
prd.bind_scroll(screen_height)
prd.column += 1

if general_vis == False:
    screen_height.grid_forget()

    # Confirmation Button
prd.button("Confirm",
           lambda: update("general", "screen height", int(screen_height.get())),
           exists = general_vis)

    # Extra Labels
default_is(1080,
           spacer = False,
           exists = general_vis)

prd.group_new_line(exists = general_vis)

prd.text(f"(Note: your screen height seems to be {prd.root.winfo_screenheight()})",
         type = "subtitle",
         color = "grey",
         exists = general_vis)

prd.spacer(exists = general_vis)

prd.group_new_line(exists = general_vis)

#################################################### General - Popup Location ####################################################

section ("Popup Location", "general", "popup location",
         exists = general_vis)

prd.button("Top Left",
           lambda: update("general", "popup location", "Top Left"),
           keep_row = True,
           exists = general_vis)

prd.button("Top Middle",
           lambda: update("general", "popup location", "Top Middle"),
           keep_row = True,
           exists = general_vis)

prd.button("Top Right",
           lambda: update("general", "popup location", "Top Right"),
           exists = general_vis)

prd.group_new_line(exists = general_vis)

prd.button("Middle Left",
           lambda: update("general", "popup location", "Middle Left"),
           keep_row = True,
           exists = general_vis)

prd.button("Middle Middle",
           lambda: update("general", "popup location", "Middle Middle"),
           keep_row = True,
           exists = general_vis)

prd.button("Middle Right",
           lambda: update("general", "popup location", "Middle Right"),
           exists = general_vis)

prd.group_new_line(exists = general_vis)

prd.button("Bottom Left",
           lambda: update("general", "popup location", "Bottom Left"),
           keep_row = True,
           exists = general_vis)

prd.button("Bottom Middle",
           lambda: update("general", "popup location", "Bottom Middle"),
           keep_row = True,
           exists = general_vis)

prd.button("Bottom Right",
           lambda: update("general", "popup location", "Bottom Right"),
           exists = general_vis)

default_is("Middle Middle",
           exists = general_vis)

#################################################### General - Popup Offset ####################################################

section ("Popup Offset", "general", "popup offset",
         exists = general_vis)

    # Entry Field
popup_offset = prd.Entry(prd.group_frame)
popup_offset.grid(row = prd.row,
                column = prd.column,
                pady = 5,
                padx = 7)
prd.bind_scroll(popup_offset)
prd.column += 1

if general_vis == False:
    popup_offset.grid_forget()

    # Confirmation Button
prd.button("Confirm",
           lambda: update("general", "popup offset", int(popup_offset.get())),
           exists = general_vis)

    # Extra Labels
default_is(0, exists = general_vis)

prd.group_new_line(exists = general_vis)

####################################################

lined_spacer()



modules = prd.listdir(prd.path.expanduser('~/Dosirak-LiFT/modules'))


for module in range(len(modules)):
    file_name = modules[module]

    # if "App Install Helper" in file_name:
    #     title("App Install Helper", "app install helper")
    #     app_install_helper_vis = prd.settings_dict["app install helper"]["hidden"]



    #     lined_spacer()  



    if "Quick Commands" in file_name:
        title("Quick Commands", "quick commands")
        quick_commands_vis = prd.settings_dict["quick commands"]["hidden"]

        section("Power Profiles", "quick commands", "power profiles hidden",
                exists = quick_commands_vis)

        prd.button("Hide All Options",
           lambda: update("quick commands", "power profiles hidden", "Hide All Options"),
           exists = quick_commands_vis)

        prd.button("Hide Performance Mode",
           lambda: update("quick commands", "power profiles hidden", "Hide Performance Mode"),
           exists = quick_commands_vis)

        prd.button("Show All Options",
           lambda: update("quick commands", "power profiles hidden", "Show All Options"),
           exists = quick_commands_vis)
        
        default_is("Show All Options",
                   exists = quick_commands_vis)

        lined_spacer()



    # if "Useful Websites" in file_name:
    #     title("Useful Websites", "useful websites")
    #     useful_websitess_vis = prd.settings_dict["useful websites"]["hidden"]

    #     lined_spacer()




    # if "Internet Stability Graph" in file_name:
    #     title("Internet Stability Graph", "internet stability graph")
    #     insternet_stability_graph_vis = prd.settings_dict["internet stability graph"]["hidden"]

    #     lined_spacer()




    # if "File Cleaner" in file_name:
    #     title("File Cleaner", "file cleaner":

    #     lined_spacer()



    # if "Screenshot Tool" in file_name:
    #     title("File Cleaner", "file cleaner")
    
    #     lined_spacer()
    
prd.group_close()

prd.run_content()