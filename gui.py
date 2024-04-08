# import tkinter as tk
# from tkinter import ttk
from tkinter.constants import BOTH

#Create a root window inheriting the propertes from Tkinter class
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from app import Start
from app.SnS import SnSFunction
from app.Start import CovidScreen, StartPage, StopNSearchScreen

from app.case_study1 import Case_Study_1
from app.case_study2 import Case_Study_2
from app.case_study3 import Case_Study_3





class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Covid19 and Stop & Search Information Centre')
        self.geometry(f'{self.winfo_screenwidth() - 200}x{self.winfo_screenheight() - 200}')
        
        
        tk.Frame(bg='green').__init__(self)
        # label
        self.frames = {}
        # defined a list of frames 
        frame_list = [StartPage,Case_Study_1,Case_Study_2,Case_Study_3, SnSFunction, CovidScreen, StopNSearchScreen ]
        for F in frame_list:
            #create a frame object from each classes mentioned above using a for loop
            frame = F(self)
            #Add the classes and objects in the initialized dictionary
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    # Defined a function which will be called every time we click the button in the above mentioned frames
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def run():
    app = Gui()
    return app

if __name__ == "__main__":
    run().mainloop()

