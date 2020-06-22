import numpy as np
import math

x = np.linspace(0, 2*math.pi, 100)
y = np.sin(x)

from plot_helper import Plotter

with Plotter(filename="demo.png", show=True, figsize=(10,10)) as ax:
    ax.plot(x,y)
    ax.set_xlabel("X")
    ax.set_ylabel("sin(x)")
    ax.set_title("A sine wave.")