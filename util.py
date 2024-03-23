import export_scatterplot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import export_scatterplot
import import_csv
import export_csv


# вывод на печать графика - передать датафрейм, атрибут, порядковый номер файла с графиком
def print_scatter(df, attrib, count):
    v = df[attrib]
    pf = str(count)
    export_scatterplot.export_scpl(v, pf)


# формирование датафрейма по пути к файлу и разделителю столбцов
def declare_dataframe(path, separ):
    MY_DATASET = path
    df = pd.read_csv(MY_DATASET, sep=separ)
    print(df.head())
    return df

#ыгрузка для обработки в семидис
def semidis_export(dataset, path):
    csvfile = export_csv.create(dataset, path)
    return csvfile

# выгрузка для lse
def lse_export(dataset, path):
    csvfile = export_csv.lse_export(dataset, path)
    return csvfile

def any_export(d,f,t,s):
    csvfile = export_csv.transform(d,f,t,s)
    return csvfile

# d - путь и файл для парсинга
def import_data(d):
    datalist = import_csv.parseCSV(d)
    return datalist


def export_data(d, filepath, title):
    if isinstance(title, str):
        csvfile = export_csv.column(d, filepath, title)
    else:
        s = ','
        csvfile = export_csv.transform(d, filepath, title, s)
    return csvfile
