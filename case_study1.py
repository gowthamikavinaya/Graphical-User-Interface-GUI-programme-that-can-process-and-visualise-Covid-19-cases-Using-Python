import tkinter as tk
from tkinter.constants import BOTH, CENTER, LEFT, RIGHT, TOP
from tkcalendar import DateEntry
from tkinter import ttk, messagebox

from . import Start
from .helper_func.lists import area_list
from ttkwidgets.autocomplete import AutocompleteCombobox

import datetime

from app.helper_func.date_area_check import check
from app.helper_func.plot import PlotCovid19Cases


class Case_Study_1(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app, padx=50)
        


        # Create left frame and right frame:
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
        self.row6 = tk.Frame(self.leftFrame)
        self.row6.pack(side=TOP, expand=True)
        self.row7 = tk.Frame(self.leftFrame)
        self.row7.pack(side=TOP, expand=True)

        # Create start day option:
        

        # Create area option:
        self.area = ttk.Label(self.row1, text='Area:', font=10)
        self.area.pack(side=LEFT)
        self.area_entry = AutocompleteCombobox(self.row1, completevalues=area_list)
        self.area_entry.pack(side=LEFT)
        # # Set Hartlepool as default
        self.area_entry.insert(0, 'Hartlepool')
        
        self.date1 = ttk.Label(self.row2, text='Start date:', font=10)
        self.date1.pack(side=LEFT)
        self.start_date = DateEntry(self.row2, width= 16, background= "lightgreen", foreground= "white",bd=2, year=2020)
        self.start_date.pack(side=LEFT)
        # # Create end date option:

        self.date2 = ttk.Label(self.row3, text='End date:', font=10)
        self.date2.pack(side=LEFT)
        self.end_date = DateEntry(self.row3, width= 16, background= "lightgreen", foreground= "white",bd=2, year=2020)
        self.end_date.pack(side=LEFT)

        self.area_label = ttk.Label(self.row4, text='Area Type:', font=10)
        self.area_label.pack(side=LEFT)
        self.area_type_entry = AutocompleteCombobox(self.row4, completevalues=['ltla', 'utla'])
        self.area_type_entry.pack(side=LEFT)
        self.area_type_entry.insert(0, 'ltla')
        # Create query button:
        self.query1_button = ttk.Button(
                                  self.row5,
                                  text='Daily Cases', cursor='hand2',
                                  command=lambda:plot_daily_cases(self.start_date.get_date(), self.end_date.get_date(), self.area_entry.get(), self.area_type_entry.get()))

        self.query1_button.pack(side=LEFT)

        self.query2_button = ttk.Button(
                                  self.row5,
                                  text='Montly cases', cursor='hand2',
                                  command=lambda: plot_montly_cases(self.start_date.get_date(), self.end_date.get_date(), self.area_entry.get(), self.area_type_entry.get()))
        self.query2_button.pack(side=LEFT)

        # Create back button
        self.back_button = ttk.Button(
                                 self.row6, cursor='hand2', text='Back',
                                 command=lambda:
                            app.show_frame(Start.StartPage))
        self.back_button.pack(side=LEFT)

        # Create quit button
        self.quit_button = ttk.Button(
                                self.row7, cursor='hand2', text='Exit',
                                command=app.quit)
        self.quit_button.pack(side=LEFT)

        # Call check format function and Plot daily case
        def plot_daily_cases(start_date, end_date, area, areaType):
            errors = check(start_date, end_date, area)
            if len(errors)!=0:
                messagebox.showerror("error:", errors)
            else:
                plot = PlotCovid19Cases(str(start_date), str(end_date), str(areaType), self.rightFrame)
                plot.daily_cases(str(area))
        # Call check format function and Plot infection rate
        def plot_montly_cases(start_date, end_date, area, areaType):
            errors = check(start_date, end_date, area)
            if len(errors)!=0:
                messagebox.showerror("error:", errors)
            else:
                plot = PlotCovid19Cases(str(start_date), str(end_date), str(areaType), self.rightFrame)
                plot.monthly_cases(str(area))

