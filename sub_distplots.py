import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

def create_sub_distplots(df):
    fig = plt.figure()
    col_size = df.columns.size
    one_size = math.ceil(col_size**0.5)
    f, axes = plt.subplots(one_size, one_size, figsize=(7,7))
    j = 0
    k = 0
    for i in range(0, col_size):
        pos = [j, k]
        sns.distplot(df.iloc[:, i], ax=axes[j, k])
        k = k + 1
        if k % one_size == 0:
            k = 0
            j = j + 1
        print(j, k)
    fig.subplots_adjust(top=0.88)
    plt.show()
