import tkinter as tk
from tkinter import filedialog
from threading import *
import os

class CreateDirectorySegment(tk.Frame):
    def __init__(self, parent):
        super().__init__(master = parent)

        self.main_folder_path = ''

        mainDirectory_LabelFrame = tk.LabelFrame(parent, text = 'Main directory of flashing files', font = ('Arial', 10))
        mainDirectory_LabelFrame.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.12)

        self.create_widgets(mainDirectory_LabelFrame)

    def create_widgets(self, parent):

        self.mainDirectory_Entry = tk.Entry(parent, font = ('Arial', 12), textvariable = self.main_folder_path)
        self.mainDirectory_Entry.insert(0, self.main_folder_path)
        self.mainDirectory_Entry.place(relx = 0.01, rely = 0.08, relwidth = 0.86, relheight = 0.7)

        selectDirectory_Button = tk.Button(parent, text = 'Select', font = ('Arial', 12), command = self.select_directory)
        selectDirectory_Button.place(relx = 0.88, rely = 0.08, relwidth = 0.11, relheight = 0.7)

    def select_directory(self):
        self.main_folder_path = filedialog.askdirectory(title="Select integration directory")
        self.set_directory_text_box()
    
    def set_directory_text_box(self):
        self.mainDirectory_Entry.delete(0, len(self.main_folder_path))
        self.mainDirectory_Entry.insert(0, self.main_folder_path)

    def get_directory_text_box(self):
        return self.mainDirectory_Entry.get()

def checkingSchedule():
    pass

def atClosenig():
    print('----------------------------------------')
    print('                                        ')
    print('        >> Application closed <<        ')
    print('           See you next time!           ')
    print('                                        ')
    print('########################################')

    window.after(300,  window.destroy)

try:
    print('########################################')
    print('                                        ')
    print('        >> Application start! <<        ')
    print('                                        ')
    print('----------------------------------------')
    print('')
 
    # window settings
    windowTitle = 'Simply flash application'
    size = (900,600)

    window = tk.Tk()
    window.title(windowTitle)
    window.iconbitmap('flash_icon.ico')
    window.minsize(size[0], size[1])
    window.maxsize(size[0], size[1])

    # widgets
    directory_segment = CreateDirectorySegment(window)

    t1 = Thread(target = checkingSchedule)
    t1.start()

    window.protocol("WM_DELETE_WINDOW", atClosenig)
    window.mainloop()
except:
    print('')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('     >> Application launch error <<     ')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')