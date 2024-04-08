import tkinter as tk
from tkinter.constants import BOTH, LEFT, RIGHT, TOP
from tkcalendar import DateEntry
from tkinter import ttk, messagebox
from . import Start
from .helper_func.lists import area_list
import datetime

from app.helper_func.date_area_check import check
from app.helper_func.plot import PlotCovid19Cases
from ttkwidgets.autocomplete import AutocompleteCombobox


class Case_Study_2(tk.Frame):
    def __init__(self, app, compare=False):
        tk.Frame.__init__(self, app)
        
        # self.title_label = tk.Label(
        #                        self, justify='center', font=20,
        #                        text='Compare areas in terms of daily/monthly cases',
        #                        borderwidth=1, relief='solid', anchor='c',
        #                        background='white', foreground='black')
        # self.title_label.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)


        # Left frame
        self.leftFrame = tk.Frame(self, height=100, pady=30, padx=20, background='lightblue')
        self.leftFrame.pack(side=LEFT, pady=10, fill=BOTH )

        self.rightFrame = tk.Frame(self, width=400, height=500, bg='white')
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

        # 
        self.area = ttk.Label(self.row1, text='Area:', font=10)
        self.area.pack(side=LEFT)
        self.area_entry1 = AutocompleteCombobox(self.row1, completevalues=area_list)
        self.area_entry1.pack(side=LEFT)
        # Set Hartlepool as default
        self.area_entry1.insert(0, 'Hartlepool')


        self.area2 = ttk.Label(self.row2, text='Area 2:', font=10)
        self.area2.pack(side=LEFT)
        self.area_entry2 = AutocompleteCombobox(self.row2, completevalues=area_list)
        self.area_entry2.pack(side=LEFT)
        # Set Middlesbrough as default
        self.area_entry2.insert(0, 'Middlesbrough')   

        
        self.date1 = ttk.Label(self.row3, text='Start date:', font=10)
        self.date1.pack(side=LEFT)
        self.start_date = DateEntry(self.row3, width= 16, background= "lightgreen", foreground= "white",bd=2, year=2020)
        self.start_date.pack(side=LEFT)
        # Create end date option:

        self.date2 = ttk.Label(self.row4, text='End date:', font=10)
        self.date2.pack(side=LEFT)
        self.end_date = DateEntry(self.row4, width= 16, background= "lightgreen", foreground= "white",bd=2, year=2020)
        self.end_date.pack(side=LEFT)

        self.area_label = ttk.Label(self.row5, text='Area Type:', font=10)
        self.area_label.pack(side=LEFT)
        self.area_type_entry = AutocompleteCombobox(self.row5,  completevalues=['ltla', 'utla'])
        self.area_type_entry.pack(side=LEFT)
        self.area_type_entry.insert(0, 'ltla')
        # Create query button:
        self.query1_button = ttk.Button(
                                  self.row6,
                                  text='Compare daily', cursor='hand2',
                                  command=lambda:plot_daily_cases(self.start_date.get_date(), self.end_date.get_date(), self.area_entry1.get(),self.area_entry2.get(), self.area_type_entry.get()))

        self.query1_button.pack(side=LEFT)

        self.query2_button = ttk.Button(
                                  self.row6,
                                  text='Compare Montly', cursor='hand2',
                                  command=lambda: plot_montly_cases(self.start_date.get_date(), self.end_date.get_date(), self.area_entry1.get(),self.area_entry2.get(), self.area_type_entry.get()))
        self.query2_button.pack(side=LEFT)

        # Create back button
        self.back_button = ttk.Button(
                                 self.row7, cursor='hand2', text='Back',
                                 command=lambda:
                                 app.show_frame(Start.StartPage    ))
        self.back_button.pack(side=LEFT)

        # Create quit button
        self.quit_button = ttk.Button(
                                self.row7, cursor='hand2', text='Exit',
                                command=app.quit)
        self.quit_button.pack(side=LEFT)

        # Call check format function and Plot daily case
        def plot_daily_cases(start_date, end_date, area,area2, areaType):
            errors = check(start_date, end_date, area)
            if len(errors)!=0:
                messagebox.showerror("error:", errors)
            else:
                plot = PlotCovid19Cases(str(start_date), str(end_date), str(areaType), self.rightFrame)
                plot.compare_daily_cases(str(area), str(area2))
        # Call check format function and Plot infection rate
        def plot_montly_cases(start_date, end_date, area,area2, areaType):
            errors = check(start_date, end_date, area)
            if len(errors)!=0:
                messagebox.showerror("error:", errors)
            else:
                plot = PlotCovid19Cases(str(start_date), str(end_date),str(areaType), self.rightFrame)
                plot.compare_monthly_cases(str(area), str(area2))
