from calendar import c
import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import font
from tkinter.constants import BOTH, BOTTOM, CENTER, LEFT, TOP

from numpy import right_shift
from . import SnS
from .case_study1 import Case_Study_1
from .case_study2 import Case_Study_2
from .case_study3 import Case_Study_3



class StartPage(tk.Frame):

    def __init__(self, app):


        tk.Frame.__init__(self, app)
        self.pack(fill=BOTH, anchor=CENTER)
        

        # Home page contains three sections, leftFrame, rightFrame and rightframe
        leftFrame = tk.Frame(self,  width=300, height=50, pady=150, padx=70)
        leftFrame.pack( side=tk.LEFT,expand=True, padx=1, anchor=CENTER)

        rightFrame = tk.Frame(self,  width=300, height=50,pady=150, padx=170)
        rightFrame.pack( side=tk.RIGHT, expand=True, padx=1, anchor=CENTER)
            
        
        #leftFrame logo
        self.logo = PhotoImage(file='app/Data/university logo.png')
        img = tk.Label(leftFrame, image=self.logo)
        img.pack()
        
        
        heading = tk.Label(leftFrame, text='\nWelcome to Information Centre!\n', font=("Arial", 25),foreground="black", background='lightblue')
        heading.pack(side=tk.TOP,pady=20, padx=20)

        Developer = tk.Label(leftFrame, text='ICA by Gowthami Nagappan (B1326237)', background='white', font="bold", foreground="black")
        Developer.pack(side=tk.TOP,pady=15)
        
        self.exit_button = ttk.Button(rightFrame, text="EXIT", cursor='hand2',command=app.quit)
        self.exit_button.pack(side=tk.BOTTOM)

        # Create buttons for navigate to covid-19 study

        button_covid = ttk.Button(rightFrame, cursor='hand2', text="Covid19 Cases Finder", command=lambda:app.show_frame(CovidScreen))
        button_covid.pack(side=LEFT, padx=20, pady=20)
        button_sns = ttk.Button(rightFrame, cursor='hand2', text="Stop and Search Finder", command=lambda:app.show_frame(StopNSearchScreen))
        button_sns.pack(side=LEFT, padx=10, pady=10)
        




class StopNSearchScreen(tk.Frame):
    def __init__(self, app ):
        tk.Frame.__init__(self, app)

        middleFrame = tk.Frame(self, width=100)
        middleFrame.pack(fill=BOTH,expand=True, anchor=CENTER)

        case_1 = tk.Label(middleFrame, text='Stop and Search Queries',borderwidth=1, relief='solid',justify='center',background='grey', foreground='white', width=30)
        case_1.pack(side=tk.TOP,expand=True, padx=20, pady=20)

        but_1 = ttk.Button(middleFrame, cursor='hand2',text='Stop and Searches by force in a month', command=lambda:app.show_frame(SnS.SnSFunction))
        but_1.pack(side=tk.TOP,expand=True, pady=5)
        back_button = ttk.Button(
                                 middleFrame, cursor='hand2', text='Back',
                                 command=lambda:
                                 app.show_frame(StartPage))
        back_button.pack(side=TOP)

        # Create quit button
        quit_button = ttk.Button(
                                middleFrame, cursor='hand2', text='Exit',
                                command=app.quit)
        quit_button.pack(side=TOP)


class CovidScreen(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app, padx=50)

        middleFrame = tk.Frame(self, width=100)
        middleFrame.pack(fill=BOTH, expand=True, side=TOP  )

        case_1 = tk.Label(middleFrame,text='Covid19 cases in UK',borderwidth=1, relief='solid',justify='center',background='grey', foreground='white', width=30)
        case_1.pack(side=tk.TOP, expand=True, pady=20, padx=20)
        
        but_1 = ttk.Button(middleFrame, cursor='hand2',text='Confirmed cases',command=lambda:app.show_frame(Case_Study_1))
        but_1.pack(side=tk.TOP, expand=True, pady=5)

        but_2 = ttk.Button(middleFrame, cursor='hand2',text='Compare two areas',command=lambda:app.show_frame(Case_Study_2))
        but_2.pack(side=tk.TOP, expand=True, pady=5)

        but_3 = ttk.Button(middleFrame, cursor='hand2', text='Five areas with highest number of cases', command=lambda:app.show_frame(Case_Study_3))
        but_3.pack(side=tk.TOP, expand=True, pady=5)
        back_button = ttk.Button(
                                 middleFrame, cursor='hand2', text='Back',
                                 command=lambda:
                                 app.show_frame(StartPage))
        back_button.pack(side=TOP)

        # Create quit button
        exit_button = ttk.Button(
                                middleFrame, cursor='hand2', text='Exit',
                                command=app.quit)
        exit_button.pack(side=TOP)
        