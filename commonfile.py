from pprint import pprint
import import_csv
import export_csv

def import_data(d):
    datalist = import_csv.parseCSV(d)
    return datalist

data1 = import_data('sourse2/clearstudy1b.csv')
data2 = import_data('sourse2/study1bsemidis.csv')
data3 = import_data('sourse2/study1blse.csv')

def common_list (d1, d2, d3):
    commondata = []
    for d in d1[1:]:
        r = d
        for i in d2[1:]:
            if d[0] == i[0]:
                for el1 in i[2:]:
                    r.append(el1)
        for j in d3[1:]:
            if d[0] == j[3]:
                for el2 in j[1:]:
                    r.append(el2)
        commondata.append(r)
    return commondata

def common_title (d1, d2, d3):
    title = d1[0]
    t2 = d2[0]
    for k in t2[2:]:
        title.append(k)
    t3 = d3[0]
    for l in t3[1:]:
        title.append(l)
    return title


datalist = common_list(data1, data2, data3)
filepath = 'result2/std1b.csv'
title = common_title(data1, data2, data3)
sep = ","
export_csv.transform(datalist, filepath, title, sep)

print(title)
