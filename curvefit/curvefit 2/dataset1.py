import numpy as np
import matplotlib.pyplot as plt
#reading from the dataset2
file = open("dataset1.txt")
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

M = np.column_stack([x_data, np.ones(len(x_data))])
# Use the lstsq function to solve for p1 and p2
(p1, p2), _, _, _ = np.linalg.lstsq(M, y_data, rcond=None)
print(f"The estimated equation is {p1} x + {p2}") 

def stline(x,m,c):
    return m * x + c

y = stline(x_data,p1,p2)

#for noise
y_noise = [y[i] - y_data[i] for i in range(len(y))] 

plt.plot(x_data,y_data,label = 'Noisy from dataset', color = 'green')
#error bar
plt.errorbar(x_data[::25], y_data[::25], np.std(y_noise), fmt='ro', label = 'Errorbar')
#estimated using least square
plt.plot(x_data,y,color ='orange',label = 'Estimated line')

plt.title('Dataset 1')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
plt.savefig('dataset1.png')