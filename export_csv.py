# выгрузка для semidis
def create(datalist, filepath):
    csv = 'id,text\n'
    for d in datalist:
        csv += '{}\n'.format(','.join(str(el) for el in d))
        print(csv)
    with open(filepath, 'w', encoding="utf-8") as page:
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
        csv += '\n' + d
    with open(filepath, 'w', encoding="utf-8") as page:
        page.write(csv)
    return csv


# выгрузка для LSE
def lse_export(datalist, filepath):
    csv = 'Subject#,Word1,Word2,Word3,Word4,Word5,Word6,Word7,Word8,Word9,Word10\n'
    for d in datalist:
        csv += '{}\n'.format(','.join(str(el) for el in d))
        print(csv)
    with open(filepath, 'w', encoding="utf-8") as page:
        page.write(csv)
    return csv
