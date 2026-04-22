import matplotlib.pyplot as plt

class PlotGenerator:
    def make_plot(self, df, preset):
        col_x = preset['x']
        col_y = preset['y']
        plot_type = preset['kind'] 
        
        plt.figure(figsize=(8, 5))
        
        if plot_type == 'line':
            plt.plot(df[col_x], df[col_y])
        elif plot_type == 'scatter':
            plt.scatter(df[col_x], df[col_y])
            
        plt.xlabel(col_x)
        plt.ylabel(col_y)
        
        file_path = "out.png"
        plt.savefig(file_path)
        plt.close()
        
        return file_path
