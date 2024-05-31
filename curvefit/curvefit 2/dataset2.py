import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#reading from the dataset2
file = open("dataset2.txt")
file_rd = file.readlines()

line_data = []
y_data = []
x_data = []

for lines in file_rd:
    r = lines.split()
    x_data.append(float(r[0]))
    y_data.append(float(r[1]))
#creating arrays with the data points    
x_data = np.asarray(x_data)
y_data = np.asarray(y_data)
#for periodicity
autocorrelation = np.correlate(y_data,y_data, mode='full')
peak_index = np.argmax(autocorrelation)
estimated_periodicity = x_data[peak_index]  

print(f"Estimated periodicity using autocorrelation: {estimated_periodicity} seconds")
#intuitively from the graph
print("Estimated periodicity from the graph: 2.5 seconds") 
#matrix M using autocorrelation periodicty
M = np.column_stack([np.sin((2 * np.pi * x_data)/estimated_periodicity), np.sin(3 * (2 * np.pi * x_data)/estimated_periodicity), np.sin(5 * (2 * np.pi * x_data)/estimated_periodicity),np.ones(len(x_data))])
#matrix N using periodicity from the graph
N = np.column_stack([np.sin((2 * np.pi * x_data)/2.5), np.sin(3 * (2 * np.pi * x_data)/2.5), np.sin(5 * (2 * np.pi * x_data)/2.5),np.ones(len(x_data))])
#solivng the matrices
(p1, p2, p3, p4), _, _, _ = np.linalg.lstsq(M, y_data, rcond=None)
(sp1, sp2, sp3, sp4), _, _, _ = np.linalg.lstsq(N, y_data, rcond=None)

print(f"The estimated(from autocorrelation) equation is {p1} sinx + {p2} sin3x + {p3} sin5x + {p4}")
print(f"The estimated(from graph) equation is {sp1} sinx + {sp2} sin3x + {sp3} sin5x + {sp4}")
print("Frequency is 0.4")

#function representing the curve given
def sin_superpos1(x,p1,f,p2,p3,p4):
    return p1 * np.sin((2 * np.pi* f * x)) + p2 * np.sin(3*(2 * np.pi * x * f)) + p3 * np.sin(5*(2 * np.pi * x * f)) + p4

#estimated y values with frequency from the graph
y1 = sin_superpos1(x_data,sp1,0.4,sp2,sp3,sp4)
#estimated y values with frequency from autocorrelation
y = sin_superpos1(x_data,p1,1/estimated_periodicity,p2,p3,p4)
#graphs
plt.plot(x_data,y_data,label = 'From Data', color = 'green')
plt.plot(x_data, y, color = 'orange', label = 'Estimated using periodicity from autocorrelation')
plt.plot(x_data, y1, color = 'red', label = 'Estimated using periodicity from the graph')

#using curvefit
(s1,f, s2, s3, s4), _ = curve_fit(sin_superpos1, x_data, y_data, p0 = [6,0.4,2,0.8,-0.03] )
#y values from curvefit
y_curvefit = sin_superpos1(x_data,s1,f,s2,s3,s4)
print(f"""The estimated equation using curve fit if {s1} sin({2*np.pi*f} x) + {s2} sin({3*2*np.pi*f} x) + {s3} sin({5*2*np.pi*f} x) + {s4}
with frequency {f}""")
plt.plot(x_data,y_curvefit,color = 'blue', label = 'curve fit')

plt.title('Dataset 2')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc = 'upper right')
plt.savefig('dataset22.png')