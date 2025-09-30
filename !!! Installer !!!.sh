# ================================================================ #
#      ____             __           __      __    ______________  #
#     / __ \____  _____/_/________ _/ /__   / /   /_/ ___/__  __/  #
#    / / / / __ \/ ___/ / ___/ __ `/ //_/  / /   / / /_    / /     #
#   / /_/ / /_/ /__  / / /  / /_/ / ,<    / /___/ / __/   / /      #
#  /_____/\____/____/_/_/   \__,_/_/|_|  /_____/_/_/     /_/       #
#                                                                  #
#  (Logo made with pyfiglet)                                       #
# ================================================================ #
# Dosirak LiFT  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0


# Prerequisites:

###  Update and Upgrade repositories
sudo apt update && upgrade

###  Installing Flatpak
sudo apt install flatpak -y
sudo apt install gnome-software-plugin-flatpak -y
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

###  Installing Xed text reader
sudo apt install xed -y

###  Installing Python and Tkinter
sudo apt install python3 -y
sudo apt install python3-tk -y

###  Installing git clone
sudo apt install git -y


# Installing App from Github Repo:

git clone https://github.com/Thomas-Duggan/simplified-linux-utilities-and-toolbox

