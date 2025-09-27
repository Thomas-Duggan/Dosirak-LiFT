#Useful Websites#

# Simplified Linux Utilities and Toolbox  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0


from key_modules import aaa__prerequisite_definitions__DO_NOT_DELETE as prd


prd.create_content("Useful Websites")


def new (button_title, label_title, command, is_chromium_ext = False, is_chrome_ext = False):

    prd.group_open()

    prd.button (button_title, command, keep_row = True)

    if is_chromium_ext == True:
        prd.text (label_title, keep_row = True)
        prd.text (" (Ungoogled Chromium Extension)", type = "subtitle", color = "grey")

    elif is_chrome_ext == True:
        prd.text (label_title, keep_row = True)
        prd.text (" (Chrome Extension)", type = "subtitle", color = "grey")

    else:
        prd.text (label_title)

    prd.group_close()


new ("Protondb", 
     "Steam game compatibility database for Linux",
     lambda:prd.wb.open("https://www.protondb.com/"))

new ("Linux Fixes & Tricks",
     "Guide for fixing problems and other things",
     lambda:prd.wb.open("https://docs.google.com/document/d/1iPcp4pvT8h_el82Yu8QHue2tv_q9hZtX3IhALam9dG4/edit?tab=t.0"))

new ("Flathub",
     "Online Flatpak app store",
     lambda:prd.wb.open("https://flathub.org/"))

new ("SystemRescueCD",
     "Linux distro for OS recovery",
     lambda:prd.wb.open("https://www.system-rescue.org/Download/"))

new ("Chromium-web-store",
     "Google web store unlocker",
     lambda:prd.wb.open("https://github.com/NeverDecaf/chromium-web-store"),
     is_chromium_ext=True)

new ("uBlock Origin",
     "Ad blocker",
     lambda:prd.wb.open("https://chromewebstore.google.com/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm"),
     is_chromium_ext=True)

new ("Gnome-Look Cursors",
     "Catalog of user-created custom mice",
     lambda:prd.wb.open("https://www.gnome-look.org/browse?cat=107&ord=rating"))

new ("Gnome-Look Plymouth Themes",
     "Catalog of user-created boot themes",
     lambda:prd.wb.open("https://www.gnome-look.org/browse?cat=108&ord=rating"))

new ("Android Google Certification",
     "Use with Waydroid Script to download Google's Play Store",
     lambda:prd.wb.open("https://google.com/android/uncertified/?pli=1"))

new ("Modded Youtube Music App",
     "Portable Youtube Music app with many features",
     lambda:prd.wb.open("https://github.com/th-ch/youtube-music/releases/tag/v3.9.0"))

new ("Box64 Installer",
     "x64 compatibility layer for ARM CPUs",
     lambda:prd.wb.open("https://github.com/cobalt2727/L4T-Megascript/blob/master/scripts/box64.sh"))

new ("Easy Linux Tips Project",
     "Tips for Linux Mint users",
     lambda:prd.wb.open("https://easylinuxtipsproject.blogspot.com/p/clean-mint.html?m=1"))

########################
prd.spacer()
prd.text("Not Linux Related:", type = "title")
########################

new ("Discord on Web",
     "Online Discord application",
     lambda:prd.wb.open("https://discord.com/channels/@me/"))

new ("Video Download Helper",
     "Video downloader for any website",
     lambda:prd.wb.open("https://chromewebstore.google.com/detail/video-downloadhelper/lmjnegcaeklhafolokijcfjliaokphfk"),
     is_chrome_ext=True)

new ("Vencord Web",
     "Vencord client for Discord on Web",
     lambda:prd.wb.open("https://chromewebstore.google.com/detail/video-downloadhelper/lmjnegcaeklhafolokijcfjliaokphfk"),
     is_chrome_ext=True)

new ("SponsorBlock for Youtube",
     "Skip annoying parts of Youtube videos",
     lambda:prd.wb.open("https://chromewebstore.google.com/detail/sponsorblock-for-youtube/mnjggcdmjocbbbhaepdhchncahnbgone?hl=en"),
     is_chrome_ext=True)

new ("MCreator",
     "Easy Minecraft Modding Tool",
     lambda:prd.wb.open("https://mcreator.net/"))

new ("Aternos",
     "Free Minecraft Server Creator",
     lambda:prd.wb.open("https://aternos.org/go/"))

prd.run_content()