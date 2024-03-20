import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

MY_DATASET = 'model.csv'
df = pd.read_csv(MY_DATASET)
#print(df.head())
x = df[['ukwac', 'subtitle', 'baroni', 'glove', "tasa", 'lse','dat']]
y = df['originality']
lr = LinearRegression()
lr.fit(x, y)
pred = lr.predict(x)
print(mean_absolute_error(y, pred), np.mean(y))

#sns.histplot(data = df['originality'], kde = True)
#plt.savefig("scatterplot.jpg")

sns.histplot(data = df['dat'], kde = True)
plt.savefig("scatterplot1.jpg")