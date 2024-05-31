import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#declaring values of h,c,kB
h = 6.626e-34
kB = 1.38e-23    
c = 3e8
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


def planck_formula(f,T):
    return (( 2 * h *(f ** 3) / (c ** 2)) * (((np.exp(((h * f)/ (kB * T))) - 1)**(-1))))

#using curve fit for estimating temperature
(p1), pcov = curve_fit(planck_formula, freq_data, intensity_data, p0 = 1000)
print(f"estimated temperature is {p1}")
#values of y from curvefit
intensity_curvefit = planck_formula(freq_data,p1)
plt.plot(freq_data,intensity_data, label = 'Original', color = 'green')
plt.plot(freq_data, intensity_curvefit, label = 'Estimated', color = 'red')

plt.title('Black Body Radiation')
plt.xlabel('Frequency')
plt.ylabel('Intensity')
plt.legend()
plt.savefig('dataset3_1.png')