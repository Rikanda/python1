
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
def transform(datalist):
    csv = ''
    for d in datalist:
        csv += '{}\n'.format(','.join(str(el) for el in d))
        print(csv)
    with open('transformdata.csv', 'w', encoding="utf-8") as page:
        page.write(csv)
    return csv