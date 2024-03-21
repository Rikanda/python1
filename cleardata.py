import util
import pprint
import array as arr

dpath = 'source/study24.csv'

dataset = util.import_data(dpath)
new_dataset = []
a =0
for row in dataset:
    b = 0
    new_row = []
    for cell in row:
        if b < 24:
            new_row.append(cell)
            b +=1
    new_dataset.append(new_row)

#pprint.pprint(new_dataset[0:2])






