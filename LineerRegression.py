import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,4])
slope, intercept, r_value, p_value, std_err = linregress(x,y)
print(f"slope = {slope}\nintercept = {intercept}\nr_value = {r_value}\np_value = {p_value}\nstd_err = {std_err}")
plt.plot(x,y,'o',label='original data')
plt.plot(x,slope*x+intercept,label='fitted line')
plt.legend()
plt.show()
