import matplotlib.pyplot as plt

class Plotter():
    """
    Context manager which creates, saves, and shows a plot on exit.
    """
    def __init__(self, *args, filename=None, show=True, **kwargs):

        self.filename = filename
        self.args = args
        self.kwargs = kwargs
        self.show = show

    def __enter__(self):
        self.fig, self.ax = plt.subplots(*self.args, **self.kwargs)
        return self.ax

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            # Pass through errors
            raise exc_type(str(exc_val))
        if self.filename:
            self.fig.savefig(self.filename)
        if self.show:
            plt.show()
            

        plt.close(self.fig)
        return True
