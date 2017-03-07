#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Tegan Straley
#Port scanner in python
#created for CSCI 4800, cyber security programming
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# file: GUIFrame.py
# Creates the front-end side of a port scanner with Python's tkinter libraries.
# Pack and grid inserts are found at the bottom of the file.

from tkinter import *
import GUIFunctions

#~~~~~~~~~~ MENU ~~~~~~~~~~

root = Tk()
menu = Menu(root)
root.config(menu=menu) # what's under 'File' menu item
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Port Scanner", command=GUIFunctions.NewFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

aboutMenu = Menu(menu) # what's under 'About' menu item
menu.add_cascade(label="About", menu=aboutMenu)
aboutMenu.add_command(label="Author", command=GUIFunctions.AboutAuthor)
aboutMenu.add_command(label="Port scanner", command = GUIFunctions.AboutPortScanner)


#~~~~~~~~ FEATURE CREATION ~~~~~~~~

scannerInfo = Frame(root)
scannerInfo2 = Frame(root)
scannerInfo3 = Frame(root)

# things for scannerInfo
label = Label(scannerInfo, text="Port Scanner")

# things for scannerInfo2
portNumber = Label(scannerInfo2, text="IP address (xxx.xxx.xxx.xxx)")
entry1 = Entry(scannerInfo2)
portStart = Label(scannerInfo2, text="Port to start at")
entry2 = Entry(scannerInfo2)
portStop = Label(scannerInfo2, text="Port to stop at")
entry3 = Entry(scannerInfo2)

# things for scannerInfo3
scan_button = Button(scannerInfo3, text="Scan", command=GUIFunctions.portScan, width = 20, height = 1)
outputBox = Text(scannerInfo3, height = 10, width = 60)
outputBox.insert(INSERT, "The numbers of the open ports will appear here...\n\n")
scrollbar = Scrollbar(outputBox)
listbox = Listbox(outputBox, yscrollcommand=scrollbar.set, width = 60, height = 10)
listbox.insert(END, "The numbers of the open ports will appear here...\n\n")

#~~~~~~~~~~ LAYOUT PACK, GRID, ETC. ~~~~~~~~~~~~~

#scannerInfo
label.pack(fill=X, pady=10)

#scannerInfo2
portNumber.grid(row=1, sticky=E, padx = 5, pady=5)
entry1.grid(row=1, column=1, sticky=E, padx = 5, pady=5)
portStart.grid(row=2, sticky=E, padx = 5, pady=5)
entry2.grid(row=2, column=1, sticky=E, padx = 5, pady=5)
portStop.grid(row=3, sticky=E, padx = 5, pady=5)
entry3.grid(row=3, column=1, sticky=E, padx = 5, pady=5)

#scannerInfo3
scan_button.pack(padx = 10, pady=10)
outputBox.pack(side=LEFT, fill = BOTH, pady=15, padx=15)
scrollbar.pack(side = RIGHT, fill = Y )
# listbox is in the outputBox
listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command = listbox.yview)


scannerInfo.pack()
scannerInfo2.pack()
scannerInfo3.pack()

root.title("Tegan Straley's Port Scanner")

mainloop() # shows the GUI