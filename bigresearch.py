import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

MY_DATASET = 'study24.csv'
df = pd.read_csv(MY_DATASET, sep='\t')
print(df.head())


sns.histplot(data = df['dat'], kde = True)
plt.savefig("bigscatterplot.jpg")