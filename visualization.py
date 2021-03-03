# Visualization of all json files in folder
import matplotlib.pyplot as plt
import glob
import json
files = glob.glob('./*.json')

for file in files:
    with open(file, "r") as f:
        data = json.load(f)

        points = data['dataBuffer'][0]['values']
        units = data['dataBuffer'][0]['units']
        # Data for plotting
        t = range(len(points))
        voltage = points
        fig, ax = plt.subplots()
        ax.plot(t, voltage, 'r')

        ax.set(xlabel='time (mS)', ylabel=f'voltage ({units})',
               title='Visualization')
        ax.grid()
        plt.savefig(f"{file.strip('json')}png", dpi=300)
        plt.show()