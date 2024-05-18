import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1 = np.random.rand(100)
y1 = np.random.rand(100)
z1 = np.random.rand(100)
ax.scatter(x1, y1, z1, s=20, color='red')

plt.show()
