import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


numbers = np.random.randint(1, 101, 1000)

freq = pd.Series(numbers).value_counts()
top5 = freq.iloc[:5]

plt.hist(numbers, bins=20)
plt.title("histogram of the  random number")
plt.xlabel("number")
plt.ylabel("frequency")
plt.show()