
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import export_scatterplot
import util


# путь к файлу и разделитель
p = 'source/study24.csv'
s = '\t'

df = util.declare_dataframe(p,s)

