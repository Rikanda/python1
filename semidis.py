from pprint import pprint
import import_csv
import export_csv

def import_data(d):
    datalist = import_csv.parseCSV(d)
    return datalist


def table(i_data):
    dataset = []
    dataset_orogonality = []
    for i in i_data:
        if i[7]!= "NA":
            row = [i[0], i[18]+' '+i[19]+' '+i[20]+' '+i[21]+' '+i[22]+' '+i[23]+' '+i[24]+' '+i[25]+' '+i[26]+' '+i[27]]
            dataset.append(row)
            dataset_orogonality.append(i)
#    pprint(dataset)
#    pprint(dataset_orogonality)
    return dataset

def table2(i_data):
    dataset = []
    for i in i_data:
        row = i[0]
        dataset.append(row)
#    pprint(dataset)
    return dataset

data = 'sourse2/testdata2.csv'
dset = table(import_data(data))

# проверка пересечений с общей выборкой
data2 = 'source/dataset140.csv'
dset2 = table2(import_data(data2))

def common_row(dset1, dset2):
    common_data = []
    for i in dset1:
        for j in dset2:
            if i[0] == j[0]:
                common_data.append(i[0])
    return common_data

pprint(common_row(dset, dset2))



# выгрузка в файл семидис
#datalist = dset[1:]
#filepath = 'result2/forsemidis1.csv'
#export_csv.create(datalist, filepath)

# выгрузка в файл для общей таблицы
#datalist = dset[1:]
#filepath = 'sourse2/clearstudy1b.csv'
#title = dset[0]
#sep = ","
#export_csv.transform(datalist, filepath, title, sep)
