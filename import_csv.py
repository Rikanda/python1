import csv

# преобразование данных в кортежи (вместе с заголовками)
def parseCSV(csv_file):
    data_list=[]
    with open(csv_file,'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            str_data = list(row)
            data_list.append(str_data)
    return(data_list)

#преобразование данных в кортежи без заголовков
def parseCSVdata(csv_file):
    data_list=[]
    with open(csv_file,'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        line_count = 0
        for row in reader:
            if line_count==0:
                line_count+=1
            else:
                str_data = list(row)
                data_list.append(str_data)
                line_count+=1
    return(data_list)
