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
 #   print(ccsv)


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
         #   print(row[3])
            foreigner_dataset.append(row)

all_dataset = []
for row in new_dataset[1:]:
    for c in country_dataset[1:]:
        if (row[3] == c[0]) and (c[1] != '0'):
            all_dataset.append(row)

def export_native(native_dataset, new_dataset):
    native_path = 'results/natives.csv'
    title = new_dataset[0]
    ncsv = util.export_data(native_dataset, native_path, title)
    pprint.pprint(ncsv)

def export_foreigners(foreigner_dataset, new_dataset):
    foreigner_path = 'results/foreigners.csv'
    title = new_dataset[0]
    fcsv = util.export_data(foreigner_dataset, foreigner_path, title)
    pprint.pprint(fcsv)



#export_foreigners(foreigner_dataset, new_dataset)
def fcreat():
    for_creativ = []
    for row in foreigner_dataset:
        if (row[7] != 'NA'):
            for_creativ.append(row)
    pprint.pprint(for_creativ)
    for_path = 'results/for_creativ.csv'
    title = new_dataset[0]
    fccsv = util.export_data(for_creativ, for_path, title)
    pprint.pprint(fccsv)

def ncreat():
    nat_creativ = []
    for row in native_dataset:
        if (row[7] != 'NA'):
            nat_creativ.append(row)
    #pprint.pprint(nat_creativ)
    for_path = 'results/nat_creativ.csv'
    title = new_dataset[0]
    nccsv = util.export_data(nat_creativ, for_path, title)
    pprint.pprint(nccsv)

all_path = 'results/all.csv'
title = new_dataset[0]
acsv = util.export_data(all_dataset, all_path, title)
pprint.pprint(acsv)

all_creativ = []
for row in all_dataset:
    if (row[7] != 'NA'):
        all_creativ.append(row)
pprint.pprint(all_creativ)
allc_path = 'results/all_creativ.csv'
title = new_dataset[0]
accsv = util.export_data(all_creativ, allc_path, title)
pprint.pprint(accsv)