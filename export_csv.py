# выгрузка для semidis
def create(datalist):
    csv = 'id,text\n'
    for d in datalist:
        csv += '{}\n'.format('\t'.join(str(el) for el in d))
        print(csv)
    with open('results/resultdata.csv', 'w', encoding="utf-8") as page:
        page.write(csv)
    return csv


# выгрузка произвольного списка в csv
def transform(datalist, filepath, title, sep):
    csv = '{}\n'.format(sep.join(str(el) for el in title))
    for d in datalist:
        csv += '{}\n'.format(sep.join(str(el) for el in d))
    with open(filepath, 'w', encoding="utf-8") as page:
        page.write(csv)
    return csv

def column(datalist, filepath, title):
    csv = title
    for d in datalist:
        csv += '\n'+d
    with open(filepath, 'w', encoding="utf-8") as page:
        page.write(csv)
    return csv