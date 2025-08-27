import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

categories = ['A','B','C']
values = [3,5,7]

plt.bar(categories,values,color = ['red','blue','green'])
plt.title("V Bar")
plt.show()