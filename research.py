# анализ выборки из 140 человек методом линейной регрессии

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import export_scatterplot

MY_DATASET = 'source/model.csv'
df = pd.read_csv(MY_DATASET)
# print(df.head())
x = df[['baroni','ukwac', 'subtitle', 'glove', "tasa", 'lse', 'dat']]
y = df['originality']
lr = LinearRegression()
lr.fit(x, y)
pred = lr.predict(x)
print(mean_absolute_error(y, pred), np.mean(y))

print('Coefficients: ', lr.coef_)

print('Variance score: {}'.format(lr.score(x, y)))
def print_scatter():
    v = df['dat']
    pf = str(2)
    export_scatterplot.export_scpl(v, pf)
