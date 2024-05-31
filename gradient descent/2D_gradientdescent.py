import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#2D generic fucntion for gradient descent 
def generic(function, derivative,frange,bestx,learningrate):
    xbase = np.linspace(frange[0],frange[1],100)
    ybase = function(xbase)

    best_x = bestx
    bestcost = function(best_x)
    rangemin, rangemax = frange[0], frange[1]
#for plotting
    fig, ax = plt.subplots()
    ax.plot(xbase, ybase)
    ax.plot(best_x, bestcost, 'bo',label = 'starting point')
    xall, yall = [], []
    #tracks convergence
    lnall,  = ax.plot([], [], 'ro-',label = 'convergence')
    #gives the optimized point accordingly
    lngood, = ax.plot([], [], 'go', markersize=10, label = 'optimized point')

    lr = learningrate

    #for animation
    def onestepderiv(frame):
        nonlocal bestcost, bestx, lr
        xall.append(bestx)
        yall.append(function(bestx))
        #improving x each time
        x = bestx - derivative(bestx) * lr 
        bestx = x
        y = function(x)
        lngood.set_data(x, y)
        lnall.set_data(xall, yall)
    #animation   
    ani= FuncAnimation(fig, onestepderiv, frames=range(100), interval=1000, repeat=False)
    return ani

# To observe the plot for f1
# ani = generic(f1,f1_dx,[-5,5],4,0.05)
# plt.show()
# plt.legend()
