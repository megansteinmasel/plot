import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([30, 13, 26, 29, 40])
x1points = np.array([26, 10, 22, 25, 37])
ypoints = np.array(["Josie", "Chris", "Jessica", "Tracey", "Terry"])

plt.plot(ypoints, xpoints, 'r', marker ='o')
plt.plot(x1points, 'o:r')
plt.ylabel("Seconds")

plt.grid(axis = 'y')
title = "Task Results"
plt.title(title, loc = 'left')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
