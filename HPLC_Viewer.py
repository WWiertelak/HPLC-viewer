import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Decorator of program output with name od application

def output_decorator(func):  
    def wrapper(self):
        print("-----------HPLC Glyco-Sep Viewer-----------")
        func(self)
        print("-----------HPLC Glyco-Sep Viewer-----------")
    return wrapper

#Main class 
class HPLC_Viewer:

    def __init__(self, name):
        self.name = name

    #Return the name of model
    @output_decorator
    def __str__(self) -> str:   
        return self.name
    
    #Function to load data to model. Input: Data Frame from Excel with raw data from HPLC; Time of eparation in minutes
    def load_data(self, raw_data: pd.DataFrame, run_time_minutes: float):
        self.data = pd.DataFrame()
        self.data['Flu'] = raw_data[49:-118]
        self.run_time_minutes = run_time_minutes

    #Add time value to every flurescence value and intrested range of separation
    def clean_data(self, start: int, stop: int):
        self.start = start
        self.stop = stop
        if self.start > self.run_time_minutes or self.stop > self.run_time_minutes:
            print(f"Value of time is higher than time of separation({self.run_time_minutes} [min])")
        else: 
            self.data['Time [min]'] = np.linspace(0, self.run_time_minutes, num=len(self.data))
            self.data = self.data[(self.data['Time [min]'] >= self.start) & (self.data['Time [min]'] <= self.stop)]
    
    #MinMax scale of fluorescence value
    def scale(self):
        flu_max = self.data['Flu'].max()
        flu_min = self.data['Flu'].min()
        self.data['Flu_scaled'] = (self.data['Flu'] - flu_min) / (flu_max - flu_min) 
    #Load retention time of dextran standard with Glucose Unit values
    def load_GU(self, GU: pd.DataFrame): 
        self.GU = GU


    #Return data
    @output_decorator
    def print_data(self):
        print(self.data)

    #Function to plot chart
    @output_decorator
    def plot(self):
        x = self.data['Time [min]']
        y = self.data['Flu_scaled']
        fig, ax1 = plt.subplots()
        ax1.plot(x, y)
        plt.title(self.name)
        plt.yticks([])
        plt.xlabel('Time [min]')
        plt.ylabel('Fluorescence')
        self.GU = self.GU[(self.GU['Time [min]'] >= self.start) & (self.GU['Time [min]'] <= self.stop)]
        ax2 = plt.twiny()
        ax2.set_xlabel("GU")
        ax2.set_xlim(ax1.get_xlim())
        ax2.set_xticks(self.GU['Time [min]'])
        ax2.set_xticklabels(self.GU['GU'])
        plt.show()
        

        
        
        
        

        

    




