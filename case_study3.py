import tkinter as tk
from tkinter.constants import BOTH, LEFT, RIGHT, TOP
from tkcalendar import DateEntry
from tkinter import ttk, messagebox
from . import Start

from ttkwidgets.autocomplete import AutocompleteCombobox
from app.helper_func.lists import area_list
from app.helper_func.date_area_check import check
from app.helper_func.plot import PlotCovid19Cases


class Case_Study_3(tk.Frame):
    def __init__(self, app, compare=False):
        tk.Frame.__init__(self, app)



        # Create a top frame center frame and bottom frame 
        self.leftFrame = tk.Frame(self, height=100, pady=30, padx=20, background='lightblue')
        self.leftFrame.pack(side=LEFT, pady=10, fill=BOTH )

        self.rightFrame = tk.Frame(self, width=600, height=500, bg='white')
        self.rightFrame.pack(side=RIGHT)

        self.row1 = tk.Frame(self.leftFrame)
        self.row1.pack(side=TOP, expand=True)
        self.row2 = tk.Frame(self.leftFrame)
        self.row2.pack(side=TOP, expand=True)
        self.row3 = tk.Frame(self.leftFrame)
        self.row3.pack(side=TOP, expand=True)
        self.row4 = tk.Frame(self.leftFrame)
        self.row4.pack(side=TOP, expand=True)
        self.row5 = tk.Frame(self.leftFrame)
        self.row5.pack(side=TOP, expand=True)
        

        # Choose a date
    
        date = ttk.Label(self.row1, text='Choose a date', font=10)
        date.pack(side=LEFT)
        date_entry = DateEntry(self.row1, width= 16, background= "lightgreen", foreground= "white",bd=2, year=2020)
        date_entry.pack(side=LEFT)
        #choose area type
        area_type = ttk.Label(self.row2, text='Area Type:', font=10)
        area_type.pack(side=LEFT)
        area_type_entry = AutocompleteCombobox(self.row2,  completevalues=['ltla', 'utla'])
        area_type_entry.pack(side=LEFT)
        area_type_entry.insert(0, 'ltla')
        # Create query button:
        query1_button = ttk.Button(
                                  self.row3,
                                  text='Areas with highest cases', cursor='hand2',
                                  command=lambda:plot_pie(date_entry.get_date(), area_type_entry.get()))

        query1_button.pack(side=LEFT)

        query2_button = ttk.Button(
                                  self.row4,
                                  text='Areas with highest cases bar plot', cursor='hand2',
                                  command=lambda: plot_bar(date_entry.get_date(), area_type_entry.get()))
        query2_button.pack(side=LEFT)

        # Create back button
        back_button = ttk.Button(
                                 self.row5, cursor='hand2', text='Back',
                                 command=lambda:
                                 app.show_frame(Start.StartPage))
        back_button.pack(side=LEFT)
    
        # Create quit button
        quit_button = ttk.Button(
                                self.row5, cursor='hand2', text='Exit',
                                command=app.quit)
        quit_button.pack(side=LEFT)
        # check year and plot a pie chart
        def plot_pie(date, areaType):
            if(date.year != 2020):
                messagebox.showerror("The year should be 2020")
            else:
                plot = PlotCovid19Cases(None, None, str(areaType), self.rightFrame) 
                plot.cases_highest(str(date))
                
        # check year and plot a bar chart
        def plot_bar(date, areaType):
            if(date.year != 2020):
                messagebox.showerror("The year should be 2020")
            else:
                plot = PlotCovid19Cases(None, None, str(areaType), self.rightFrame) 
                plot.plot_highest_bar(str(date))
 
