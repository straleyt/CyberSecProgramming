#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Tegan Straley
#Port scanner in python
#created for CSCI 4800, cyber security programming
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# file: GUIFunctions.py
# Creates the back-end side of a port scanner with Python's tkinter libraries.
# portScan() - uses code from lab02 to port scan from and to a specified port. Has input validation at beginning.
# NewFile() - Erases the text in all the boxes of the GUI.
# AboutAuthor() - displays out information about me (Tegan Straley)
# AboutPortScanner() - displays out information about port scanning :)

from tkinter import *
import socket
from tkinter import messagebox
import sys
import GUIFrame


#backend port scanning function
def portScan():

    GUIFrame.listbox.delete(0, END)

    try:
        socket.inet_aton(GUIFrame.entry1.get()) # IP input validation
        remoteServer = GUIFrame.entry1.get()
        portStart = int(GUIFrame.entry2.get())
        portStop = int(GUIFrame.entry3.get())
        if portStop < 0 or portStart < 0:
            messagebox.showerror("Error", "IP addresses cannot be negative! Try again...")
            return;
        if portStop < portStart:
            messagebox.showerror("Error", "The port to stop at can't be lower than the starting port! Try again...")
            return;
        if portStop > 65535 or portStart > 65535:
            messagebox.showerror("Error", "There's only 65,535 ports to scan! Try again...")
            return;
        messagebox.showinfo("Just so you know...", "This may take a few minutes to complete.")
    except ValueError:
        messagebox.showerror("Error", "Not valid start/stop port! Try again...") #integer input validation
    except socket.error:
        messagebox.showerror("Error", "That isn't a valid IP address! Try again...") #IP input validation

    try:
        for port in range(int(portStart), int(portStop)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creation of new socket
            sock.settimeout(.5)
            sock.setblocking(1)
            result = sock.connect_ex((remoteServer, port)) #if socket can connect to the port given...
            if result == 0:
                GUIFrame.listbox.delete(0, END)
                GUIFrame.listbox.insert(END, "Port{}:  Open".format(port))
                GUIFrame.listbox.insert(END, "\n")
            sock.close()
            GUIFrame.listbox.insert(END, "\nPort scanning complete")
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        messagebox.showinfo("Port scanning ended", "Ctrl+C was pressed, you may want to restart the scan...") #?? doesn't really work
        sys.exit()

def NewFile():
    GUIFrame.entry1.delete(0, END)
    GUIFrame.entry2.delete(0, END)
    GUIFrame.entry3.delete(0, END)
    GUIFrame.listbox.delete(0, END)

def AboutAuthor():
    print("Created by: Tegan Straley\nClass: CSCI 4800\nFebruary 28, 2017\n")
    GUIFrame.listbox.delete(0, END)
    GUIFrame.listbox.insert(END, "Author: Tegan Straley\n\n")
    GUIFrame.listbox.insert(END,"Class: CSCI 4800")
    GUIFrame.listbox.insert(END,"Date: February 28, 2017")

def AboutPortScanner():
    GUIFrame.listbox.delete(0, END)
    GUIFrame.listbox.insert(END,"Every computer has ports that connect to external devices.")
    GUIFrame.listbox.insert(END, "There are a total of 65,535 ports. Not all of them are in use.")
    GUIFrame.listbox.insert(END, "A Port scanner verifies which ports are open on a specific IP address.")
    GUIFrame.listbox.insert(END, "This is used by administrators to verify")
    GUIFrame.listbox.insert(END, "security policies of their networks and by attackers")
    GUIFrame.listbox.insert(END, "to try to exploit vulnerabilities.")
