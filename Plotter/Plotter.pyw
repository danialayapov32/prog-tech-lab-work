import pandas as pd

class Plotter:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    def prepare_data(self, preset):
        self.df = pd.read_csv(self.csv_path)
        
        col_x = preset['x']
        col_y = preset['y']
        
        self.df = self.df[[col_x, col_y]].dropna(subset=[col_x, col_y])
        
        return self.df

