from pprint import pprint

import import_csv
import export_csv

def import_data(d):
    datalist = import_csv.parseCSV(d)
    return datalist




def table(i_data):
    dataset = []
    for i in i_data:
        row = [i[0], i[20]+' '+i[21]+' '+i[22]+' '+i[23]+' '+i[24]+' '+i[25]+' '+i[26]+' '+i[27]+' '+i[28]+' '+i[29]]
        dataset.append(row)
  #  pprint(dataset)
    return dataset

data = 'testdata.csv'
dset = table(import_data(data))

def table2(i_data):
    dataset = []
    for i in i_data:
        row = i[3]
        dataset.append(row)
    #set1 = list(set(dataset))
    return dataset

data1 = 'study24.csv'
ctrs = table2(import_data(data1))
#pprint(ctrs)
export_csv.transform(ctrs)



def export_data(ds):
    export_csv.create(ds)

#export_data(dset)
