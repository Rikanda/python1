import util
import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import export_scatterplot


import sklearn
import warnings

from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score


# study_c = util.import_data('source/study32.csv')

# pprint.pprint(study_c[0])

# ident = 'id'
# y = 'aut.originality'
# x1 = 'age'
# x2 = 'gender'


# def dataset_export_semidis():
#     for_enrich = []
#     for row in study_c[1:]:
#         enrich_row = [row[0]]
#         word_row = row[18:]
#         stro = '{}'.format(' '.join(str(el) for el in word_row))
#         print(str)
#         enrich_row.append(stro)
#         for_enrich.append(enrich_row)
#     return for_enrich
#
#
# # util.semidis_export(for_enrich, 'results/studyc1.csv')
# # pprint.pprint(for_enrich)
#
# def dataset_export_lse():
#     for_enrich = []
#     studyindex = []
#     i = 0
#     for row in study_c[1:]:
#         i += 1
#         enrich_row = [i]
#         studyindex_row = [i, row[0]]
#         word_row = row[18:]
#         for word in word_row:
#             enrich_row.append(word)
#             studyindex_row.append(word)
#         for_enrich.append(enrich_row)
#         studyindex.append(studyindex_row)
#     return for_enrich, studyindex
#
#
# # datalse = dataset_export_lse()[0]
# # print(datalse[0])
# # controllse = dataset_export_lse()[1]
#
# # util.lse_export(datalse,'results/studyc2.csv')
#
# # util.any_export(controllse[1:],'results/studys_control.csv',controllse[0],',')
#
# # обработка 140 человек
# study1 = util.import_data('source/global140.csv')
#
#
# def dataset_export_lse():
#     for_enrich = []
#     for row in study1[1:]:
#         enrich_row = [row[1]]
#         word_row = row[30:]
#         for word in word_row:
#             enrich_row.append(word)
#         for_enrich.append(enrich_row)
#     return for_enrich
#
# data = dataset_export_lse()
#
# #util.lse_export(data,'results/study140.csv')
#
# flow = util.import_data('source/summary140.csv')
# ftitle = flow[0]
# flow1 = flow[1::2]
# itogtitle = study1[0] + flow[0][1:]
# #pprint.pprint(flow)
#
# itog = [itogtitle]
#
#
#
# for s in study1[1:]:
#     rowi = []
#     for f in flow1:
#         if s[1] == f[0]:
#             rowi=[*s,*f[1:4]]
#     itog.append(rowi)

#util.any_export(itog[1:],'results/dataset140.csv',itog[0],',')

df = util.declare_dataframe('source/dataset140.csv',',')

#pprint.pprint(itog[0])

y1 = 'aut_originality'


x1 = 'dat'
x2 = 'ukwac'
x3 = 'subtitle'
x4 = 'baroni'
x5 = 'glove'
x6 = 'tasa'
x7 = 'dsimean'
x8 = 'age'
x9 = 'gender'
x10 = 'aut_flexibility_1'
x11 = 'aut_flexibilit_2'
x12 = 'aut_flexibility'
x13 = 'aut_originality_1'
x14 = 'aut_originality_2'
x15 = 'aut_originality'
x16 = 'aut_fluency_1'
x17 = 'aut_fluency_2'
x18 = 'aut_fluency'
x19 = 'bag_appropriateness_1'
x20 = 'bag_appropriateness_2'
x30 = 'bag_appropriateness'
x31 = 'understood'
x32 = 'strategy'
x33 = 'valids'
x34 = 'Flow'
x35 = 'lse'

x = df[[x2,x3,x4,x5,x6,x34,x35]]
y = df[y1]

#print(df.info())

lr = LinearRegression()
lr.fit(x, y)

# print('Coefficients: ', lr.coef_)
# print('Variance score: {}'.format(lr.score(x, y)))

from sklearn.preprocessing import PolynomialFeatures

# poly_reg2 = PolynomialFeatures(degree=2)
# X_poly = poly_reg2.fit_transform(x)
# lin_reg_2 = LinearRegression()
# lin_reg_2.fit(X_poly, y)
#
# print('Coefficients: ', lin_reg_2.coef_)
# print('Variance score: {}'.format(lin_reg_2.score(X_poly, y)))

poly_reg3 = PolynomialFeatures(degree=3)
X_poly3 = poly_reg3.fit_transform(x)
lin_reg_3 = LinearRegression()
lin_reg_3.fit(X_poly3, y)

koef = lin_reg_3.coef_

#print('Coefficients: ', koef)
print('Variance score: {}'.format(lin_reg_3.score(X_poly3, y)))

from sklearn.linear_model import LassoLars
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Loading dataset
Flow0 = 0.929

DSI_ukwac1 = 0.8866
DSI_subtitle1 = 0.9462
DSI_baroni1 = 0.9319
DSI_glove1 = 0.9152
DSI_TASA1 = 0.9958
LSE1 = 0.946
dat1 = 85.85

xtlist = []
xtlist.append([0.8866, 0.9462, 0.9319, 0.9152, 0.9958, 0.923, 0.946])

DSI_ukwac2 = 0.8685
DSI_subtitle2 = 0.9439
DSI_baroni2 = 0.9235
DSI_glove2 = 0.9012
DSI_TASA2 = 0.997
LSE2 = 0.945
dat2 = 82.3

xtlist.append([0.8685, 0.9439, 0.9235, 0.9012, 0.997, 0.929, 0.945])
# ko =[]
# for k in koef:
#     ko.append(str(k))
#
# pprint.pprint(ko)
#
# util.export_data(ko, 'results/koef3.csv', 'Коэффициенты')

xdf = pd.DataFrame(xtlist)
print(xdf)

xt1 = xdf[[0,1,2,3,4,5,6]]
xt1_poly3 = poly_reg3.fit_transform(xt1)
DT_predict = lin_reg_3.predict(xt1_poly3) #Predictions on Testing data
print(DT_predict)
print(round(100 - (len(df[df[y1]>DT_predict[0]])/141)*100))
print(round(100 - (len(df[df[y1]>DT_predict[1]])/141)*100))

def print_scatter():
    v = df['dat']
    pf = str('dat')
    export_scatterplot.export_scpl(v, pf)

#print_scatter()

# Splitting training and testing data
# X_train, X_test, y_train, y_test = train_test_split(x, y,
#                                                     test_size=0.15, random_state=42)
#
# # Creating and fitting the regressor
# regressor = LassoLars(alpha=0.1)
# regressor.fit(X_train, y_train)
#
# # Evaluating model
# prediction = regressor.predict(X_test)
#
# print(f"r2 Score of test set : {r2_score(y_test, prediction)}")


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#print(df['dat'].corr(df[y1]))