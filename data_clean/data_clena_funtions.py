import numpy as np
import pandas as pd


def find_anomaly_values_in_by_nedian(s:pd.Series, to_be=2) -> list:
    median = np.median(s)
    outlies = []

    for item in s:
        if abs(item - median) > to_be:
            outlies.append(item)

    return outlies


def find_anomaly_values_in_by_mean(s:pd.Series) -> list:
    mean = np.mean(s)
    std = np.std(s)
    outlies = []

    for item in s:
        if (item < mean - std) or (item > mean + std):
            outlies.append(item)

    return outlies


def find_anomaly_values_in_by_z_score_detection(s: pd.Series) -> list:
    mean = np.mean(s)
    std = np.std(s)

    outlies = []

    for item in s:
        z_score = (item - mean) / std
        if z_score > 1.5:
            outlies.append(item)

    return outlies


def find_anomaly_values_interquartile_range(s: pd.Series) -> list:
    Q1, Q3 = np.percentile(s, [23, 75])
    IQR = Q3 - Q1
    outliers = []
    for item in s:
        if item < (Q1 - 1.5 * IQR) or item > (Q3 + 1.5 * IQR):
            outliers.append(item)

    return outliers
