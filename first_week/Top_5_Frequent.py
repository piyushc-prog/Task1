import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numbers = np.random.randint(1,101,1000)

freq = pd.Series(numbers).value_counts()

top5 = freq.iloc[:5]

print(top5)

plt.hist(numbers)
plt.title("Histogram of Random Numbers")
plt.xlabel("Numbers")
plt.ylabel("Frequency")
plt.show()