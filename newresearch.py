import util
import pprint

study_c = util.import_data('source/study32.csv')

# pprint.pprint(study_c[0])

ident = 'id'
y = 'aut.originality'
x1 = 'age'
x2 = 'gender'


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


datalse = dataset_export_lse()[0]
print(datalse[0])
controllse = dataset_export_lse()[1]

util.lse_export(datalse,'results/studyc2.csv')

util.any_export(controllse[1:],'results/studys_control.csv',controllse[0],',')

