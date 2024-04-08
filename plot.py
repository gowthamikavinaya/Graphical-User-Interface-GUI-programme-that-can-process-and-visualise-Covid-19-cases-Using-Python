import json
from tkinter import Label
from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import requests as rq
from ..helper_func.lists import month_filter


class PlotStopnSearch:
    def __init__(self, year, month, force, rightFrame=None):
        self.year = year
        self.month = month
        self.frame = rightFrame
        self.force = force.lower()
        self.api('https://data.police.uk/api/stops-force?')
        self.df = None
    def api(self, url):
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
        headers = {
        'User-Agent': user_agent,
        'Accept':'application/json'
        }
        try:
            res = rq.get(f"{url}force={self.force}&date={self.year}-{self.month}", headers=headers, timeout=5)
            if res.ok:
                self.data = res.json()
                self.process_json()
            else:
                print(res.status_code)
        except:
            print("net error")
    def sort_(self, df):
        sort_data = df[self.df['age_range']=='18-24']
        return sort_data

    
    def plot_pie(self, sizes, labels):
        figure = plt.figure(figsize=(10, 5), dpi=80)
        chart = FigureCanvasTkAgg(figure,self.frame)
        chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')
        fig = figure.add_subplot(111)
        fig.pie(sizes, labels=labels, colors=['blue', 'green'])
        fig.legend(title=f"Teenagers stopped and searched by {self.force} force\nTotal: {sizes[0]+sizes[1]}\n {labels[0]}:{sizes[0]}\n{labels[1]}:{sizes[1]}")
        fig.grid()

    def process_json(self):
        type_ = set()
        count = []
        self.df = pd.DataFrame(self.data)
        sorted_by_age = self.sort_(self.df)
        for type in sorted_by_age['type']:
            type_.add(type)
        for i in type_:
            count.append(sorted_by_age['type'].value_counts()[i])

        self.plot_pie(list(count), list(type_))
        
        
    def monthly_cases(self):
        pass
    
class PlotCovid19Cases:
    def __init__(self, start_date = None, end_date = None, areaType = None, rightFrame=None):
        self.start_date = start_date
        self.end_date = end_date
        self.areaType = areaType
        self.frame = rightFrame
        self.data = self.read_csv()
    def read_csv(self):
        data = pd.read_csv('app/Data/specimenDate_ageDemographic-unstacked.csv', parse_dates=['date'])
        data['total_cases'] = data['newCasesBySpecimenDate-0_59'] + data['newCasesBySpecimenDate-60+']
        return data

    def start(self):
        self.mov7avg()
 
    def sort_data_by_area(self, area):
        sorted_data = self.data[(self.data.areaName == area) & (self.data.areaType == self.areaType) & (self.data['date'] >= self.start_date) & (self.data['date'] <= self.end_date)]
        return sorted_data
    def sort_data_by_day(self, day):
        return self.data[(self.data.areaType == self.areaType) & (self.data['date'] == day)]
    
    def plot_bar_graph(self, x, y, labelX, labelY, labelSize = 5):
        figure = plt.figure(figsize=(10, 5), dpi=70)
        chart = FigureCanvasTkAgg(figure,self.frame  )
        chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')
        fig = figure.add_subplot(111)
        fig.tick_params(axis='x', labelrotation=90, labelsize=labelSize)
        fig.bar(x, y, color="orange")
        fig.set_xlabel(labelX)
        fig.set_ylabel(labelY)
        fig.legend()
        fig.grid()

    def plot_line_graph(self, x_plot1,x_plot2, y_plot1,y_plot2, labelX, labelY, label1, label2):
        figure = plt.figure(figsize=(10, 5), dpi=80)
        chart = FigureCanvasTkAgg(figure,self.frame  )
        chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')
        fig = figure.add_subplot(111)
        fig.plot(x_plot1,y_plot1,label=label1, color="blue" )
        fig.plot(x_plot2, y_plot2, label=label2, color="green")
        plt.legend()

    def plot_highest_pie(self, sizes, labels):
        figure = plt.figure(figsize=(10, 5), dpi=80)
        chart = FigureCanvasTkAgg(figure,self.frame  )
        chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')
        fig = figure.add_subplot(111)
        if len(sizes) != 0:
            
            fig.pie(sizes, labels=labels)
            fig.grid()
        else:
            fig.text(0.3, 0.7,
         'No data found! query again',
         style = 'italic',
         fontsize = 20,
         bbox ={'facecolor':'green',
                'alpha':0.6,
                'pad':10})

            

    def plot_highest_bar(self, day):
        sorted_data = self.sort_data_by_day(day).nlargest(5, ['total_cases'])
        figure = plt.figure(figsize=(10, 5), dpi=70)
        chart = FigureCanvasTkAgg(figure,self.frame  )
        chart.get_tk_widget().grid(row=1, column=0, sticky='nesw')
        fig = figure.add_subplot(111)
        fig.tick_params(axis='x', labelrotation=90)
        fig.barh(sorted_data['areaName'], sorted_data['total_cases'], color="red")
        fig.set_xlabel('Area')
        fig.set_ylabel('Total Cases')
        fig.legend()
        fig.grid()
    
    def cases_highest(self, day):
        sorted_data = self.sort_data_by_day(day).nlargest(5, ['total_cases'])
        self.plot_highest_pie(sorted_data['total_cases'], sorted_data['areaName'])

    def compare_daily_cases(self, area1, area2):
        area1_sorted = self.sort_data_by_area(area1)
        area2_sorted = self.sort_data_by_area(area2)
        self.plot_line_graph(area1_sorted['date'],area2_sorted['date'], area1_sorted['total_cases'], area2_sorted['total_cases'],"Date", "Total new cases", area1_sorted.iloc[0]['areaName'], area2_sorted.iloc[0]['areaName'] )
    def compare_monthly_cases(self, area1, area2):
        area1_sorted = self.sort_data_by_area(area1)
        area2_sorted = self.sort_data_by_area(area2)
        x_axis = []
        y_axis1 = []
        y_axis2 = []
        months_set = set()
        for m in area1_sorted['date'].dt.month:
            months_set.add(m) 
        for mo in months_set:
            x_axis.append(month_filter[str(mo)])
        for i in months_set:
            y_axis1.append(area1_sorted[area1_sorted.date.dt.month == i]['total_cases'].sum())
            y_axis2.append(area2_sorted[area2_sorted.date.dt.month == i]['total_cases'].sum())
        self.plot_line_graph(x_axis, x_axis, y_axis1, y_axis2, "Month", "Total new cases", area1_sorted.iloc[0]['areaName'], area2_sorted.iloc[0]['areaName'])
    def daily_cases(self, area):
        sorted_data = self.sort_data_by_area(area)
        self.plot_bar_graph(sorted_data['date'], sorted_data['total_cases'], 'Date', 'Total new cases')

    def monthly_cases(self, area):
        sorted_data = self.sort_data_by_area(area)
        x = []
        y=[]
        months_set = set()
        for m in sorted_data['date'].dt.month:
            months_set.add(m) 
        for mo in months_set:
            x.append(month_filter[str(mo)])
        for i in months_set:
            y.append(sorted_data[sorted_data.date.dt.month == i]['total_cases'].sum())

        self.plot_bar_graph(x, y, 'Months', 'Total Cases', 15)
        
    
    

    
