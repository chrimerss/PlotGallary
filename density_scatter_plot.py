import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interpn
from scipy.stats import gaussian_kde
from matplotlibconfig import basic

# set configuration for plot
basic()

def scatter(x,y,**figkwargs):
    '''
    Make density scatter plot
    Args:
    ---------------
    :x - numpy.array object (None, 1)
    :y - numpy.array object (None, 1)

    Returns:
    ---------------
    :fig - matplotlib.pyplot object
    :axes - axes for the figure
    '''≈

    _max= max(x.max(), y.max())
    _min= min(x.min(), y.min())
    fig= plt.figure()
    axes= fig.add_subplot()
    data, x_e, y_e= np.histogram2d(x, y, bins=100)
    z= interpn( ( 0.5*(x_e[1:] + x_e[:-1]) , 0.5*(y_e[1:]+y_e[:-1]) ) ,
        data , np.vstack([x,y]).T , method = "splinef2d", bounds_error = False )
    idx= z.argsort() #move high density forward
    x, y, z= x[idx], y[idx], z[idx]
    ax= axes.scatter(x, y, c= z, s=50, edgecolor= '', cmap='jet', **figkwargs)
    axes.set_aspect('equal', 'box')
    axes.plot([_min, _max],[_min, _max], c='r')
    cb= plt.colorbar(orientation='vertical', mappable=ax)

    return fig, axes
