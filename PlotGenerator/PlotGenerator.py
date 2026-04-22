import matplotlib.pyplot as plt

class PlotGenerator:
    def create_chart(self, df, preset):
        kind = preset['kind']
        x, y = preset['x'], preset['y']
        
        if kind == 'line':
            plt.plot(df[x], df[y])
        else:
            plt.scatter(df[x], df[y])
        
        return plt 
    