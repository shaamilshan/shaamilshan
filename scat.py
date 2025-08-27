import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x,y,color = 'red', marker='x')
plt.title("scatter plot")
plt.show()