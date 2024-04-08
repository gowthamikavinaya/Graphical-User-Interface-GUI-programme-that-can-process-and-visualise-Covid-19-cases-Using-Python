import tkinter as tk
from tkinter.constants import LEFT, TOP
from tkcalendar import DateEntry
from tkinter import ttk, messagebox
from app.helper_func.date_area_check import sns_check
from . import Start
from app.helper_func.plot import PlotStopnSearch
from ttkwidgets.autocomplete import AutocompleteCombobox
from app.helper_func import stop_search, date_area_check


class SnSFunction(tk.Frame):
    def __init__(self, app, compare=False):
        tk.Frame.__init__(self, app)
        
        # title_label = tk.Label(
        #                        self, justify='center', font=25,
        #                        text='Teenagers stopped and searched by the forces',
        #                        borderwidth=1, relief='solid', anchor='c',
        #                        background='white', foreground='black')
        # title_label.grid(row=0, column=0, sticky='nesw', padx=11, pady=11)


        # Create left frame for entering data and right frame for plotting graphs
        self.topFrame = tk.Frame(self, height=100, pady=30, padx=20)
        self.topFrame.pack(side=TOP, pady=10)

        self.centerFrame = tk.Frame(self, width=600, height=400, bg='white')
        self.centerFrame.pack(side=TOP)
        self.bottomFrame = tk.Frame(self, bg='white')
        self.bottomFrame.pack(side=TOP)
        

        # Entry for choosing the force:
        area = ttk.Label(self.topFrame, text='Force:', font=10)
        area.pack(side=LEFT)
        force_entry = AutocompleteCombobox(self.topFrame, completevalues=stop_search.force_list)
        force_entry.insert(0, 'Avon-and-Somerset')
        force_entry.pack(side=LEFT)
        
        # choose an year 
        year = ttk.Label(self.topFrame, text='Year', font=10)
        year.pack(side=LEFT)
        year_entry = AutocompleteCombobox(self.topFrame, completevalues=stop_search.selected_years)
        
        year_entry.insert(0, '2019')
        year_entry.pack(side=LEFT)

        # Choose a month
        month = ttk.Label(self.topFrame, text='Month', font=10)
        month.pack(side=LEFT)
        month_entry = AutocompleteCombobox(self.topFrame, completevalues=stop_search.months)
        month_entry.pack(side=LEFT)
        month_entry.insert(0, '01')
        # Query button
        query1_button = ttk.Button(self.topFrame,text='Submit', cursor='hand2',command=lambda: plot_pie(force_entry.get(), year_entry.get(), month_entry.get()))

        query1_button.pack(side=LEFT)

        back_button = ttk.Button(
                                 self.bottomFrame, cursor='hand2', text='Back',
                                 command=lambda:
                                 app.show_frame(Start.StartPage))
        back_button.pack(side=LEFT)

        # Exit button
        quit_button = ttk.Button(
                                self.bottomFrame, cursor='hand2', text='Exit',
                                command=app.quit)
        quit_button.pack(side=LEFT)

        def plot_pie(area, year, month):
            err = date_area_check.sns_check(year, month, area)
            if len(err) > 0:
                messagebox.showerror("error", err)
            else:
                plot = PlotStopnSearch(year, month, area, self.centerFrame)

