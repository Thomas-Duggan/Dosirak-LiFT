#Quick Commands#

# Dosirak LiFT  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0

from key_modules import aaa__prerequisite_definitions__DO_NOT_DELETE as prd

power_profiles_setting = prd.settings_dict["quick commands"]["power profiles hidden"]

if power_profiles_setting == "Hide All Options":
    pass


prd.create_content("Quick Commands")

prd.group_open()

###################################
prd.spacer()
prd.text("Power Profiles:",
         type = "title")
###################################

prd.group_new_line()

prd.button("Power Saver",
           lambda:prd.run('gnome-terminal -- powerprofilesctl set power-saver', shell=True),
           keep_row = True)

prd.button("Balanced",
           lambda:prd.run('gnome-terminal -- powerprofilesctl set balanced', shell=True),
           keep_row = True)

prd.button("Performance",
           lambda:prd.run('gnome-terminal -- powerprofilesctl set performance', shell=True))

prd.group_new_line()

###################################
prd.spacer()
prd.text("Waydroid Extras Script:",
         type = "title")
###################################

prd.group_new_line()

prd.button("Launch",
           lambda:prd.run('gnome-terminal -- sudo bash -c "git clone https://github.com/casualsnek/waydroid_script ; cd waydroid_script ; python3 -m venv venv ; venv/bin/pip install -r requirements.txt ; sudo venv/bin/python3 main.py; exec bash"', shell=True),
           keep_row = True)

prd.button("Website (Source)",
           lambda:prd.wb.open("https://github.com/casualsnek/waydroid_script"))

prd.group_new_line()

###################################
prd.spacer()
prd.text("CLI-Only Apps:",
         type = "title")
###################################

prd.group_new_line()

prd.button("Table of Processes",
           lambda:prd.run('gnome-terminal -- top -id 999', shell=True),
           keep_row = True)

prd.button("Human Table of Processes",
           lambda:prd.run('gnome-terminal -- htop', shell=True),
           keep_row = True)

#prd.group_new_line()

prd.button("NCurses Disc Usage Analyzer",
           lambda:prd.run('gnome-terminal -- ncdu /', shell=True),
           keep_row = True)

prd.group_new_line()

prd.button("Android Screen Copy",
           lambda:prd.run('gnome-terminal -- scrcpy', shell=True),
           keep_row = True)

prd.button("Android Screen Copy (Full Screen)",
           lambda:prd.run('gnome-terminal -- scrcpy --keyboard=uhid --mouse=aoa --gamepad=aoa --fullscreen', shell=True),
           keep_row = True)

prd.group_new_line()

###################################
prd.spacer()
prd.text("Quick Access Folders / Files:",
         type = "title")
###################################

prd.group_new_line()

prd.button("Boot Theme Folder",
           lambda:prd.run('gnome-terminal -- sudo open /usr/share/plymouth/themes/mint-logo', shell=True),
           keep_row = True)

prd.button("Custom Mice Folder",
           lambda:prd.run('gnome-terminal -- sudo open /usr/share/icons', shell=True),
           keep_row = True)

prd.button("Neofetch Customizer",
           lambda:prd.run('gnome-terminal -- xed ~/.config/neofetch/config.conf', shell=True),
           keep_row = True)

prd.group_new_line()

prd.button("Gnome Terminal Aliases",
           lambda:prd.run('gnome-terminal -- xed ~/.bashrc /', shell=True),
           keep_row = True)

prd.button("FISH Aliases",
           lambda:prd.run('gnome-terminal -- xed ~/.config/fish/config.fish /', shell=True),
           keep_row = True)

prd.button("GRUB Boot Options",
           lambda:prd.run('gnome-terminal -- sudo xed /etc/grub.d/40_custom', shell=True),
           keep_row = True)

prd.group_new_line()

prd.button("Swappiness Editor",
           lambda:prd.run('gnome-terminal -- bash -c "echo \\"At the bottom of text editor, type:   vm.swappiness = 10\nReccomended range: 0 to 20 \n\\"; sudo xed /etc/sysctl.conf ; sudo sysctl -p"', shell=True),
           keep_row = True)

prd.button("Proton Wineprefix Folder",
           lambda:prd.run('gnome-terminal -- nemo ~/.steam/steam/steamapps/compatdata', shell=True),
           keep_row = True)

prd.button("Steam Workshop Folder",
           lambda:prd.run('gnome-terminal -- nemo ~/.local/share/Steam/steamapps/workshop/content', shell=True),
           keep_row = True)

prd.group_new_line()

prd.button("Sysreq Unlocker",
           lambda:prd.run('gnome-terminal -- bash -c "echo \\"Replace the value in this file with:  1\nThis will allow the keybind Alt+PrtScn+K for a safer and faster alternative to REISUB.\nPlease disregard any file saving errors.\\"; sudo xed /proc/sys/kernel/sysreq ; sudo sysctl -p"', shell=True),
           keep_row = True)

prd.group_new_line()


# lsusb  -  list all usb devices
# sudo xed /etc/udev/rules.d/51-android.rules  -  udev rules file
# SUBSYSTEM=="usb", ATTR{idVendor}=="####", ATTR{idProduct}=="####", MODE="0666", GROUP="plugdev"  -  #### gets replaced in order
# sudo udevadm control --reload-rules; sudo udevadm trigger  -  Reload udev rules

prd.group_close()

###################################
prd.spacer()
prd.text("Wine:",
         type = "title")
###################################

prd.group_open()

prd.button("File Explorer",
           lambda:prd.run('gnome-terminal -- winefile', shell=True),
           keep_row = True)

prd.button("Registry Editor",
           lambda:prd.run('gnome-terminal -- regedit', shell=True))

prd.group_close()

###################################
prd.run_content()
###################################