def create(datalist):
    csv = 'id,text\n'
    for d in datalist:
        csv += '{}\n'.format(','.join(str(el) for el in d))

    with open('resultdata.csv','w', encoding="utf-8") as page:
        page.write(csv)
    return csv