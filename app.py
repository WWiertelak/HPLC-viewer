import pandas as pd
import numpy as np



class HPLC_viewer:

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def load_data(self, df, time_of_sep):
        self.data = df
        self.time = time_of_sep

    def clean_data(data):
        pass
        
        

        
model = HPLC_viewer("test")




