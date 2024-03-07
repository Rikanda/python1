from pprint import pprint

import import_csv
import export_csv

def import_data(d):
    datalist = import_csv.parseCSV(d)
    return datalist

data = 'testdata.csv'


def table(i_data):
    dataset = []
    for i in i_data:
        row = [i[0], i[20]+' '+i[21]+' '+i[22]+' '+i[23]+' '+i[24]+' '+i[25]+' '+i[26]+' '+i[27]+' '+i[28]+' '+i[29]]
        dataset.append(row)
    pprint(dataset)
    return dataset

dset = table(import_data(data))

def export_data(ds):
    export_csv.create(ds)

export_data(dset)
