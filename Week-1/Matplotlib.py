## 30. Introduction of Matplotlib
'''
- Matplotlib is a low-level graph plotting library in Python
- It is mainly used for data visualization, it helps turn raw data into charts and graphs
'''


## 31. Plotting
'''
- The plot() function is used to draw points (markers) on a diagram
- But by default, it does not just place points-it connects them with a line from point to point
- This function needs 2 parameters to specify points in the diagram
    + Parameter 1 is an array containing the points on the x-axis
    + Parameter 2 is an array containing the points on the y-axis
- For instance, if we want to plot a line from A(0, 0) to B(6, 250), we have to pass 2 arrays [0, 6] and [0, 250]
'''

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints, 'o')  
plt.title("Plotting graph")       # Plotting without Line use parameter 'o'
plt.show()

## 32. Markers
# We use the keyword marker to emphasize each point with a specified marker
xpoints1 = np.array([3, 8, 1, 10])
ypoints1 = np.array([6, 12, 30, 45])
plt.plot(xpoints1, ypoints1, 'p:r')
plt.title("Marker graph")
plt.show()

