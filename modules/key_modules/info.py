#Info#

# Dosirak LiFT  Copyright (c) 2025  Thomas Duggan
# This work is licensed under CC BY-SA 4.0

import aaa__prerequisite_definitions__DO_NOT_DELETE as prd

prd.create_content("Info")

prd.group_open()

prd.spacer()
#######################################################################################

prd.text("Copyright:",
         type = "title"),

#######################################################################################

prd.text("Creative Commons Attribution-ShareAlike 4.0 International Public License"),

prd.button("See More",
           lambda: prd.wb.open("https://creativecommons.org/licenses/by-sa/4.0"))

prd.spacer()
#######################################################################################

prd.text("Credits:",
         type = "title"),

prd.text('Thomas Duggan  -  Lead Programmer')

prd.button("Github",
           lambda: prd.wb.open("https://github.com/Thomas-Duggan"),
           )

prd.spacer()
#######################################################################################

prd.text("Dylan Johnston  -  Quality Assurance")

prd.spacer()
prd.spacer()
#######################################################################################

prd.text("Special Thanks To...",
         type = "title_not_bold")

prd.spacer()
#######################################################################################

prd.text("Gaurav Leekha  -  Source Code Contributor")


prd.button("Tutorialspoint",
           lambda: prd.wb.open("https://www.tutorialspoint.com/implementing-a-scrollbar-using-grid-manager-on-a-tkinter-window"))

prd.spacer()
#######################################################################################

prd.text("Python Tutorial  -  Tkinter Info Database")


prd.button("Python Tutorial",
           lambda: prd.wb.open("https://www.pythontutorial.net/tkinter/"))

#######################################################################################

prd.group_close()

prd.run_content()