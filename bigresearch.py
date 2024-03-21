import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import export_scatterplot
import util

# сформировать датасет: путь к файлу и разделитель
# p = 'source/study24.csv'
# s = '\t'

p = 'source/nat_creativ.csv'
s = ','

ndf = util.declare_dataframe(p, s)

p1 = 'source/for_creativ.csv'

fdf = util.declare_dataframe(p1, s)

p2 = 'source/all_creativ.csv'
adf = util.declare_dataframe(p2, s)
# вывод на печать графика - передать датафрейм, атрибут, порядковый номер файла с графиком

attrib = 'dat'


# util.print_scatter(fdf,attrib,4)

def print_mean():
    print('native_mean = ', ndf['dat'].mean(), ' s = ', ndf['dat'].std())
    print('foreigner_mean = ', fdf['dat'].mean(), ' s = ', fdf['dat'].std())
    print('all_mean = ', adf['dat'].mean(), ' s = ', adf['dat'].std())
    print('native_median = ', ndf['dat'].median())
    print('foreigner_median = ', fdf['dat'].median())
    print('all_median = ', adf['dat'].median())


print_mean()

f1 = 'aut.originality.1'
f2 = 'aut.originality.2'
f3 = 'aut.originality'
f4 = 'multilingual'
f5 = 'country'
f6 = 'gender'
f7 = 'age'
f8 = 'problems.cra'
y = 'dat'


def print_creativ():
    print('native_mean = ', ndf[f3].mean(), ' s = ', ndf[f3].std())
    print('foreigner_mean = ', fdf[f3].mean(), ' s = ', fdf[f3].std())
    print('native_median = ', ndf[f3].median())
    print('foreigner_median = ', fdf[f3].median())


print_creativ()


# print(fdf.info())

def scat_creat():
    util.print_scatter(fdf, f3, 5)
    util.print_scatter(ndf, f3, 6)
    util.print_scatter(adf, f3, 7)

scat_creat()


print('all correlation', adf[y].corr(adf[f3]))

