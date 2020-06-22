# Plot-Helper

This is a context manager for matplotlib figures. It creates a new
pair of figure/axes upon entry and saves, plots, and clears the figure on exit.

This is a little cleaner than manually saving and drawing figures made with
matplotlib and this makes it easier to use the [object oriented API](https://matplotlib.org/3.2.1/api/index.html#the-object-oriented-api) of matplotlib
which gives you more control and flexibility over the default pyplot api.

# Installation

    pip install plot-helper

# Usage

```python
    import numpy as np
    import math

    x = np.linspace(0,2*math.pi,100)
    y = np.sin(x)

    from plot_helper import Plotter
    with Plotter(filename="where_to_save.png", show=True, figsize=(10,10)) as ax:
        ax.plot(x,y)
```

This will save the plot to `where_to_save.png` and also show it. Both `filename`
and `show` are optional parameters, and any other arguments will be passed to
the `plt.subplots` function.

# Miscellaneous

This is mostly a convenience for me since I use matplotlib a lot in my projects
so I often copy paste this thing everywhere I go. Any feedback and contributions
is welcome.