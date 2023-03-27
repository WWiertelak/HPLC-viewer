import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def output_decorator(func):
    def wrapper(self):
        print("-----------HPLC Glyco-Sep Viewer-----------")
        func(self)
        print("-----------HPLC Glyco-Sep Viewer-----------")
    return wrapper

class HPLC_Viewer:

    def __init__(self, name):
        self.name = name

    @output_decorator
    def __str__(self) -> str:
        return self.name

    def load_data(self, raw_data: pd.DataFrame, run_time_minutes: float):
        self.data = raw_data.rename(columns={1: 'Abs'})
        self.run_time_minutes = run_time_minutes

    def clean_data(self):
        time_per_event = self.run_time_minutes / len(self.data)
        self.data['Time (min)'] = np.linspace(0, time_per_event, num=len(self.data))
    
    def scale(self):
        abs_max = self.data['Abs'].max()
        abs_min = self.data['Abs'].min()
        self.data['Abs_scaled'] = (self.data['Abs'] - abs_min) / (abs_max - abs_min)

    @output_decorator
    def print_data(self):
        print(self.data)

    @output_decorator
    def plot(self):
        x = self.data['Time (min)']
        y = self.data['Abs_scaled']
        plt.plot(x, y)
        plt.title(self.name)
        plt.xlabel('Time (min)')
        plt.ylabel('Absorbance (scaled)')
        plt.show()
        print("Plot complete!")

        
        
        
        

        
model = HPLC_Viewer("test")


path_name = '/Users/wojciechwiertelak/python/HPLC-viewer/Data/data.xlsx'
db = pd.read_excel(path_name)
print(db)

model.load_data(db, 74)
model.clean_data()
model.scale()
model.plot()

