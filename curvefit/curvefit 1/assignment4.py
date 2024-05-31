import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv

#for storing data of all universities initializing parameters
GRE = []
TOEFL = []
university_rating = []
CGPA = []
SOP = []
LOR = []
adm_chance = []
research = []
#for storing data of top ranked university initializing parameters
GRE5 = []
TOEFL5 = []
CGPA5 = []
SOP5 = []
LOR5 = []
adm_chance5 = []
research5 = []
#reading data from csv file
with open('Admission_Predict_Ver1.1.csv','r') as csv_file:
    read = csv.reader(csv_file)
    next(read, None)
    
    #storing the data
    for row in read:
        university_rating.append(float(row[3]))
        SOP.append(float(row[4]))
        LOR.append(float(row[5]))
        CGPA.append(float(row[6]))
        research.append(float(row[7]))
        adm_chance.append(float(row[8]))
        GRE.append(float(row[1]))
        TOEFL.append(float(row[2]))
    
    #starting again from the start of csv file
    csv_file.seek(0)
    next(read, None)
    
    #storing the data of top ranked university
    for row in read:
        if float(row[3]) == 5 :
            SOP5.append(float(row[4]))
            LOR5.append(float(row[5]))
            CGPA5.append(float(row[6]))
            research5.append(float(row[7]))
            adm_chance5.append(float(row[8]))
            GRE5.append(float(row[1]))
            TOEFL5.append(float(row[2]))
    
    # converting them into arrays
    CGPA = np.asarray(CGPA)
    SOP = np.asarray(SOP)
    LOR = np.asarray(LOR)
    TOEFL = np.asarray(TOEFL)
    university_rating = np.asarray(university_rating)
    GRE = np.asarray(GRE)
    research = np.asarray(research)
    adm_chance = np.asarray(adm_chance)
    
    CGPA5 = np.asarray(CGPA5)
    SOP5 = np.asarray(SOP5)
    LOR5 = np.asarray(LOR5)
    TOEFL5 = np.asarray(TOEFL5)
    GRE5 = np.asarray(GRE5)
    research5 = np.asarray(research5)
    adm_chance5 = np.asarray(adm_chance5)
    
#scatter plots for observations through graphs    
plt.scatter(SOP, adm_chance, label= 'SOP')
plt.scatter(research, adm_chance, label = 'research')
plt.scatter(LOR, adm_chance, label = 'LOR')
plt.legend()
plt.savefig('scatter.png')    

#function for checking linear relationship
def stline(x,m,c):
    return m * x + c

# using least squares method
#for TOEFL
M = np.column_stack([TOEFL, np.ones(len(TOEFL))])
(p1, p2), _, _, _ = np.linalg.lstsq(M, adm_chance, rcond=None)
yest1 = stline(TOEFL, p1, p2)
#for GRE
M = np.column_stack([GRE, np.ones(len(GRE))])
(zp1, zp2), _, _, _ = np.linalg.lstsq(M, adm_chance, rcond=None)
yest2 = stline(GRE, zp1, zp2)
#plotting estimated values on the scatter plot
plt.scatter(TOEFL,adm_chance, label = 'TOEFL', color = 'green')
plt.scatter(GRE,adm_chance, label = 'GRE', color = 'orange')
plt.plot(TOEFL,yest1,color = 'red',label = 'TOEFL Estimated',)
plt.plot(GRE,yest2,color = 'blue',label = 'GRE Estimated')
plt.xlabel('TOEFL,GRE')
plt.ylabel('Admission chance')
plt.legend()
plt.savefig('fig1.png')
#for CGPA
M = np.column_stack([CGPA, np.ones(len(CGPA))])
(p1, p2), _, _, _ = np.linalg.lstsq(M, adm_chance, rcond=None)
yest = stline(CGPA, p1, p2)
#plotting estimated values on the scatter plot
plt.scatter(CGPA,adm_chance, label = 'CGPA')
plt.plot(CGPA,yest,color = 'red', label = 'Estimated')
plt.xlabel('CGPA')
plt.ylabel('Admission chance')
plt.legend()
plt.savefig('fig2.png')
#defining  polynomial function with all 7 parameters
def func(a,t1,t2,t3,t4,t5,t6,t7):
    return a[0] ** t1 + a[1] ** t2 + a[2] ** t3 + a[3] ** t4 + a[4] ** t5 + a[5] ** t6 + a[6] ** t7 
#forming a matrix
c  = []
c.append(CGPA)
c.append(SOP)
c.append(LOR)
c.append(GRE)
c.append(TOEFL)
c.append(university_rating)
c.append(research)
#using curve fit to estimate values
params_c, pcov = curve_fit(func, c, adm_chance,p0 = [1,0,0,1,1,0,0])
c1,c2,c3,c4,c5,c6,c7 = params_c
print(f"CGPA: {c1}, SOP: {c2}, LOR: {c3}, GRE: {c4}, TOEFL: {c5}, university_rating: {c6}, research: {c7}")
# function for analysing data of all 7 parameters for all universities    
def func(a,p1,t1,t2,t3,t4,t5,t6,t7):
    return p1 * a[0] ** t1 * a[1] ** t2 * a[2] ** t3 * a[3] ** t4 * a[4] ** t5 * a[5] ** t6 * a[6] ** t7 
#forming a matrix
a  = []
a.append(CGPA)
a.append(SOP)
a.append(LOR)
a.append(GRE)
a.append(TOEFL)
a.append(university_rating)
a.append(research)
#using curve fit to estimate values
params_a, pcov = curve_fit(func, a, adm_chance,p0 = [1,1,0,0,1,1,0,0])
pa,a1,a2,a3,a4,a5,a6,a7 = params_a
print(f"factor: {pa} ,CGPA: {a1}, SOP: {a2}, LOR: {a3}, GRE: {a4}, TOEFL: {a5}, university_rating: {a6}, research: {a7}")

# function for analysing data of all 7 parameters for top ranked university 
def func1(a,p1,t1,t2,t3,t4,t5,t6):
    return p1 * a[0] ** t1 * a[1] ** t2 * a[2] ** t3 * a[3] ** t4 * a[4] ** t5 * a[5] ** t6
#forming a matrix
b  = []
b.append(CGPA5)
b.append(SOP5)
b.append(LOR5)
b.append(GRE5)
b.append(TOEFL5)
b.append(research5)
#using curvefit to estimate values
params_b, pcov = curve_fit(func1, b, adm_chance5 ,p0 = [1,1,0,0,1,1,0])
pb,b1,b2,b3,b4,b5,b6 = params_b
print(f"factor: {pb} ,CGPA: {b1}, SOP: {b2}, LOR: {b3}, GRE: {b4}, TOEFL: {b5}, research: {b6}")