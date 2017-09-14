import shutil
from matplotlib import matplotlib_fname

shutil.copyfile(matplotlib_fname(), 'matplotlibrc')
