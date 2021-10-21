from matplotlib import pylab
import numpy as np
import matplotlib.pyplot as mpl
a1 = np.linspace(0,10,25)
a2 = a1 * a1 + 2
print(a1,"\n"*2,a2)

pylab.plot(a1,a2,'r')
mpl.show()