import util
import pprint


# study_c = util.import_data('source/study32.csv')

# pprint.pprint(study_c[0])

# ident = 'id'
# y = 'aut.originality'
# x1 = 'age'
# x2 = 'gender'


def dataset_export_semidis():
    for_enrich = []
    for row in study_c[1:]:
        enrich_row = [row[0]]
        word_row = row[18:]
        stro = '{}'.format(' '.join(str(el) for el in word_row))
        print(str)
        enrich_row.append(stro)
        for_enrich.append(enrich_row)
    return for_enrich


# util.semidis_export(for_enrich, 'results/studyc1.csv')
# pprint.pprint(for_enrich)

def dataset_export_lse():
    for_enrich = []
    studyindex = []
    i = 0
    for row in study_c[1:]:
        i += 1
        enrich_row = [i]
        studyindex_row = [i, row[0]]
        word_row = row[18:]
        for word in word_row:
            enrich_row.append(word)
            studyindex_row.append(word)
        for_enrich.append(enrich_row)
        studyindex.append(studyindex_row)
    return for_enrich, studyindex


# datalse = dataset_export_lse()[0]
# print(datalse[0])
# controllse = dataset_export_lse()[1]

# util.lse_export(datalse,'results/studyc2.csv')

# util.any_export(controllse[1:],'results/studys_control.csv',controllse[0],',')

# обработка 140 человек
study1 = util.import_data('source/global140.csv')


def dataset_export_lse():
    for_enrich = []
    for row in study1[1:]:
        enrich_row = [row[1]]
        word_row = row[30:]
        for word in word_row:
            enrich_row.append(word)
        for_enrich.append(enrich_row)
    return for_enrich

data = dataset_export_lse()

#util.lse_export(data,'results/study140.csv')

flow = util.import_data('source/summary140.csv')
ftitle = flow[0]
flow1 = flow[1::2]
itogtitle = study1[0] + flow[0][1:]
#pprint.pprint(flow)

itog = [itogtitle]



for s in study1[1:]:
    rowi = []
    for f in flow1:
        if s[1] == f[0]:
            rowi=[*s,*f[1:4]]
    itog.append(rowi)

util.any_export(itog[1:],'results/dataset140.csv',itog[0],',')
