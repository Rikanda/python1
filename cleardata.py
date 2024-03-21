import util
import pprint
import array as arr

dpath = 'source/study24.csv'

dataset = util.import_data(dpath)
new_dataset = []
a = 0
for row in dataset:
    b = 0
    new_row = []
    for cell in row:
        if b < 24:
            new_row.append(cell)
            b += 1
    new_dataset.append(new_row)


# pprint.pprint(new_dataset[0:2])


def countries_list(dataset):
    countries = []
    for row in dataset:
        countries.append(row[3])
    list_countries = list(set(countries))
    country_path = 'results/country.csv'
    title = 'country'
    ccsv = util.export_data(list_countries, country_path, title)
    print(ccsv)


# 0 - исключаем, 1 -английские нэйтивы, 2 - иностранцы
cdpath = 'source/countrytype.csv'
country_dataset = util.import_data(cdpath)
# pprint.pprint(country_dataset)

native_dataset = []
for row in new_dataset[1:]:
    for c in country_dataset[1:]:
        if (row[3] == c[0]) and (c[1] == '1'):
            native_dataset.append(row)

foreigner_dataset = []
for row in new_dataset[1:]:
    for c in country_dataset[1:]:
        if (row[3] == c[0]) and (c[1] == '2'):
            print(row[3])
            foreigner_dataset.append(row)


def export_native(native_dataset, new_dataset):
    native_path = 'results/natives.csv'
    title = new_dataset[0]
    ncsv = util.export_data(native_dataset, native_path, title)
    pprint.pprint(ncsv)


foreigner_path = 'results/foreigners.csv'
title = new_dataset[0]
fcsv = util.export_data(foreigner_dataset, foreigner_path, title)
pprint.pprint(fcsv)
