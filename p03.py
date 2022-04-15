import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 500, 50)
y1 = 2*x+1
y2 = x**2
plt.figure()
plt.plot(x, y1)
plt.show()

plt.figure()
plt.plot(x, y2)
plt.show()
