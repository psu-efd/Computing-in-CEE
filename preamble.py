#This is my preamble.py file to set things at the beginning for a Jupyter Notebook.
#
#Include this preamble in Notebook at the begining with "import preamble" for easiness of use and to ensure consistency across all notebooks. 
# 
# by Xiaofeng Liu, Ph.D., P.E., Penn State University

# This line configures matplotlib to show figures embedded in the notebook, 
# instead of opening a new window for each figure. More about that later. 
# If you are using an old version of IPython, try using '%pylab inline' instead.
#%matplotlib inline

print("Start to load preamble.")

import numpy as np

from IPython.display import Image
from IPython.core.display import HTML 

#the following makes the plot to be inline (within the Notebook).
import matplotlib.pyplot as plt

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'png')
plt.rcParams['savefig.dpi'] = 75

#import libraries
import scipy.integrate as sp_int
import scipy.optimize as sp_opt
from pylab import *

__all__ = ['np', 'plt', 'sp_int', 'sp_opt']

print("Finished loading preamble.")