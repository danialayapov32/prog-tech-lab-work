import numpy as np

class DataLoader:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.data_array = None

    def load_by_names(self, header_cols, x_name, y_name):
        x_idx = header_cols.index(x_name)
        y_idx = header_cols.index(y_name)
        
        self.data_array = np.genfromtxt(
            self.csv_path, 
            delimiter=',', 
            skip_header=1, 
            usecols=(x_idx, y_idx)
        )
        
        print("Данные загружены в массив NumPy:")
        return self.data_array
