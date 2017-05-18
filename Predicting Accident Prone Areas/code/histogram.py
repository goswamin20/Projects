import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
from pylab import *
from matplotlib import style
from matplotlib.backends.backend_pdf import PdfPages

data = pd.read_csv("Accidents_2015.csv",usecols=[27],na_values='0')  # reading and parsing the csv dataset
data=data.dropna(how='any') # as in the dataset 0 stands for no special reason condition we have removed it from the dataset
data_2 = data.ix[0:,['Special_Conditions_at_Site']] # Removing all the coloumns apart from Special_Conditions_at_Site in the dataset
data_2.plot(kind = 'hist')           # Hisogram Plotting the dataset using  Matplotlib From Pandas 
plt.xlabel("Special Conditions at Site ") # Labelling the X-Axis 
plt.show() # Showing the Histogram 
a = data_2.plot(kind='hist',title="Histogram for Special Conditions at Site ")   # Hisogram Plotting the dataset using  Matplotlib From Pandas  
plt.xlabel("Special Conditions at Site") # Labelling the X-Axis 
pp = PdfPages('Histogram.pdf')
pp.savefig(a.figure)
pp.close()
