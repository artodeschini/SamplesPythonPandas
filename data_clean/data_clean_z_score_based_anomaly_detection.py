import pandas as pd
import numpy as np


# z score based anomalu detection
s = pd.Series([2.1, 2.3, 4.5, 2.2, 2.4])
media = np.mean(s)
desvio_padrao = np.std(s)

outlies = []

for item in s:
    z_score = (item - media) / desvio_padrao
    if z_score > 1.5:
        outlies.append(item)

print(outlies)