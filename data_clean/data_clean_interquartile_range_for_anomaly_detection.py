import pandas as pd
import numpy as np


s = pd.Series([2.1, 2.3, 4.5, 2.2, 2.4])
Q1, Q3 = np.percentile(s, [23, 75])
IQR = Q3 - Q1
outliers = []
for item in s:
    if item < (Q1 - 1.5 * IQR) or item > (Q3 + 1.5 * IQR):
        outliers.append(item)

print(outliers)
