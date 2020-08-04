import matplotlib.pyplot as plt
import os

SHOW = True
BASE_FILEPATH = None

class Plotter():
    """
    Context manager which creates, saves, and shows a plot on exit.
    """
    def __init__(self, *args, filename=None, show=None, **kwargs):

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
            if BASE_FILEPATH is not None:
                self.fig.savefig(os.path.join(BASE_FILEPATH, self.filename))
            else:
                self.fig.savefig(self.filename)
        show = self.show 
        if show is None:
            show = SHOW
        if show:
            plt.show()
            

        plt.close(self.fig)
        return True
