# Plot-Helper

[![PyPI
version](https://badge.fury.io/py/plot-helper.svg)](https://badge.fury.io/py/plot-helper)

This is a context manager for matplotlib figures. It creates a new
pair of figure/axes upon entry and saves, plots, and clears the figure on exit.

This is a little cleaner than manually saving and drawing figures made with
matplotlib and this makes it easier to use the [object oriented API](https://matplotlib.org/3.2.1/api/index.html#the-object-oriented-api) of matplotlib
which gives you more control and flexibility over the default pyplot api.

# Installation

    pip install plot-helper

# Usage

```python
    import math

    import numpy as np
    from plot_helper import Plotter    


    x = np.linspace(0,2*math.pi,100)
    y = np.sin(x)


    with Plotter(filename="where_to_save.png", show=True, figsize=(10,10)) as ax:
        ax.plot(x,y)
```

This will save the plot to `where_to_save.png` and also show it. Both `filename`
and `show` are optional parameters, and any other arguments will be passed to
the `plt.subplots` function.

You can also configure default values for a base_path where to save files to and
whether or not plots should be shown:

```python
    import math

    import numpy as np

    import plot_helper
    from plot_helper import Plotter    

    plot_helper.SHOW = True # Show all plots by default
    plot_helper.BASE_FILEPATH = "demo" # Save all plots in this script under the folder demo/

    x = np.linspace(0,2*math.pi,100)
    y = np.sin(x)


    with Plotter(filename="where_to_save.png", figsize=(10,10)) as ax:
        # This will be saved under 'demo/where_to_save.png" 
        # Also the plot will be shown upon exiting the with statement
        ax.plot(x,y)
```


# Miscellaneous

This is mostly a convenience for me since I use matplotlib a lot in my projects
so I often copy paste this thing everywhere I go. Any feedback and contributions
is welcome.