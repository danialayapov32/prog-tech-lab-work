import matplotlib.pyplot as plt

class PlotGenerator:
    def make_plot(self, df, preset):
        if preset['kind'] == 'line':
            plt.plot(df[preset['x']], df[preset['y']])
        else:
            plt.scatter(df[preset['x']], df[preset['y']])
        
        path = "out.png"
        plt.savefig(path)
        plt.close()
        
        return path