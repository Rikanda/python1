from pprint import pprint
import import_csv
import export_csv

def import_data(d):
    datalist = import_csv.parseCSV(d)
    return datalist

def table(data):
     for_enrich = []
     for row in data[1:]:
         enrich_row = [row[0]]
         word_row = row[18:]
         for word in word_row:
             enrich_row.append(word)
         for_enrich.append(enrich_row)
     return for_enrich

#data = 'sourse2/clearstudy1b.csv'

#lse_dset = table(import_data(data))
#pprint(lse_dset)

#lse export
#filepath = 'result2/forlse.csv'
#export_csv.lse_export(lse_dset,filepath)

flow = import_data('sourse2/lseresult.csv')
ftitle = flow[0]
flow1 = flow[1::2]

# выгрузка в файл для общей таблицы
datalist = flow1
filepath = 'sourse2/study1blse.csv'
title = ftitle
sep = ","
export_csv.transform(datalist, filepath, title, sep)