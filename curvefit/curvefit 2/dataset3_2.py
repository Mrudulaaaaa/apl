import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#reading from dataset3
file = open("dataset3.txt")
file_rd = file.readlines()

y_data = []
x_data = []

for lines in file_rd:
    r = lines.split()
    x_data.append(float(r[0]))
    y_data.append(float(r[1]))
#creatin arrays to store data points       
freq_data = np.asarray(x_data)
intensity_data = np.asarray(y_data)
# function with all parameters
def planck_formula(f,T,h,c,kB):
    return (( 2 * h / (c ** 2))* (f ** 3)) / (np.exp((((h / (kB)) * f) / T) - 1))
#estimating all values using curvefit with proper initial values
popt, pcov = curve_fit(planck_formula, freq_data, intensity_data, p0 = [4800,5.9e-34,2.99999e8,1.00398e-23])
print(f"""Estimated temperature : {popt[0]}
          Estimated h : {popt[1]}
          Estimated c : {popt[2]}
          Estimated kB : {popt[3]}""")
#y values of curvefit
intensity_curvefit = planck_formula(freq_data,popt[0],popt[1],popt[2],popt[3])

plt.plot(freq_data,intensity_data, label = 'Original', color = 'green')
plt.plot(freq_data, intensity_curvefit, label = 'Estimated', color = 'red')
plt.title('Black Body Radiation')
plt.xlabel('Frequency')
plt.ylabel('Intensity')
plt.legend()

plt.savefig('dataset3_2.png')