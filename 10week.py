import 9week
import numpy as np


x_idx = header_cols.index(x_name)
y_idx = header_cols.index(y_name)


data_array = np.genfromtxt('plot_data.csv', delimiter=',', skip_header=1, usecols=(x_idx, y_idx))

print("Данные загружены в массив NumPy:")
print(data_array) 