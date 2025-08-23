import numpy as np
a = np.arange(6)
print(a)
b= a.reshape((2,3))
print("Reshaped:\n",b)
print(np.mean(a))
print(np.median(a))
print(np.std(a))

