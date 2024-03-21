import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def export_scpl(values, postfix):
    sns.histplot(data = values, kde = True)
    filename = "scatterplots/scatterplot" + postfix +".jpg"
    plt.savefig(filename)
