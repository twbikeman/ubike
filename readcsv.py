import csv

csvfile = 'example1.csv'

'''
list1 = [[1,2,3],[2,4,6]]
with open(csvfile, 'a+', newline='\n') as fp:
    writer = csv.writer(fp)
    writer.writerow(['data1','data2','data3'])
    for row in list1:
        writer.writerow(row)
'''

with open(csvfile, "r", newline='') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar ="'")
    for row in reader:
        for line in row:
            if isinstance(line, str):
                print(line + '\t', end='')
        print()
    

