import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#for 3d plotting
from mpl_toolkits.mplot3d import Axes3D

#generic gradient descent for 3D
def generic(function, derivative_x, derivative_y, frange, best_x, best_y,learningrate):
    xbase = np.linspace(frange[0], frange[1], 100)
    ybase = np.linspace(frange[0], frange[1], 100)
    xbase, ybase = np.meshgrid(xbase, ybase)
    zbase = function(xbase, ybase)

    # Set up some initial values
    bestx = best_x
    besty = best_y
    bestcost = f3(bestx, besty)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    rangemin, rangemax = frange[0], frange[1]
    #plotting surface of curve given
    ax.plot_surface(xbase, ybase, zbase, cmap='spring_r', alpha = 0.4)
    #giving arguments as bestx, besty, bestcost - lnall arguments should not be left empty
    xall, yall, zall = [bestx], [besty], [bestcost]
    lnall, = ax.plot([bestx], [besty], [bestcost], 'ro-', label = 'convergence')


    # Learning rate
    lr = learningrate

    def onestepderiv(frame):
        nonlocal bestcost, bestx, besty, lr
        xall.append(bestx)
        yall.append(besty)
        z = f3(bestx, besty)
        zall.append(z)  # Store the z value
        bestcost = z  # Update bestcost with the current cost
        x = bestx - df3_dx(bestx, besty) * lr
        y = besty - df3_dy(bestx, besty) * lr
        bestx = x
        besty = y

        # Update the data of lnall for the 3D line plot
        lnall.set_data(xall, yall)
        lnall.set_3d_properties(zall)

        #for observing the optimized point
        if frame == 99:
            ax.scatter([bestx], [besty], [bestcost], color='green', marker='o', s=100, label = 'optimized point')
            display_optimized_values(bestx, besty, bestcost)

    # Create an animation object
    ani = FuncAnimation(fig, onestepderiv, frames=range(100), interval=1000, repeat=False)
    return ani

# To observe the plot for f3
# ani = generic(f3, df3_dx, df3_dy, [-10,10],6,4,0.05)
# plt.show()
# plt.legend()